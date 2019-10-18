import paramiko
import sys
import time
import re

ipaddr ='10.10.10.2'
username = "cisco"
password = "cisco"
enable = "enable"
conf = "configure terminal"
host = "hostname R2"
end = "end"
exit = "exit"

def GET_SERIAL():
    print "Attempting to get the Serial Number of the Appliance!"
    remote_conn.send("terminal length 0\n")
    remote_conn.send("enable\r")
    remote_conn.send("cisco\r")
    remote_conn.recv(1000)
    remote_conn.send("show inventory" + "\r")
    time.sleep(2)
    output = remote_conn.recv(2000)
    test = re.findall(r'SN:\s([0-9]*)', output)
    print "The Serial Number of the Appliance is %s: " % test
    
    
    
def GET_CONFIG_R():
	print "Attempting to get the Config Register of the Appliance!"
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("show version" + "\r")
	time.sleep(2)
	output = remote_conn.recv(4000)
	test = re.search(r'\nConfiguration.*(\d\D\d+)', output)
	print "\nThe Config Register is set to:\t%s\n" % test.group(1)

def LOG():
	print "Acquiring Logging Info!"
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("show log" + "\r")
	time.sleep(4)
	output = remote_conn.recv(10000)
	test = re.findall(r'.*IPACCESSLOGDP.*', output)
	if test:
		print "\nThere is/are %d deny entries on the access-list PYTHON" % len(test)
	if len(test) > 0:
		test3 = raw_input("\nWould you like to view these errors? (y/n) ")
		if test3 == "y":
			for entry in test:
				print entry

	
router1 = '10.10.10.1'
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(router1, username=username, password=password, look_for_keys= False, allow_agent= False)
remote_conn = remote_conn_pre.invoke_shell()
print "SSH connection established to %s" %  router1
GET_SERIAL()
GET_CONFIG_R()
LOG()

sys.exit("operation completed")
