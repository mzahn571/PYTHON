import requests
from bs4 import BeautifulSoup

dash = '~' * 50
hostname = 'localhost'
url = "http://%s:5000/xml/patents"% hostname
username = 'student'
password = 'student'

# Making RESTful call via python
get_data = requests.get(url, auth=(username, password))

# Get Data from endpoint and prepare for parsing
data = get_data.text
soup = BeautifulSoup(data, 'lxml')
# Check pre-parsed data
#print soup.prettify()
# Iterate XML data and print
for i in soup.find_all('patent-assignment'):
	for c in i.find_all('correspondent'):
		for n in c.find_all('name'):
			print type(n)
	for a in i.find_all('patent-assignee'):
		patent_company = (a.name.string).strip()
	#dest_zone = (i.patent-assignee.string).strip()
	#dest_cidr = (i.destination.member.string).strip()
	print 'Patent Correspondent: %s'% patent_corr
	print 'Patent Assignee: %s'% patent_company
	#print 'Source Subnet: %s'% source_cidr
	#print 'Destination Zone: %s'% dest_zone
	print dash