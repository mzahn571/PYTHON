import sys
from bs4 import BeautifulSoup as Soup
import requests

base_url = 'http://192.168.104.134:5000/api/object/xml'

# create credentials structure

tenant_url = base_url
xml_data = requests.get(tenant_url)
XML = xml_data.content
soup = Soup(XML, 'xml')
print soup.prettify()
print "\n"
ip = soup.ip.entry

print ip['name']
