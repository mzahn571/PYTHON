import paramiko
import telnetlib
import sys
import time

username = "cisco"
password = "cisco"
ipaddr1 ='10.10.10.1'
ipaddr2 ='10.10.10.2'
ipaddr3 ='10.10.10.3'
ipaddr4 ='10.10.10.4'
enable = "enable"
conf = "configure terminal"
end = "end"
exit = "exit"

def Session1():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr1, username=username, password=password, look_for_keys= False, allow_agent= False)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)	
	remote_conn.send("hostname R1\r")
	remote_conn.send("end\r")
	remote_conn.send("disable\r")
	remote_conn.close()

def Session2():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr2, username=username, password=password)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)
	remote_conn.send("hostname R2\r")
	remote_conn.send("end\r")
	remote_conn.send("disable\r")
	remote_conn.close()

def Session3():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr3, username=username, password=password)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)
	remote_conn.send("hostname R3\r")
	remote_conn.send("end\r")
	remote_conn.send("disable\r")
	remote_conn.close()

def Session4():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr4, username=username, password=password)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)
	remote_conn.send("hostname R4\r")
	remote_conn.send("end\r")
	remote_conn.send("disable\r")
	remote_conn.close()


Session1()
print "Connecting to TEST1"
Session2()
print "Connecting to TEST2"
Session3()
print "Connecting to TEST3"
Session4()
print "Connecting to TEST4"

sys.exit("operation completed")

