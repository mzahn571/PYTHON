import requests
import json
import pprint

# Define variable for RESTful Call
hostname = 'localhost'
url = "http://%s:5000/json/cisco/routes"% hostname
username = 'student'
password = 'student'
dash = '~' * 75
top = '_' * 75

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
print('{:<25s}{:>27s}{:>22s}'.format('Destination Subnet', 'Destination Interface', 'Protocol'))
print dash
for route in json_output['items']:
	dest_net = route['destination-network']
	dest_int = route['outgoing-interface']
	protocol = route['routing-protocol']
	print('{:<25s}{:>25s}{:>23s}'.format(dest_net, dest_int, protocol))
	print dash
