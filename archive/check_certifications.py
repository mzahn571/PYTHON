#!/usr/bin/python
# Check certificates on frontend hosts - cbukolt

import subprocess
import datetime

# Low
emailproxys_m = ['emailproxy02', 'emailproxy03', 'emailproxy04', 'emailproxy05']
emailproxys_y = ['emailproxy07', 'emailproxy08', 'emailproxy09']
emailproxys_l = ['emailproxy10', 'emailproxy11', 'emailproxy12']
dnspXs = ['dnspX01', 'dnspX02', 'dnspX03', 'dnspX04']
tlsXs = ['tlsX01', 'tlsX02']
rpts = ['rptX01'] # haha

# High
emsXs = ['emsX01', 'emsX02', 'emsX03', 'emsX04', 'emsX05',
        'emsX06', 'emsX07', 'emsX08', 'emsX09', 'emsX10']
dnssXs = ['dnssX01', 'dnssX02', 'dnssX03', 'dnssX04']

debug=True
debug=False

def check_cert_expire(host, location, jump):
        if jump:
                process = subprocess.Popen(['ssh', '-ttq', 'mgmtX01', 'ssh', '-ttq', host,\
                 '-C', '\"cat', location,  '|', 'openssl', 'x509', '-noout', '-enddate\"'],\
                 stdout=subprocess.PIPE)
        else:
                process = subprocess.Popen(['ssh', host, '-qC', 'cat', \
                 location,  '|', 'openssl', 'x509', '-noout', '-enddate'], stdout=subprocess.PIPE)

        out, err = process.communicate()

        if err:
                print '[E] ', host, ': ', err
                quit()

        if debug:
                print '[D] ', host, ': out: ', out[:-1]

        out = out.split('=')[1][:-1].strip()

        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        datetime.datetime.strptime(out, ssl_date_fmt)
        td = datetime.datetime.strptime(out, ssl_date_fmt) - datetime.datetime.utcnow()

        output = True

        if td.days < 0:
                output = '[E] ' + host + ': ' + location +  ': Expired on:' + out
        elif td.days < 90:
                output = '[W] ' + host + ': ' + location + ': Only ' + td.days + 'days remaining, expires:' + out
        elif debug:
                print '[D] ', host, ': Time remaining: ', td.days
        return output

msg = []

## Low

# Postfix on Loops
for emailproxy in emailproxys_l:
        msg.append(check_cert_expire(emailproxy, '/etc/pki/tlsX/certs/external.crt', True))

# External on rpts
for rpt in rpts:
        msg.append(check_cert_expire(rpt, '/etc/pki/tlsX/certs/external.crt', True))

# Internal on everyone (s1-hostname.crt)
for hostgroup in [emailproxys_m, emailproxys_y, emailproxys_l, dnspXs, tlsXs, rpts]:
        for host in hostgroup:
                location = '/etc/pki/tlsX/certs/s1-' + host + '.crt'
                msg.append(check_cert_expire(host, location, True))

## High

for hostgroup in [emsXs, dnssXs]:
        for host in hostgroup:
                location = '/etc/pki/tlsX/certs/s1-' + host + '.crt'
                msg.append(check_cert_expire(host, location, False))

try:
        # Clear "True"s
        msg = filter(lambda a: a != True, msg)

        # Convert to string
        msg = "\n".join(msg)
except:
        print "[E] Error processing msg! :", msg

if debug:
        print msg
else:
        from smtplib import SMTP
        smtpObj = SMTP('localhost')
        #rec = 'cbukolt@ccn.is.centurylink.net'
        rec = 'B3-Engineering@ccn.is.centurylink.net'
        message = 'From: chkcrt.py\n' +\
         'To: ' + rec + '\n' +\
         'Subject: Certificate Check Report\n' +\
         '(Is this email all jumbled? Click "Restore extra line breaks" above.)\n\n' +\
         msg
        smtpObj.sendmail('noreply@s1-mgmtX03.is.centurylink.net', rec, message)