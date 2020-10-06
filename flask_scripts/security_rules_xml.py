import requests
from bs4 import BeautifulSoup

dash = '~' * 110
top = '_' * 110
hostname = 'localhost'
url = "http://%s:5000/xml/pan/nat/rules"% hostname
username = 'student'
password = 'student'

# Making RESTful call via python
get_data = requests.get(url, auth=(username, password))

# Get Data from endpoint and prepare for parsing
print top
print('{:<30s}{:>15s}{:>20s}{:>22s}{:>19s}'.format('Rule Name', 'Source Zone', 'Source Subnet', 'Dest Zone', 'Dest'))
print dash
data = get_data.text
soup = BeautifulSoup(data, 'lxml')
# Check pre-parsed data
# print soup.prettify()
# Iterate XML data and print
for i in soup.find_all('entry'):
	for source in i.find_all('from'):
		source_zone = (source.member.string).strip()
	rule_name = i['name'].strip()
	source_cidr = (i.source.member.string).strip()
	dest_zone = (i.to.member.string).strip()
	dest_cidr = (i.destination.member.string).strip()
	print('{:<30s}{:>15s}{:>20s}{:>20s}{:>20s}'.format(rule_name, source_zone, source_cidr, dest_zone,dest_cidr ))
	print dash