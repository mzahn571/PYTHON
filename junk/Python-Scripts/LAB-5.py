import paramiko
import telnetlib
import sys
import time


enable = "enable"
conf = "configure terminal"
shrun = "show run"
termlength = "terminal length 0"
username = "cisco"
password = "cisco" 

filelist = open("/home/student/Desktop/PYTHON/TEST/FILES.txt")

class Session(object):  
	def Getrun(self, ip):
		self.ip = ip
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(self.ip, username=username, password=password, look_for_keys= False, allow_agent= False)
		print "SSH connection established to %s" % self.ip
		remote_conn = remote_conn_pre.invoke_shell()
		remote_conn.send(termlength + "\r")
		time.sleep (1)
		output = remote_conn.recv(1000)
		remote_conn.send("\r")
		remote_conn.send(enable + "\r")
		remote_conn.send(password + "\r")
		remote_conn.send(shrun + "\r")
		time.sleep(5)
		output = remote_conn.recv(65534)
		file = output
		remote_conn.close()
		return file
		
		
	def Postrun(self, files, file):
		HOME = "/home/student/Desktop/PYTHON/TEST/Routers/%s" %(files)
		f = open(HOME.strip(), "w")
		f.write(str(file))
		f.close()

ips = {1:"10.10.10.1", 2:"10.10.10.2", 3:"10.10.10.3", 4:"10.10.10.4"}
                
ssh = Session()
file1 = ssh.Getrun(ips[1])
file2 = ssh.Getrun(ips[2])
file3 = ssh.Getrun(ips[3])
file4 = ssh.Getrun(ips[4])
runfiles = [file1,file2,file3,file4]
for i,j in zip(filelist, runfiles):
        ssh.Postrun(i,j)
sys.exit("operation completed")
