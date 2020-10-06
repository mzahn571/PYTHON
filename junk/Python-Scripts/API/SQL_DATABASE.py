
DSN = 'dbname=postgres'

## don't modify anything below this line (except for experimenting)

import sys
import os
import StringIO
import psycopg2

if len(sys.argv) > 1:
    DSN = sys.argv[1]

print "Opening connection using dsn:", DSN
conn = psycopg2.connect(DSN)
print "Encoding for this connection is", conn.encoding

curs = conn.cursor()
try:
    curs.execute("CREATE TABLE cisco_devices (device text, Serial_No text)")
except:
    conn.rollback()
    curs.execute("DROP TABLE cisco_devices")
    curs.execute("CREATE TABLE cisco_devices (device text, Serial_No text)")
conn.commit()

# demostrate copy_to functionality
data = [('R1', '12345'),
        ('R2', '34567')]
query = "INSERT INTO cisco_devices VALUES (%s,%s)"
curs.executemany(query, data)
conn.commit()

# copy_to using custom separator
io = open('/home/student/Desktop/TestConfig.txt', 'w')
curs.copy_to(io, 'cisco_devices', ':')
print "2) Copied %d records into file object using sep = :" % len(data)
io.close()

#curs.execute("DROP TABLE cisco_devices")
#os.unlink('/Users/pnegron/Desktop/TestConfig.txt')
#conn.commit()
