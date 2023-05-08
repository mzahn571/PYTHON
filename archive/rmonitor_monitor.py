#!/usr/bin/python
# Some parts, MIT licensed by <charlie@schluting.com>
# cbukolt/Denver

import time, sys, os, pyinotify
from smtplib import SMTP

global pdebug
pdebug = True
pdebug = False

# Open file, skip to end
global fh
fn = '/var/log/nagios/remote_logs/rmonitor/rmonitor'
fh = open(fn, 'r')
fh.seek(0,2)

global ratelimit
ratelimit = {}

wm = pyinotify.WatchManager()

dirmask = pyinotify.IN_MODIFY | pyinotify.IN_DELETE | pyinotify.IN_MOVE_SELF | pyinotify.IN_CREATE

class eventHandler(pyinotify.ProcessEvent):
        # This is the core code that processes lines, handles rate limitng, and sends email alerts
        def chkLine(self):
                for line in fh.readlines():
                        if 'removed' in line:
                                alert = 'FAILOVER'
                        elif 'Route' in line or 'route' in line:
                                alert = 'ROUTE'
                        elif 'Fail' in line or 'fail' in line:
                                if 'query' in line:
                                        continue
                                alert = 'FAIL'
                        else:
                                continue

                        # I'm disabling rate-limiting since once traffic fails over
                        # it requires manual intervention to switch back.  The script
                        # won't flood inboxes.

                        # Rate limiting - If we sent the same message in the last 24 hours,
                        # don't send it again.

                        # Scan through our ratelimit dict and remove expired entries.
                        # Failing to do this introduces a memory leak.
                        #try:
                        #for k in ratelimit.keys():
                        # Immediatly clear previous "DOWN" alert(s) if we are back UP
                        # so we don't  miss an alert.
                        # Note: k = the alert, ratelimit[k] is the entry date!
                        ##      if 'UP' in alert:
                        #               if 'down' in k:
                        #                       pass
                        #               elif 'Established to' in k:
                        #                       pass
                        #       elif ratelimit[k] <= time.time():
                        #               pass
                        #       else:
                        #               continue
                        #       ratelimit.pop(k)
                        ##except TypeError:
                        ##      print '[BUG] TypeError. k:', k, ' ratelimit:', ratelimit

                        ## Don't cache UPs
                        #if 'UP' not in alert:
                        #       # Strip timestamp
                        #       l = ' '.join(line.split(' ')[1:])
                        #       try:
                        #               if ratelimit[l]:
                        #                       if pdebug:
                        #                               print '[DEBG] Alert rate-limited'
                        #                       continue
                        #       except KeyError:
                        #               pass
                        #       #ratelimit[l] = time.time() + 86400 # 24 Hours
                        #       ratelimit[l] = time.time() + 3600 # 1 Hour
                        ## First time seeing alert, send notification and add to
                        ## rate limiting cache.
                        prefix = '[' + alert + ']'
                        msg = prefix + ' ' + line.rstrip()
                        if pdebug:
                                print '[DEBG] Alert is fresh: ', msg
                        else:
                                smtpObj = SMTP('localhost')
                                rec = 'pfagan@ccn.is.centurylink.net'
                                #rec = 'ECS-S1-Alerts@ccn.is.centurylink.net'
                                message = 'From: rmonitor_monitor.py\n' +\
                                 'To: ' + rec + '\n' +\
                                 'Subject: RMONITOR ALERT: ' + prefix + '\n' +\
                                 msg
                                smtpObj.sendmail('noreply@s1-mgmtX03.is.centurylink.net', rec, message)
                        #ratelimit[l] = time.time() + 86400 # 24 Hours

        # This reopens the fh handle after a logrotate
        def chkRotation(self, event):
                if fn in os.path.join(event.path, event.name):
                        if pdebug:
                                print "[DEBG] Reopen triggered!"
                        global fh
                        fh.close
                        fh = open(fn, 'r')
                        self.chkLine()
                        # Thanks to rate limiting, we can scan through the new file
                        # and not worry about double alerts or missing lines.
                        #fh.seek(0,2)
                return

        # Here is where we start, this gets called on every line.  We check if it's for ipsec
        # (remember we monitor the whole dir, see comment on line ~126) and if it is
        # we hand it off to chkLine for processing.
        def process_IN_MODIFY(self, event):
                if fn in os.path.join(event.path, event.name):
                        if pdebug:
                                print '[DEBG] File modified: ', event
                        self.chkLine()
                else:
                        if pdebug:
                                print '[DEBG] Modify called, but not matched: ', event

        def process_IN_MOVE_SELF(self, event):
                if pdebug:
                        print "[DEBG] File moved!  Still reading from old file."

        def process_IN_CREATE(self, event):
                # Note: Logrotate isn't triggering this, not sure why....
                # _IN_DELETE below is what actually gets called during a rotate.
                print '[DEBG] CREATE: ', event
                self.chkRotation(event)

        def process_IN_DELETE(self, event):
                if pdebug:
                        print "[DEBG] File deleted!", event
                self.chkRotation(event)



notifier = pyinotify.Notifier(wm, eventHandler())
# Need to watch the dir containing fn otherwise we can't detect logrotate
index = fn.rfind('/')
wm.add_watch(fn[:index], dirmask)

while True:
        try:
                notifier.process_events()
                if notifier.check_events():
                        notifier.read_events()
        except KeyboardInterrupt:
                break
