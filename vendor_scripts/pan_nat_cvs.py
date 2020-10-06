import ssl
import sys
import urllib
import urllib2
import getpass
import re
import xlsxwriter
from bs4 import BeautifulSoup

# Function Logging into Palo Alto Networks Device, producing a key and using the key to pull configs
def pan_cmd():

 # SSL for Palo Alto Login
 ctx = ssl
 check_hostname = False
 verify_mode = ssl.CERT_NONE

 # Variables for Palo Alto Login
 pa_ip = "100.100.2.17"
 username = "student"
 password = getpass.getpass(prompt='Please enter your password: ')
 login_url = 'https://'+pa_ip+'/api/?type=keygen&user='+username+'&password='+password

 # Request authorization key for future inquiries
 login_response = urllib2.urlopen(login_url)
 pa_key = ""

 # Iterate XML for Palo Alto Login
 login_soup = BeautifulSoup(login_response, 'xml')
 print "XML Output before Iteration for Auth Key Request:"
 print(login_soup.prettify())
 print "- Iterating XML for Auth Key"
 for tag in login_soup.find_all('response'):
	pa_key = (tag.key.string)


 # GET Request URL Construction for Pulling NAT Rules
 cmd = "/api/?type=config&action=get&"
 nat_parameters = {'xpath':"/config/devices/entry[@name=\'localhost.localdomain\']/vsys/entry[@name=\'vsys1\']/rulebase/nat/rules"}
 # Alternative Endpoints
 # service_parameters = {'xpath':"/config/devices/entry[@name=\'localhost.localdomain\']/vsys/entry[@name=\'vsys1\']/service"}
 # parameters = {'xpath':"/config/devices/entry[@name=\'localhost.localdomain\']"}
 url = "https://"+pa_ip+cmd+"Key="+pa_key+"&"+urllib.urlencode(nat_parameters)

 count = 0

 # Create a workbook and add a worksheet.
 workbook = xlsxwriter.Workbook('nat.xlsx')
 worksheet = workbook.add_worksheet()
 worksheet.set_column(0, 3, 24)

 # Start from the first cell. Rows and columns are zero indexed.
 row = 0
 col = 0

 # Grab all the relevant objects from each NAT Rule
 cmd_response = urllib2.urlopen(url)
 cmd_soup = BeautifulSoup(cmd_response, 'xml')
 print "XML Output of NAT Rule GET Request:"
 print(cmd_soup.prettify())
 print "- Iterating NAT Rule GET Request for Relevent Objects"
 for tag in cmd_soup.find_all('entry'):
 	nat_name = None
 	pre_nat = None
 	post_nat = None
 	ticket_no = None
 	pre_nat = (tag.destination.member.string)
 	if pre_nat != 'any':
 		if not (tag.description):
 			continue
 		nat_name = tag['name']
 		ticket_no = (tag.description.string)
 		for tag1 in cmd_soup.find_all('translated-address'):
 			if not (tag1.string):
 				continue
 			else:
 				try:
 					for post_nat in getattr(tag, 'destination-translation')('translated-address')[0]:
 						if post_nat is TypeError:
 							continue
 						if post_nat is None:
 							continue
 				except Exception:
 					pass
 	else:
 		continue
 	if pre_nat is '' and post_nat is '':
 		continue
 	if pre_nat is None and post_nat is None:
 		continue
 	if post_nat is None:
 		continue

 	# Iterate over the data and write it out row by row.
 	print "- Adding Objects to 'nat.cvs' Worksheet for rule %s"% nat_name
	worksheet.write(col + count, row, nat_name)
 	worksheet.write(col + count, row + 1, pre_nat)
 	worksheet.write(col + count, row + 2, post_nat)
 	worksheet.write(col + count, row + 3, ticket_no)

 	count = count + 1

	# Print all NAT Rule Values
 	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	print 'Rule Name: '+nat_name
 	print 'Pre-NAT Address: '+pre_nat
 	print 'Post-NAT Address: '+post_nat
 	print 'Tickets: '+ticket_no

 print "Operation Completed!"
 workbook.close()

pan_cmd()