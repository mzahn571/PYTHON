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
		test2 = re.findall(r'(100)\D', output)
		if '100' in test2:
			print 'the vlan exist'
		else:
			print ' the vlan does not exist'
    

if __name__ == "__main__":
    print ("You ran this module directly (and did not 'import' it)")
