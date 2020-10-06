import requests
from bs4 import BeautifulSoup

dash = '~' * 50
hostname = 'localhost'
url = "http://%s:5000/xml/books"% hostname
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
for i in soup.find_all('book'):
	author = (i.author.text).strip()
	title = (i.title.text).strip()
	date = (i.publish_date.text).strip()
	genre = (i.genre.text).strip()
	print 'Book Author: %s'% author
	print 'Book Title: %s'% title
	print 'Publish Date: %s'% date
	print 'Book Genre: %s'% genre
	print dash