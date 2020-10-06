import paramiko
import sys
import time

ipaddr ='10.10.10.2'
username = "cisco"
password = "cisco"
enable = "enable"
conf = "configure terminal"
host = "hostname R2"
end = "end"
exit = "exit"

def COMMONBEGIN():
    print "Interactive SSH session established"
    #output = remote_conn.recv(1000)
    #print output
    remote_conn.send("terminal length 0\n")
    remote_conn.send("enable\r")
    remote_conn.send("cisco\r")
    remote_conn.send("conf t\r")
    output = remote_conn.recv(2000)
    print output
    time.sleep(2)


def COMMONEND():
    remote_conn.send("end\r")
    remote_conn.send("disable\r")
    remote_conn.close()

remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ipaddr, username=username, password=password, look_for_keys= False, allow_agent= False)
remote_conn = remote_conn_pre.invoke_shell()
print "SSH connection established to 10.10.10.2"
COMMONBEGIN()
remote_conn.send("hostname R2\r")
COMMONEND()
sys.exit("operation completed")
