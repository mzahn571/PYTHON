import requests
import psycopg2
import json
import sys
from bs4 import BeautifulSoup

# Define variable for RESTful Call
hostname = 'localhost'
json_url = "http://%s:5000/json/contacts"% hostname
xml_url = "http://%s:5000/xml/contacts"% hostname
username = 'student'
password = 'student'
db_name = 'student'
url_list = [json_url, xml_url]
curs = ''
conn = ''

def TableCreate(url, db_name):
	global conn
	global curs
	if 'json' in url:
		table = 'json_contacts'
	elif 'xml' in url:
		table = 'xml_contacts'
	else:
		print 'Data Type does not exist.'
		sys.exit()
	#Accessing DB and creating table for data insertion
        print '- Accessing and creating/flushing database table %s'% table
        conn = psycopg2.connect(database = db_name)
        curs = conn.cursor()
        try:
		curs.execute("CREATE TABLE %s (id text, first text, last text, gender text, email text, ip text)"% table)
        except:
		conn.rollback()
		curs.execute("DROP TABLE %s"% table)
		curs.execute("CREATE TABLE %s (id text, first text, last text, gender text, email text, ip text)"% table)

def RestToDB(url, db_name, conn, curs):
	print '- Making RESTful Call to Endpoint'
	get_data = requests.get(url, auth=(username, password))
	if 'json' in url:
		table = 'json_contacts'
		# Making RESTful call via python to attain JSON data
		data = get_data.content
		json_output = json.loads(data)
		# Iterate Routes for important information
		print '- Iterating JSON Data and inserting into database'
		for contact in json_output['items']:
			contact_id = str(contact['id'])
			first_name = contact['first_name']
			last_name = contact['last_name']
			gender = contact['gender']
			email = contact['email']
			ip_addr = contact['ip_address']
			curs.execute("INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (table, contact_id, first_name, last_name, gender, email, ip_addr))
	elif 'xml' in url:
		table = 'xml_contacts'
		data = get_data.text
		soup = BeautifulSoup(data, 'lxml')
		print '- Iterating XML Data and inserting into database'
		for i in soup.find_all('record'):
			for c in i.find_all('id'):
				contact_id = (c.text).strip()
			first_name = (i.first_name.text).strip()
			last_name = (i.last_name.text).strip()
			gender = (i.gender.text).strip()
			email = (i.email.text).strip()
			ip_addr = (i.ip_address.text).strip()
	        	curs.execute("INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (table, contact_id, first_name, last_name, gender, email, ip_addr))
	else:
		print 'No data exists for this for schema.'
		sys.exit()
	conn.commit()
	conn.close()

for url in url_list:
	TableCreate(url, db_name)
	RestToDB(url, db_name, conn, curs)
