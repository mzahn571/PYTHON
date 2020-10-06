import paramiko
import sys
import time
import re
import psycopg2

ipaddr ='10.10.10.2'
username = "cisco"
password = "cisco"
enable = "enable"
conf = "configure terminal"
host = "hostname R2"
end = "end"
exit = "exit"

def GET_BGP(remote_conn, ip):
    print "Getting BGP Information...\n"
    remote_conn.send("terminal length 0\n")
    remote_conn.send("enable\r")
    remote_conn.send("cisco\r")
    remote_conn.recv(1000)
    remote_conn.send("show ip bgp %s" % ip + "\r")
    time.sleep(2)
    output = remote_conn.recv(2000)
    network = ip
    local_pref = re.search(r'localpref ([0-9]+)', output)
    nexthop = re.search(r'Local.*\n.*(([0-9]\.){3}[0-9])', output)
    n1 =  network
    networklist = [network, nexthop.group(1),local_pref.group(1)]
    return networklist

def DATABASE_SEND(XXX,YYY,ZZZ):
	DSN = ('dbname=student')
	print "Opening connection using dsn:", DSN
	conn = psycopg2.connect(DSN)
	curs = conn.cursor()
	try:
		curs.execute("CREATE TABLE cisco_devices (Network text, NextHop text, LocalPref text)")
	except:
		conn.rollback()
		curs.execute("DROP TABLE cisco_devices")
		curs.execute("CREATE TABLE cisco_devices (Network text, NextHop text, LocalPref text)")
		conn.commit()
	
	# demostrate copy_to functionality
	data = ([('%s' % XXX, '%s' % YYY, '%s'% ZZZ)])
	query = "INSERT INTO cisco_devices VALUES (%s, %s, %s)"
	curs.executemany(query, data)
	conn.commit()
	
	# copy_to using custom separator
	print '\nCheck the Database for posted Info...'
	
router1 = raw_input('What is the router you are connecting to: ')
prefix = raw_input('What is the prefix you would like to see: ')
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(router1, username=username, password=password, look_for_keys= False, allow_agent= False)
remote_conn = remote_conn_pre.invoke_shell()
print "SSH connection established to %s" %  router1
test10= GET_BGP(remote_conn, '%s' % prefix)
DATABASE_SEND(test10[0], test10[1], test10[2])

sys.exit("operation completed")
