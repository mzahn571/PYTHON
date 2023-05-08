import paramiko
import sys
import time

enable = "enable"
username = 'cisco'
password = 'cisco'

R2Lo0 = "2.2.2.2"
R3Lo0 = "3.3.3.3"
R4Lo0 = "4.4.4.4"
R1 = "R1"
R2 = "R2"
R3 = "R3"
R4 = "R4"

loopbacks = {R2:R2Lo0, R3:R3Lo0, R4:R4Lo0}

Router2 = loopbacks[R2]
Router3 = loopbacks[R3]
Router4 = loopbacks[R4]

routers = [Router2, Router3, Router4]

def Ping(router):
	ip = "10.10.10.1"
	ssh_prep = paramiko.SSHClient()
	ssh_prep.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_prep.connect(ip, username=username, password=password, look_for_keys= False, allow_agent= False)
	conn = ssh_prep.invoke_shell()
	conn.send(enable + "\r")
	conn.send(password + "\r")
	print "pinging router %s" % router
	conn.send("ping "+ router + "\r")
	time.sleep(5)
	output = conn.recv(65534)

for router in routers:
    tst = Ping(router)
sys.exit("operation completed")
