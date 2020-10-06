import paramiko
import telnetlib
import sys
import time
import getpass



ip1 = "10.10.10.1"
ip2 = "10.10.10.2"
ip3 = "10.10.10.3"
ip4 = "10.10.10.4"

ip_list = [ip1,ip2,ip3,ip4]

tn1 = ""
enable = "enable"
conf = "configure terminal"
end = "end"
exit = "exit"
termlength = "terminal length 0"
password = getpass.getpass()
username = "cisco"


###  telnet to a session and configure the hostname- end and exit the session  ###
def Session1(session, name, ipaddr):
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr, username=username, password=password, look_for_keys= False, allow_agent= False)
	print "SSH connection established to %s" % ipaddr
	remote_conn = remote_conn_pre.invoke_shell()
	print "Interactive SSH session established"
	output = remote_conn.recv(1000)
	print output
	remote_conn.send(termlength + "\r")
	remote_conn.send(enable + "\r")
	remote_conn.send(password + "\r")
	remote_conn.send(conf + "\r")
	time.sleep(2)	
	remote_conn.send(name + "\r")
	remote_conn.send(end + "\r")
	remote_conn.send("disable\r")
	remote_conn.close()
    


### login to sessions and pass on different variables###
Session1(tn1 , 'hostname R1', ip_list[0])
Session1(tn1 , 'hostname R2', ip_list[1])
Session1(tn1 , 'hostname R3', ip_list[2])
Session1(tn1 , 'hostname R4', ip_list[3])

sys.exit("operation completed")


