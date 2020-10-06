import requests
from bs4 import BeautifulSoup

dash = '~' * 50
hostname = 'localhost'
url = "http://%s:5000/xml/recipe"% hostname
username = 'student'
password = 'student'

# Making RESTful call via python to flask
get_data = requests.get(url, auth=(username, password))

data = get_data.text
soup = BeautifulSoup(data, 'lxml')
print soup.prettify()
for i in soup.find_all('ingredient'):
	item_name = (i.item.text).strip()
	item_qty = (i.qty.text).strip()
	print 'Item Name: %s'% item_name
	if item_qty == '':
		print 'Item Quantity: N/A'
	else:
		print 'Item Quantity: %s'% item_qty