import requests
from bs4 import BeautifulSoup

dash = '~' * 75
top = '_' * 75
hostname = 'localhost'
url = "http://%s:5000/xml/pan/nat/rules"% hostname
username = 'student'
password = 'student'

# Making RESTful call via python
get_data = requests.get(url, auth=(username, password))

# Get Data from endpoint and prepare for parsing
print top
print('{:<35s}{:>20s}{:>20s}'.format('Rule Name', 'Destination', 'Dest Translation'))
print dash
data = get_data.text
soup = BeautifulSoup(data, 'lxml')
dest_translation = ''
# Check pre-parsed data
# print soup.prettify()
# Iterate XML data and print
for i in soup.find_all('entry'):
	for d in i.find_all('destination-translation'):
		for a in d.find_all('translated-address'):
			dest_translation = (a.string).strip()
	rule_name = i['name'].strip()
	dest = (i.destination.member.string).strip()
	print('{:<35s}{:>20s}{:>20s}'.format(rule_name, dest, dest_translation ))
	print dash