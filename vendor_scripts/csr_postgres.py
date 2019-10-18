import requests
import json
import sys
import re
import psycopg2

dash = '~' * 50
hostname = 'csr-rtr-01'
device = "https://%s:55443/"% hostname
token = ''
username = 'student'
password = 'student'

def GetToken(device):
	global token
	token_url = device+'api/v1/auth/token-services'
	get_token = requests.post(token_url, auth=(username, password), verify=False)
	token_resp = json.loads(get_token.text)
	for key, value in token_resp.iteritems():
		if key == 'token-id':
			token = value
			print 'Token Key is: %s'% token

def GetInterfaces(device, token, headers, dash):
	global if_desc
	global if_name
	global ip_addr
	global mac_addr
	print '\n- Getting Interface Information'
	# URL Path to CSR Interfaces Information
	int_url = device+'api/v1/interfaces'
	# Making RESTful call via python to CSR Device
	get_int = requests.get(int_url,
		headers=headers,
		verify=False)
	# Preparing Iteration of JSON from REST Output
	int_resp = json.loads(get_int.text)
	print "Here is the output before we iterate:"
	print int_resp
	# Iterating Interface Attributes within JSON Output
	for output in int_resp['items']:
		for key, value in output.iteritems():
			if key == 'description':
				if_desc = value
			if key == 'if-name':
				if_name = value
			if key == 'ip-address':
				ip_addr = value
			if key == 'mac-address':
				mac_addr = value
		#Insert each Interface and their respective attributes into DB
		print "- Inserting Interface values into Table"
		curs.execute("INSERT INTO CSR_INT VALUES ('%s','%s','%s','%s')"% (if_name, if_desc, ip_addr, mac_addr))

		# Printout of each Interface and their respective attributes
		print dash
		print 'Interface ID: %s'% if_name
		print 'Interface Name: %s'% if_desc
		print 'IP Address: %s'% ip_addr
		print 'Mac Address: %s'% mac_addr

def GetTable(device, token, headers, dash):
	print '- Getting Route Table Information'
	# URL Path to CSR Route Table Information
	tbl_url = device+'api/v1/routing-svc/routing-table'
	# Making RESTful call via python to CSR Device
	get_tbl = requests.get(tbl_url,
		headers=headers,
		verify=False)
		# Preparing Iteration of JSON from REST Output
	tbl_resp = json.loads(get_tbl.text)
	# Iterating Router Table Attributes within JSON Output
	for output in tbl_resp['items']:
		for key, value in output.iteritems():
			if key == 'destination-network':
				dest = value
			if key == 'routing-protocol':
				proto = value
			if key == 'next-hop-router':
				next_hop = value
			if key == 'distance':
				dist = value
		# Printout of each Route Entry and their respective attributes
		print dash
		print 'Routing Protocol: %s'% proto.title()
		print 'Destination: %s'% dest
		print 'Next Hop: %s'% next_hop
		print 'Distance: %s'% dist

def CreateInterfaceTable():
	try:
		curs.execute("CREATE TABLE CSR_INT (INT_NAME text, INT_DESC text, IP_ADDRESS text, MAC_ADDRESS text)")
	except:
		conn.rollback()
		curs.execute("DROP TABLE CSR_INT")
		curs.execute("CREATE TABLE CSR_INT (INT_NAME text, INT_DESC text, IP_ADDRESS text, MAC_ADDRESS text)")

# Connect to Postgres Database named 'student'
postgres_db = 'dbname=student'
print "- Opening Database Connection to", postgres_db
conn = psycopg2.connect(postgres_db)
curs = conn.cursor()
print "- Creating Interface Table in Postgres"
CreateInterfaceTable()
print "- Getting Authentication Token from CSR Router"
GetToken(device)
headers = {'X-Auth-Token':token,
	'Content-Type':'application/json',
	'Accept':'application/json'}
GetInterfaces(device, token, headers, dash)
GetTable(device, token, headers, dash)
print '*** Operation Completed! ***'
conn.commit()
sys.exit(0)
