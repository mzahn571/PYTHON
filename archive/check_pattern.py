#!/usr/bin/python
#Author: Nguyen Duc Trung Dung - Network Operator (GHP FarEast - VietNam) - ndtdung@ghp-fareast.vn
#Personal email: dung.nguyendt@gmail.com
#Blog: http://ndtdung.blogspot.com/
#Check_pattern
#Search for pattern in file and alert if pattern match
#Version 1.0 : Initial version
#License: GPL
#-------------------------------------------------------

import optparse, sys, datetime, re, commands

help_pat = 'Symbol\t\tMatches\n' \
           '------\t\t-------\n' \
           '|\t\tOR\n' \
           '^\t\tStart with\n' \
           '$\t\tEnd with\n' \
           '. (dot)\t\tAny single character\n' \
           '\d\t\tAny single digit\n' \
           '[A-Z]\t\tAny character between A and Z (uppercase)\n' \
           '[a-z]\t\tAny character between a and z (lowercase)\n' \
           '[A-Za-z]\tAny character between a and z (case-insensitive)\n' \
           '+\t\tOne or more of the previous expression (e.g., \d+ matches one or more digits)\n' \
           '[^/]+\t\tOne or more characters until (and not including) a forward slash\n' \
           '?\t\tZero or one of the previous expression (e.g., \d? matches zero or one digits)\n' \
           '*\t\tZero or more of the previous expression (e.g., \d* matches zero, one or more than one digit)\n' \
           '{1,3}\t\tBetween one and three (inclusive) of the previous expression (e.g., \d{1,3} matches one, two or three digits)\n\n' \
           'For more on regular expressions, see : http://docs.python.org/2/library/re.html#re-syntax'

#Get option
optp = optparse.OptionParser()
optp.add_option('-p', '--showpattern', help='show pattern help', action='store_true', dest='showpat')
optp.add_option('-n', '--name', help='name your search (Ex: errors, monster... one at time)', dest='name')
optp.add_option('-f', '--file', help='file location', dest='file')
optp.add_option('-s', '--schedule', help='STARTTIME-ENDTIME (Ex: 07:00-17:45,19:00-20:00)  default: 00:00-23:59', dest='times')
optp.add_option('-o', '--off', help='exclude days (Ex: Sunday,Saturday)             default: None', dest='offday')
optp.add_option('-e', '--error', help='error patterns to search (Ex: "error|caused by" OR "^server" OR etc.)', dest='errors')
optp.add_option('-i', '--ignorecase', help='ignore case sensitive', action='store_false', dest='case')
optp.add_option('-q', '--quite', help='do not print matched search', action='store_true', dest='quite')
optp.add_option('--line', help='number of last lines to check. Default: entire file', dest='line')
optp.add_option('--outfile', help='output result to FILE', dest='outfile')
optp.add_option('--mailto', help='send result to RECIPIENT (use "mail" command)', dest='outmail')
#Check if option full filled then parse
opts, args = optp.parse_args()
if opts.showpat is True:
    print help_pat
    sys.exit(0)
if opts.name is None or opts.errors is None or opts.file is None:
    optp.print_help()
    sys.exit(2)
if opts.offday is None:
    opts.offday = 'none'
if opts.times is None:
    opts.times = '00:00-23:59'
name = opts.name
schedules = opts.times.split(',')

#Check error function
def search_error():
    try:
        f = open(opts.file, 'r')
    except IOError as e:
        print 'Error - {0}: {1}'.format(e.strerror, e.filename)
        #raise
        sys.exit(2)
    else:
        out = f.read().split('\n')
        f.close()
        if opts.case is False: #ignore case
            pattern = re.compile(r'%s' %opts.errors, re.IGNORECASE)
        else:
            pattern = re.compile(r'%s' %opts.errors)
        msg = []
        if opts.line is None or int(opts.line) > len(out):#check line
            opts.line = len(out)
        else:
            opts.line = int(opts.line)
        for i in reversed(range(0, opts.line)):#search for pattern
            if pattern.search(out[i]):
                msg.append(out[i].replace('\r',''))
        if msg: #output
            emsXg = []
            if opts.outfile is not None: #output to file
                try:
                    f = open(opts.outfile + '.' + datetime.datetime.now().strftime('%Y%m%d'), 'a')
                except IOError as e:
                    emsXg.append('Error - {0}: {1}'.format(e.strerror, e.filename))
                else:
                    f.write('CRIT - %i %s found: ' %(len(msg), opts.name) + ', '.join(msg))
                    f.close()
            if opts.outmail is not None: #output to mail
                f = open('/tmp/check_pattern.tmp','w')
                f.write('CRIT - %i %s found: ' %(len(msg), opts.name) + ', '.join(msg))
                f.close()
                cmd = 'echo /tmp/check_pattern.tmp | mail -s "' + opts.name + ' found in ' + opts.file + '" ' + opts.outmail + ';rm -f /tmp/check_pattern.tmp'
                stat, out = commands.getstatusoutput(cmd)
                if stat <> 0:
                    emsXg.append(out)
            if len(msg) > 1:
                opts.name = opts.name + 's'
            if opts.quite is True: #do not print matched
                print 'CRIT - %i %s found in %s. %s' %(len(msg), opts.name, opts.file, ','.join(emsXg))
                sys.exit(2)
            else: #print matched
                print 'CRIT - %i %s found: %s. %s' %(len(msg), opts.name, ', '.join(msg), ','.join(emsXg))
                sys.exit(2)
        else:
            print 'OK - No %s found in %s' %(opts.name, opts.file)
            sys.exit(0)

#Main program
today = datetime.datetime.now().strftime("%A")
now = datetime.datetime.now().time()
con = datetime.time #convert number to time
pattern = re.compile('%s' %today, re.IGNORECASE)
if pattern.search(opts.offday):
    print 'OK - Not in working day'
    sys.exit(0)
else:
    for sche in schedules:
        start = map(int, sche.split('-')[0].split(':'))
        end = map(int, sche.split('-')[1].split(':'))
        if con(end[0],end[1]) < con(start[0],start[1]): #check if time is pass one day
            if (now >= con(start[0],start[1])) or (now <= con(end[0],end[1])):
                search_error()
            else:
                pass
        else:
            if (now >= con(start[0],start[1])) and (now <= con(end[0],end[1])):
                search_error()
            else:
                pass
    print 'OK - Out of schedule'
    sys.exit(0)