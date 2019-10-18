import requests
from bs4 import BeautifulSoup

hostname = 'localhost'
url = "http://%s:5000/xml/contacts"% hostname
username = 'student'
password = 'student'
dash = '~' * 110
top = '_' * 110

# Making RESTful call via python
get_data = requests.get(url, auth=(username, password))

# Get Data from endpoint and prepare for parsing
print top
print('{:<2s}{:>15s}{:>20s}{:>15s}{:>25s}{:>25s}'.format('Id', 'First Name', 'Last Name', 'Gender', 'Email', 'IP Address'))
print dash
data = get_data.text
soup = BeautifulSoup(data, 'lxml')
# Check pre-parsed data
#print soup.prettify()
# Iterate XML data and print
for i in soup.find_all('record'):
	contact_id = (i.id.text).strip()
	first_name = (i.first_name.text).strip()
	last_name = (i.last_name.text).strip()
	gender = (i.gender.text).strip()
	email = (i.email.text).strip()
	ip_addr = (i.ip_address.text).strip()
	print('{:<2s}{:>15s}{:>20s}{:>15s}{:>32s}{:>20s}'.format(contact_id, first_name, last_name, gender, email, ip_addr))
	print dash
