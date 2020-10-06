import simplejson as json
import requests
import sys
import StringIO
import psycopg2
import re
import time
# import acos_client as acos

username = "student"
password = "student"
hostname = "f5-lb-01"

def CREATE_TABLE():
    try:
        curs.execute("CREATE TABLE F5_POOLS (name text, allowsnat text, selfLink text)")
    except:
        conn.rollback()
        curs.execute("DROP TABLE F5_POOLS")
        curs.execute("CREATE TABLE F5_POOLS (name text, allowsnat text, selfLink text)")
        conn.commit()

def TABLE_INSERT(name, snat, link ):
    data = [(name, snat, link)]
    query = "INSERT INTO F5_POOLS VALUES (%s,%s,%s)"
    curs.executemany(query, data)
    conn.commit()

    # copy_to using custom separator

    io = open('/Users/pnegron/Desktop/TestConfig.txt', 'w')
    curs.copy_to(io, 'F5_POOLS', ':')
    print "2) Copied %d records into file object using sep = :" % len(data)
    io.close()

# setup up a requests session

icr_session = requests.session()
icr_session.auth = (username, password)
# not going to validate the HTTPS certifcation of the iControl REST service
icr_session.verify = False
# we'll use JSON in our request body and expect it back in the responses
icr_session.headers.update({'Content-Type': 'application/json'})
# this is the base URI for iControl REST
icr_url = "https://%s/mgmt/tm" % hostname

# Simple example - get all LTM pool attributes
folder = "Common"
pool_name = "Python-Pool"

# add the module URI parts
request_url = icr_url + '/ltm/pool/'
# here is an example of calling an object explicitly.
request_url += '~' + folder + '~' + pool_name

# call the get method on your requests session
response = icr_session.get(request_url)

# look at the response
if response.status_code < 400:
    response_obj = json.loads(response.text)
    print "response %s" % response_obj

OBJ_1 = response_obj['name']
OBJ_2 = response_obj['allowSnat']
OBJ_3 = response_obj['selfLink']

print OBJ_1
print OBJ_2
print OBJ_3

DSN = 'dbname=pnegron'
print "Opening connection using dsn:", DSN
conn = psycopg2.connect(DSN)
print "Encoding for this connection is", conn.encoding
curs = conn.cursor()

#Connect to the device and retrieve 3 objects called name, nat, selflink#
CREATE_TABLE()
TABLE_INSERT(OBJ_1, OBJ_2, OBJ_3)

#c = acos.Client('172.16.1.158', acos.AXAPI_30, 'admin', 'a10')
#c.slb.server.create('Transfer_1', '10.1.213.233')
#c.slb.server.create('Transfer_2', '10.1.213.234')
#c.slb.service_group.create(OBJ_1,c.slb.service_group.TCP,c.slb.service_group.ROUND_ROBIN)
#c.slb.service_group.member.create(OBJ_1, 'Transfer_1', 80)
#c.slb.service_group.member.create(OBJ_1, 'Transfer_2', 80)
sys.exit('Completed')