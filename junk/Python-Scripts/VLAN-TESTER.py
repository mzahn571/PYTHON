import paramiko
import sys
import time
import re


enable = "enable"
conf = "configure terminal"
show_vlan = 'show vlan-switch'
terminal_length = "terminal length 0"
username = "cisco"
password = "cisco"


class Session(object): 
    
	def Get_SSH(self, ip):
		session = paramiko.SSHClient()
		session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		session.connect(ip, username=username, password=password, look_for_keys= False, allow_agent= False)
		conn = session.invoke_shell()
		conn.send(enable + "\r")
		conn.send(password + "\r")
		conn.send(terminal_length + "\r")
		output = conn.recv(65534)
		conn.send(show_vlan + "\r")
		time.sleep(2)
		output = conn.recv(65534)
		#print output
		if session:
			print 'We are connected to port %s' % ip
		else:
			print 'We cannot connect to port %s' % ip
		return output
    
 
ips = ["10.10.10.3", "10.10.10.4", "10.10.10.5"]


ssh = Session()
for ip in ips:
	session = ssh.Get_SSH(ip)
	test2 = re.search(r'\n(100)\s', session)
	print test2.group(1)
	if '100' in test2.group(1):
		print 'the vlan exist'
	else:
		print ' the vlan does not exist'
sys.exit("operation completed")
    
