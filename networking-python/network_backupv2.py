#!/usr/local/bin/python
from datetime import datetime

import subprocess
import sys
import re

IPSEC01="ipsec01"
IPSEC02="ipsec02"
IPSEC03="ipsec03"
IPSEC04="ipsec04"
IPSEC05="ipsec05"
IPSEC06="ipsec06"
IPSEC07="ipsec07"
IPSEC08="ipsec08"

FW01="fw01"

#SW01="sw01"
SW02="sw02"
SW05="sw05"
SW06="sw06"

FW01="fw01"

FORMAT = "%m%d%Y-%H:%M UTC"
#Nework devices IPSEC's and Firewalls Low side
PATH1 = "/data/1_Network_Config_Backups/IPSEC01/ipsec01_config"
PATH2 = "/data/1_Network_Config_Backups/IPSEC02/ipsec02_config"
PATH3 = "/data/1_Network_Config_Backups/IPSEC03/ipsec03_config"
PATH4 = "/data/1_Network_Config_Backups/IPSEC04/ipsec04_config"
PATH5 = "/data/1_Network_Config_Backups/IPSEC05/ipsec05_config"
PATH6 = "/data/1_Network_Config_Backups/IPSEC06/ipsec06_config"
PATH7 = "/data/1_Network_Config_Backups/IPSEC07/ipsec07_config"
PATH8 = "/data/1_Network_Config_Backups/IPSEC08/ipsec08_config"

PATH9 = "/data/1_Network_Config_Backups/FW01/fw01_config"

#Network Switches low side
#PATH10 = "/data/1_Network_Config_Backups/SW01/sw01_config"
PATH11 = "/data/1_Network_Config_Backups/SW02/sw02_config"
PATH12 = "/data/1_Network_Config_Backups/SW05/sw05_config"

#Nework devices IPSEC's and Firewalls Low side manipulation file name to place date and time
NEW_PATH1 = '%s_%s' % (PATH1,datetime.now().strftime(FORMAT))
NEW_PATH2 = '%s_%s' % (PATH2,datetime.now().strftime(FORMAT))
NEW_PATH3 = '%s_%s' % (PATH3,datetime.now().strftime(FORMAT))
NEW_PATH4 = '%s_%s' % (PATH4,datetime.now().strftime(FORMAT))
NEW_PATH5 = '%s_%s' % (PATH5,datetime.now().strftime(FORMAT))
NEW_PATH6 = '%s_%s' % (PATH6,datetime.now().strftime(FORMAT))
NEW_PATH7 = '%s_%s' % (PATH7,datetime.now().strftime(FORMAT))
NEW_PATH8 = '%s_%s' % (PATH8,datetime.now().strftime(FORMAT))

NEW_PATH9 = '%s_%s' % (PATH9,datetime.now().strftime(FORMAT))
#Nework devices Switches Low side manipulation file name to place date and time
#NEW_PATH10 = '%s_%s' % (PATH10,datetime.now().strftime(FORMAT))
NEW_PATH11 = '%s_%s' % (PATH11,datetime.now().strftime(FORMAT))
NEW_PATH12 = '%s_%s' % (PATH12,datetime.now().strftime(FORMAT))

COMMAND1="show configuration | display set | no-more"

def bk_operation(NEW_PATH, HOST, COMMAND):
    """"Define Operations to backup the configuration files"""
	f = open(NEW_PATH, "w")
	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	    stdout=f,
		stderr= subprocess.PIPE)
	
	result = ssh.communicate()[0]
	
	if result == []:
	    error = ssh.stderr()
		print >>sys.stderr, "ERROR: %s" % error
	else:
	    print(HOST, "backup completed")
		return result
		

		
#Juniper Devices
bk_operation(NEW_PATH1, IPSEC01, COMMAND1)
bk_operation(NEW_PATH3, IPSEC03, COMMAND1)
bk_operation(NEW_PATH5, IPSEC05, COMMAND1)
bk_operation(NEW_PATH6, IPSEC06, COMMAND1)
bk_operation(NEW_PATH7, IPSEC07, COMMAND1)

#Cisco devices

''' Router configuration
In configuration mode

	# file privelege 3
	# username syscheck privelege 3
	# 
	#
	# configuring ip ssh pubkey-chain
	# R1(conf-ssh-pubkey)# username syscheck
	# R1(conf-ssh-pubkey-user)# key-string
	# R1(conf-ssh-pubkey-data)# key-hash ssh-rsa key-hash --- In most cases you will need to break up the key-hash
	# R1(config-ssh-pubkey-data)# endswith