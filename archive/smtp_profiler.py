#!/usr/bin/python

# check_by_ssh_mgmtX01!"/usr/bin/ssh -q s1-rptX01 $USER1$/check_smtp -t 20 -H mail5.ida.org"
# $USER1$/check_by_ssh -o ConnectionAttemailproxyts=3 -o ConnectTimeout=5 -E -t 30 -H IP ADDRESS -l syscheck -i $USER5$ -C$ARG1$

import subprocess
import datetime
import Queue
import threading
import time
import pickle

global q
q = Queue.Queue()

def testloop(host):
        while(True):
                p = subprocess.Popen('/usr/lib64/nagios/plugins/check_by_ssh -o ConnectionAttemailproxyts=3 -o ConnectTimeout=5 -E -t 30 -H IP ADDRESS -l syscheck -C "/usr/bin/ssh -q s1-rptX01 /usr/lib64/nagios/plugins/check_smtp -v -t 120 -H {0}"'.format(host), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = p.communicate()
                q.put([datetime.datetime.now(),host,out,err])
                time.sleep(5)

def main():
        targets = ['mail5.ida.org', ' mail4.ida.org']

        threads = []
        for host in targets:
                t = threading.Thread(target=testloop,args=(host,))
                t.setDaemon(True)
                threads.append(t)

        for thread in threads:
                thread.start()

        while(True):
                r = q.get()
                try:
                        with open('smtp_profiler.pkl', 'rb') as fh:
                                db = pickle.load(fh)
                except (EOFError,IOError) as e:
                        print 'Warning: Could not load output file.  First run? : {0} {0}'.format(e.message,e.args)
                        db = []
                with open('smtp_profiler.pkl', 'wb+') as fh:
                        db.append(r)
                        pickle.dump(db,fh)
                print 'output: {0}'.format(r)


if __name__ == '__main__':
        main()

