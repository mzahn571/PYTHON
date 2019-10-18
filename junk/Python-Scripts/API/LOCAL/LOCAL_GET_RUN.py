import sys
import time

enable = 'enable'
password = 'cisco'
shrun = 'show run'
termlength = 'terminal length 0'

class Running_Config(object): 

	def GetRun(self, remote_conn):
		remote_conn.send("end\r")
		remote_conn.send(shrun + "\r")
		time.sleep(5)
		output = remote_conn.recv(65534)
		return output
			
if __name__== '__main__':
	print "This 'LOCAL_GET_RUN' file has been executed locally"
