#!/usr/bin/python
# Some parts, MIT licensed by <charlie@schluting.com>
# cbukolt/Denver

import time, sys, os, pyinotify
from smtplib import SMTP

global pdebug
pdebug = True
#pdebug = False

# Open file, skip to end
global fh
fn = '/var/log/fw/fw'
#fn = '/home/bukolt/ipsec-logs/just-fmsu.log'
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
                        #if 'Received delete notification' in line or\
                        # ('sshd' in line and 'fatal: Read from socket Failed:' in line) :
                                # The above check(s) are for noise we don't care about
                        #       continue
                        if 'RT_IDP'in line:
                                smtpObj = SMTP('localhost')
                                #rec = 'pfgan@ccn.is.centurylink.net'
                                rec = ['B3-Engineering@ccn.is.centurylink.net','pfagan@ccn.is.centurylink.net']
                                ts = line.split(' ')[0]
                                hn = line.split(' ')[1]
                                atk = line.split(',')[1]
                                action = line.split(',')[3]
                                name = line.split(',')[5]
                                idk = line.split(',')[12]

                                formatted = '\n\n'
                                for v in [ts,hn,atk,action,name,idk]:
                                    formatted += v + '\n\n'
                                formatted += '\n'
                                message = 'From: idp_monitor.py\n' +\
                                 'To: ' + ','.join(rec) + '\n' +\
                                 'Subject: ATTENTION HUMANS! RT_IDP THREAT DETECTED!\n\n' +\
                                 formatted + line
                                print message
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
                        #if pdebug:
                        #       print '[DEBG] File modified: ', event
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


print 'Sending startup email...'
smtpObj = SMTP('localhost')
rec = ['pfagan@ccn.is.centurylink.net','B3-Engineering@ccn.is.centurylink.net']
message = 'From: idp_monitor.py\n' +\
 'To: ' + ','.join(rec) + '\n' +\
 'Subject: idp_monitor is running\n' +\
 'hello humans.'
smtpObj.sendmail('noreply@s1-mgmtX03.is.centurylink.net', rec, message)
print 'done'
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