import requests
from bs4 import BeautifulSoup

hostname = 'localhost'
url = 'http://%s:5000/xml/juniper/get-system-information'% hostname
username = 'student'
password = 'student'

get_data = requests.get(url, auth=(username, password))
data  = get_data.text
soup = BeautifulSoup(data, 'lxml')

for i in soup.find('host-name'):
	hostname = i.string.strip()
for i in soup.find('os-version'):
	firmware = i.string.strip()
for i in soup.find('serial-number'):
	serial = i.string.strip()

print 'Hostname: %s'% hostname
print 'OS Version: %s'% firmware
print 'Serial Number: %s'% serial
