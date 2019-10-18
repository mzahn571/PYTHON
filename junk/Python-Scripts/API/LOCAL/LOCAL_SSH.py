import paramiko
import sys
import time


enable = "enable"
disable = 'disable'
conf = "configure terminal"
shrun = "show run"
termlength = "terminal length 0"
username = "cisco"
password = "cisco"

class Session(object): 

	def SSHConnect(self, ip):
		self.ip = ip
		try:
			ssh_prep = paramiko.SSHClient()
			ssh_prep.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_prep.connect(self.ip, username=username, password=password, look_for_keys= False, allow_agent= False)
		except IOError:
			print "Cannot connect"
		else:
			return ssh_prep
			
if __name__== '__main__':
	print "This file has been executed locally"
	a = Session()
	b = a.SSHConnect('10.10.10.1')
	c = b.invoke_shell()
	d = c.recv(1000)
	print d
	
