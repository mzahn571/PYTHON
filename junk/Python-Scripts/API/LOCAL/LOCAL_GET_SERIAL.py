import sys
import time
import re

shinv = 'show inventory'

class Serial(object): 

	def GetSerial(self, remote_conn):
		remote_conn.send("\r")
		remote_conn.send('end\r')
		remote_conn.send(shinv + "\r")
		time.sleep(5)
		output = remote_conn.recv(65534)
		text = re.search(r'NAME:\s\D([a-zA-Z]*).*\n.*(SN:\s[0-9]*)', output)
		return text.groups()
			
if __name__== '__main__':
	print "This file has been executed locally"
