import sys
import time
from LOCAL_SSH import Session
from LOCAL_GET_RUN import *
from LOCAL_GET_SERIAL import *

enable = 'enable'
password = 'cisco'
shrun = 'show run'
termlength = 'terminal length 0'
			
if __name__== '__main__':
	print "This 'MASTER' file has been executed locally"
	b = Session()
	c = b.SSHConnect('10.10.10.1')
	d = c.invoke_shell()
	d.send(termlength + '\r')
	d.send(enable + '\r')
	d.send(password + '\r')  # d is the session
	e = Running_Config()
	f = e.GetRun(d)     #F has the config
	g = Serial()
	h = g.GetSerial(d) # is the Chassis and Serial
	print f
	print h
