import simplejson as json
import requests

base_url = 'http://127.0.0.1:5000/api/object/json'

# create credentials structure

tenant_url = base_url
get_response = requests.get(tenant_url)
a = json.loads(get_response.text)
#print a
#b = json.dumps(a, indent=2)
#print b

test =  a['imdata'][0]["Chassis"]['attributes']['serial_no']
print test

#z = x['serial_no']
