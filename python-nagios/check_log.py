#!/usr/bin/env python
# Check_log_files.py
# Author: Imran Ahmed <researcher6@live.com>
# Description: Nagios plugin that searches log files for a patterns loaded from a pattern file.
# Usage check_in_logfiles.py : <patfile> <logfile>
# First argument PATTERNFILE is a text file containing lines of the form:
# SEVERITY:PATTERN
# where *SEVERITY* is one of `IGNORE`, `WARNING`, `CRITICAL` and *PATTERN* is a
#  regular expression.
# Second (and later) argument LOGFILE is the path to one (or more) log files.
# if a line is found that matches a *PATTERN* with *SEVERITY* `CRITICAL`,
# exit with CRITICAL status 
# if a line is found that matches a *PATTERN* with *SEVERITY* `WARNING`,
# exit with WARNING status
  

import sys, re

def popLists(file):
        with open(file, 'r') as myPatFile:
                lines = myPatFile.readlines()
        critical = []
        warning = []
        ignore = []
        for line in lines:
                line = line.strip()
                words = line.split(":")
                if (words[0] =='CRITICAL'):
                        critical.append(words[1])
                elif (words[0] =='WARNING'):
                        warning.append(words[1])
                elif (words[0] =='IGNORE'):
                        ignore.append(words[1])
                else:
                        print   "unknown severity"
        return critical, warning, ignore



def main():
        argc = len(sys.argv)
        if argc<3:
                print "Usage :"
                print sys.argv[0]," <patfile> <logfile>"
                sys.exit(3)
        patFile = sys.argv[1]
        logFile = sys.argv[2]

        critical, warning, ignore = popLists(patFile)
        for i in ignore:
                for j in critical:
                        if j == i:
                                ignore.remove(j)
                for w in warning:
                        if w == i:
                                warning.remove(w)
        ## NOW WE START SEARCHING IN THE LOG FILE
     #   print critical
     #   print warning

        for c in critical:
                lf =open(logFile)
                for line in lf:
                        line = line.rstrip()
                        if re.search(c,line):
                                print "CRITICAL -" + c
                                #continue
                                sys.exit(2)
        for w in warning:
                lf =open(logFile)
                for wline in lf:
                        wline = wline.rstrip()
                        if re.search(w,wline):
                                print "WARNING -" + w
                                sys.exit(1)


if __name__ == "__main__":
        main()

