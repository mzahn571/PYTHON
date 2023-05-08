from onep_connect import *
import sys
import StringIO
import psycopg2

try:
    test = connect(sys.argv[1], 'cisco', 'cisco')
    if test:
        print "Connection to Element is Successful\n\n"
        properties = test.properties
        serial_no = properties.SerialNo
        sys_name =  properties.sys_name
        product_id = properties.product_id
        product_decr = properties.sys_descr
        test.disconnect()
except IOError:
    print "Connection could NOT be established...sorry!"
    test.disconnect()


DSN = 'dbname=postgres'

print "Opening connection using dsn:", DSN
conn = psycopg2.connect(DSN)
print "Encoding for this connection is", conn.encoding

curs = conn.cursor()
try:
    curs.execute("CREATE TABLE cisco_devices (device_name text, Serial_No text,\
        device_type text, description text)")
except:
    conn.rollback()
    curs.execute("DROP TABLE cisco_devices")
    curs.execute("CREATE TABLE cisco_devices (device text, Serial_No text)")
conn.commit()

# demostrate copy_to functionality
data = [(sys_name, serial_no, product_id, product_decr)]
query = "INSERT INTO cisco_devices VALUES (%s,%s,%s,%s)"
curs.executemany(query, data)
conn.commit()

# copy_to using custom separator
#io = open('/Users/pnegron/Desktop/TestConfig.txt', 'w')
#curs.copy_to(io, 'cisco_devices', ':')
#print "2) Copied %d records into file object using sep = :" % len(data)
#io.close()


sys.exit('Completed')
