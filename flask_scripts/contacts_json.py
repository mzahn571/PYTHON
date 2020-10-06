import requests
import json
import pprint
import time

# Define variable for RESTful Call
hostname = 'localhost'
url = "http://%s:5000/json/contacts"% hostname
username = 'student'
password = 'student'
dash = '~' * 110
top = '_' * 110

# Making RESTful call via python to attain JSON data
data = requests.get(url, auth=(username, password))
format_data = data.content
json_output = json.loads(format_data)
# Print all JSON Output
#print json_output
# Prettified JSON Output
#pprint.pprint(json_output)

# Iterate Routes for important information
print top
print('{:<2s}{:>15s}{:>20s}{:>15s}{:>25s}{:>25s}'.format('Id', 'First Name', 'Last Name', 'Gender', 'Email', 'IP Address'))
print dash
for contact in json_output['items']:
	contact_id = str(contact['id'])
	first_name = contact['first_name']
	last_name = contact['last_name']
	gender = contact['gender']
	email = contact['email']
	ip_addr = contact['ip_address']
	print('{:<2s}{:>15s}{:>20s}{:>15s}{:>32s}{:>20s}'.format(contact_id, first_name, last_name, gender, email, ip_addr))
	print dash
	time.sleep(.2)

