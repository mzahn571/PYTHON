import paramiko
import sys
import time
import re

ipaddr ='10.10.10.2'
username = "cisco"
password = "cisco"
enable = "enable"
conf = "configure terminal"
host = "hostname R2"
end = "end"
exit = "exit"

def GET_SERIAL():
    print "Interactive SSH session established"
    remote_conn.send("terminal length 0\n")
    remote_conn.send("enable\r")
    remote_conn.send("cisco\r")
    remote_conn.recv(1000)
    remote_conn.send("show inventory" + "\r")
    time.sleep(2)
    output = remote_conn.recv(2000)
    test = re.search(r'SN:(\s[0-9]*)', output)
    print test.group(1)
    #print output
    #time.sleep(2)


#def COMMONEND():
#    remote_conn.send("end\r")
#    remote_conn.send("disable\r")
#    remote_conn.close()

router = "10.10.10.1"
routers= ["10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4"]
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(router, username=username, password=password, look_for_keys= False, allow_agent= False)
remote_conn = remote_conn_pre.invoke_shell()
print "SSH connection established to %s" %  router
GET_SERIAL()
#remote_conn.send("hostname R2\r")
#COMMONEND()
sys.exit("operation completed")
