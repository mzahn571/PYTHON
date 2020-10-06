import paramiko
import sys
import time
import re
from MENTOR_VLAN import Session

termlength = "terminal length 0"
enable = "enable"
conf = "configure terminal"
username = "cisco"
password = "cisco"

ipaddr = "10.10.10.1"
HOSTB_IP = "192.168.100.2"
HOSTB = "HOSTB"

loopbacks = {HOSTB:HOSTB_IP}

HOST_B = loopbacks[HOSTB]

routers = [HOST_B]

def Ping(router, ip):
	print "Checking Connectivity....."
	ssh_prep = paramiko.SSHClient()
	ssh_prep.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_prep.connect(ip, username=username, password=password, look_for_keys= False, allow_agent= False)
	conn = ssh_prep.invoke_shell()
	print "SSH connection established to %s" % ip
	conn.send(termlength + "\r")
	time.sleep (1)
	output = conn.recv(1000)
	conn.send(enable + "\r")
	conn.send(password + "\r")
	conn.send("ping "+ router + "\r")
	time.sleep(5)
	output = conn.recv(65534)
	test2 = re.findall(r'!!!', output)
	conn.close()
	if '!!!' in test2:
		print 'Reachabilty to Router is Good!'
		value = 'ONE'
	else:
		print 'No Reachabilty to Node'
		value = 'TWO'
	return value



test = Session()
for router in routers:
    tst = Ping(router, ipaddr)
    if tst == 'ONE':
        print "Everthing Appears to be Tip Top!!!"
    if tst == 'TWO':
		ips = ["10.10.10.3", "10.10.10.4", "10.10.10.5"]
		print 'Checking Vlans...\n'
		PAUL = Session()
		for ip in ips:
			TEXT = PAUL.Get_SSH(ip)
        
sys.exit("operation completed")
