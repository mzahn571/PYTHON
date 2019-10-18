#!/usr/local/bin/python
from datetime import datetime
import subprocess
import sys

HOST1="ipsec01"
'HOST2="ipsec02"'
HOST3="ipsec03"
'HOST4="ipsec04"'
HOST5="ipsec05"
HOST6="ipsec06"
HOST1="ipsec07"

FORMAT = "%m%d%y"
PATH1 = "/data/1_Network_Config_Backups/IPSEC01/ipsec01_config"
PATH3 = "/data/1_Network_Config_Backups/IPSEC03/ipsec03_config"
PATH5 = "/data/1_Network_Config_Backups/IPSEC05/ipsec05_config"
PATH6 = "/data/1_Network_Config_Backups/IPSEC06/ipsec06_config"
PATH7 = "/data/1_Network_Config_Backups/FW01/fw01_config"

NEW_PATH1 = '%s_%s' % (PATH1,datetime.now().strftime(FORMAT))
NEW_PATH3 = '%s_%s' % (PATH3,datetime.now().strftime(FORMAT))
NEW_PATH5 = '%s_%s' % (PATH5,datetime.now().strftime(FORMAT))
NEW_PATH6 = '%s_%s' % (PATH6,datetime.now().strftime(FORMAT))
NEW_PATH7 = '%s_%s' % (PATH7,datetime.now().strftime(FORMAT))

COMMAND="show configuration | display set | no-more"

'************************************************************************'
f= ope(NEW_PATH1, "w")
ssh = subprocess.Popen(["ssh", "%s" % HOST1, COMMAND],
			stdout=f,
			stderr= subprocess.PIPE)

result = ssh.communicate()[0]
if result == []:
		error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
else:
	print result
'*************************************************************************'
f= ope(NEW_PATH1, "w")
ssh = subprocess.Popen(["ssh", "%s" % HOST1, COMMAND],
			stdout=f,
			stderr= subprocess.PIPE)

result = ssh.communicate()[0]
if result == []:
		error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
else:
	print result
'*************************************************************************'
f= ope(NEW_PATH3, "w")
ssh = subprocess.Popen(["ssh", "%s" % HOST3, COMMAND],
			stdout=f,
			stderr= subprocess.PIPE)

result = ssh.communicate()[0]
if result == []:
		error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
else:
	print result
'*************************************************************************'
f= ope(NEW_PATH5, "w")
ssh = subprocess.Popen(["ssh", "%s" % HOST5, COMMAND],
			stdout=f,
			stderr= subprocess.PIPE)

result = ssh.communicate()[0]
if result == []:
		error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
else:
	print result
'*************************************************************************'
f= ope(NEW_PATH6, "w")
ssh = subprocess.Popen(["ssh", "%s" % HOST7, COMMAND],
			stdout=f,
			stderr= subprocess.PIPE)

result = ssh.communicate()[0]
if result == []:
		error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
else:
	print result
'*************************************************************************'
f= ope(NEW_PATH7, "w")
ssh = subprocess.Popen(["ssh", "%s" % HOST7, COMMAND],
			stdout=f,
			stderr= subprocess.PIPE)

result = ssh.communicate()[0]
if result == []:
		error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
else:
	print result
'*************************************************************************'

