import telnetlib
import sys
import time
import psutil
import re

ssh = "ip ssh version 2"
domain = "ip domain-name cisco"
conf = "configure terminal"
crypto_keys = "crypto key generate rsa"
key = "1024"
end = "end"
exit = "exit"
username = "cisco"
password = "cisco"
enable = "enable"

def SSH(ip):
	try:
		tn = telnetlib.Telnet(ip, timeout= 10 )
		time.sleep (1)
		tn.write(username + "\r")
		tn.write(password + "\r")
		tn.write(enable + "\r")
		tn.write(password + "\r")
		tn.write(conf + "\r")
		tn.write(ssh + "\r")
		tn.write(domain + "\r")
		tn.write(crypto_keys + "\r")
		tn.write(key + "\r")
		time.sleep(1)
		tn.close()
		return tn
	except IOError:
		return None

def SSH_Verify(ip):
	try:
		tn = telnetlib.Telnet(ip, timeout= 3 )
		time.sleep (1)
		tn.write(username + "\r")
		tn.write(password + "\r")
		tn.write(enable + "\r")
		tn.write(password + "\r")
		time.sleep(1)
		tn.write('show ip ssh' + "\r")
		time.sleep(1)
		test2 = tn.read_until('Authentication')
		w = re.search(r'(SSH\sEnabled).*', test2)
		return w
	except IOError:
		return None
				
ips = ["10.10.10.1", "10.10.10.2","10.10.10.3", "10.10.10.4", "10.10.10.5"]

CPU = float(30)
x = 0
while x == 0:
	time.sleep(3)
	if psutil.cpu_percent() <= CPU:
		x = x +1
		print "Routers Booted\n"
		print "Configuring SSH for existing routers....."
		for ip in ips:
			session = SSH(ip)
			if session:
				session_new = SSH_Verify(ip)
				if session_new:
					print "ssh successful for %s" % ip
				else:
					print "ssh was unsuccesful for %s" % ip
			else:
				print "SSH has been completed for ALL routers\n"
				print "Please press 'keys icon' if any ssh did not complete successfully"
				time.sleep (4)
				break	
sys.exit('Have a Nice Day')
