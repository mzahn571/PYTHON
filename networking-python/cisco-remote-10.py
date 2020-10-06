#import the neccessary modules

import time
import sys
import getpass
import paramiko

#setup the variables used in the script 
 
ip = '10.10.10.1'
username = "cisco"
password = getpass.getpass()

#Execute the main part of the code
  
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password)
print "SSH connection established to 10.10.10.1"
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"
output = remote_conn.recv(1000)
print output
remote_conn.send("terminal length 0\n")
remote_conn.send("enable\r")
remote_conn.send("cisco\r")
remote_conn.send("conf t\r")
time.sleep(2)
remote_conn.send("hostname R1\r")
remote_conn.send("end\r")
remote_conn.send("disable\r")
remote_conn.close()

sys.exit("ALL Done!")
