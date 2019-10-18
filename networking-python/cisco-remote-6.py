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

filelist = open("/home/student/Desktop/PYTHON/Python-Scripts/MPLS3.txt")

class Session(object): 

	def SSHConnect(self, ip):
		self.ip = ip
		try:
			ssh_prep = paramiko.SSHClient()
			ssh_prep.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_prep.connect(self.ip, username=username, password=password, look_for_keys= False, allow_agent= False)
			conn = ssh_prep.invoke_shell()
			print "SSH connection established to %s" % self.ip
			conn.send(termlength + "\r")
			time.sleep (1)
			output = conn.recv(1000)
			conn.send(enable + "\r")
			conn.send(password + "\r")
			conn.send(shrun + "\r")
			time.sleep(5)
			output = conn.recv(65534)
		except IOError:
			print "Cannot connect"
		else:
			return output
		
	def Postrun(self, files, file):
		HOME = "/home/student/Desktop/PYTHON/TEST/Routers-2/%s" %(files)
		f = open(HOME.strip(), "w")
		f.write(str(file))
		f.close()
   
  
ssh = Session()
runfiles = []
y = 1
while y != 5:
    if y < 5:
		print "\nGetting Running Config for R%s" % y
		file = ssh.SSHConnect("10.10.10.%s" % y)
		y += 1
		runfiles.append(file)
    else:  
        print "\nGetting Running Config for R%s" % y
        runfiles.append(file)
        y += 1
for i,j in zip(filelist, runfiles):
        ssh.Postrun(i,j)
sys.exit("operation completed") 
  
  
  
ssh = Session()
y = 1 
runfiles = []
for router in filelist:
	
	print "Getting running Config from  %s" % router
	file = ssh.SSHConnect(str("10.10.10.%d") % y)
	if file:
		print "Adding R%s to the list" % y
	y += 1
	runfiles.append(file)

for i,j in zip(filelist, runfiles):
	print "There is a file"
#	ssh.Postrun(i,j)

sys.exit("operation completed")
	
