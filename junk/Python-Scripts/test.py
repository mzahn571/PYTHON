import paramiko
import telnetlib
import sys
import time
import re

ip = "10.10.10.1"
enable = "enable"
conf = "configure terminal"
shrun = " show run"
termlenght = "terminal length 0"
username = "cisco"
password = "cisco"
plname = raw_input("What is the prefix-list name? : ")
sh_ip_pre = "sh run | i prefix-list %s" % (plname)

class REPLACE()

	def GET_PREFIXLIST(self, ipaddr):
		self.ipaddr = ipaddr
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(ipaddr, username=username, password=password, look_for_keys= False, allow_agent= False)
		print "SSH connection established to %s" % ipaddr
		remote_conn = remote_conn_pre.invoke_shell()
		remote_conn.send(termlength + "\r")
		time.sleep(1)
		remote_conn.send("\r")
		remote_conn.send(enable + "\r")
		remote_conn.send(password + "\r")
		remote_conn.send(sh_ip_pre + "\r")
		time.sleep(4)
		output = remote_conn.recv(65534)
		return output

	def POST(self, seq):
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(self.ipaddr, username=username, password=password, look_for_keys= False, allow_agent= False)
		print "SSH connection established to %s" % self.ipaddr
		remote_conn = remote_conn_pre.invoke_shell()
		remote_conn.send(termlength + "\r")
		time.sleep(1)
		remote_conn.send("\r")
		remote_conn.send(enable + "\r")
		remote_conn.send(password + "\r")
		remote_conn.send(conf + "\r")
		time.sleep(2)
		remote_conn.send('ip prefix-list %r seq %d permit 33.33.33.33/32' % (plname, seq) + '\r')
		remote_conn.send('exit\r')
		time.sleep(2)
		remote_conn.send('clear ip bgp * in\r')
		time.sleep(2)

x = REPLACE()
y = x.GET_PREFIXLIST(ip)
z = re.findall(r'(%s)'% plname, y)
z.pop(0)
if plname in z:
	print "It is there"
else:
	print "It is not there"
	sys.exit()
text1 = refindall(r'(ip prefix-list\s[A-Z]*_.*)\r', y)
text1.pop()
PL_STATE = text1[-1]
text3 = re.match(r'.*seq (\d+)', PL_STATE)
new_seq = int(text3.group(1) + 5)
x.POST(new_seq)

