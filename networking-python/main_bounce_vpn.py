#!/usr/local/bin/python
import re
import os 
import subprocess
import pdb
import time
import datetime
from datetime import timedelta

#Global variables

# Updating and removing existing ipsec.log
if os.path.exists('/home/syscheck/ipsec.log'):
    os.remove('/home/syscheck/ipsec.log')

# Cisco
# Update and removing 
if os.path.exists('/home/syscheck/vpn_ipsec.log'):
    os.remove('/home/syscheck/vpn_ipsec.log')

# Juniper
if os.path.exists('/home/syscheck/juniper_vpn.log'):
    os.remove('/home/syscheck/juniper_vpn.log')

# Updating and removing existing juniper_bgp.dll file. This file is the output of another script in the crontab, that runs ever night to update the existing BGP's on the juniper devices
if os.path.exists('/home/syscheck/juniper_bgp.dll'):
    os.remove('/home/syscheck/juniper_bgp.dll')

# Same as above but with juniper VPN ipaddresses 
if os.path.exists('/home/syscheck/juniper_vpn.dll'):
    os.remove('/home/syscheck/juniper_vpn.dll')

# Updating and removing existing report 
if os.path.exists('/home/syscheck/Bounces-report.txt'):
    os.remove('/home/syscheck/Bounces-report')

# This might be an add in might not be required 
if os.path.exists('/data/bgp-watch/Bounces-report.txt'):
    os.remove('/data/bgp-watch/Bounces-report.txt')

# Global variables

# This portion on the code may not be required is the script is running on mgmt01. The purpose of this script was to migrate the DLL files information to mgmt03

COMMAND1 = "cat /home/syscheck/juniper_bgp.dll"
HOST1 = "mgmt01"
PATH1 = " /home/syscheck/juniper_bgp.dll"

COMMAND2 = "cat /home/syscheck/cisco.dll"
PATH2 = " /home/syscheck/cisco.dll"

COMMAND3 = "cat /home/syscheck/juniper_vpn.dll"
PATH3 = " /home/syscheck/juniper_vpn.dll"

def scp_operation(PATH, HOST, COMMAND)

    f = open (PATH, "w")
    ssh = subprocess.Popen(["ssh", HOST, COMMAND],
        stdout=f,
        stderr= subprocess.PIPE)
    
    result = ssh.comunicate()[0]
    return result

scp_operation(PATH1, HOST1, COMMAND1)
scp_operation(PATH2, HOST1, COMMAND2)
scp_operation(PATH3, HOST1, COMMAND3)


# Parseing the main log file from the device capturing the verbiage as a BGP UP/DOWN or VPN UP/DOWN on Juniper and Cisco devices
def JUNIPER_BGP_PARSING():
# collecting information from the ipsec.log file 
# Parseing what is needed and putting it into ipsec.log

    p1 = subprocess.Popen(
        ["cat", "/var/log/ipsec"]
        stdout=subprocess.PIPE,
    )
    
    p2 = subprocess.Popen(
        ["grep", "-i", "--color", "Idle\|OpenConfirm"]'
        stdin=p1=stdout,
        stdout=subprocess.PIPE,
    )
    
    p3 = subprocess.Popen(
        ["awk", '{print $1, $2, $3, $20 $22 $13}'],
        stdin=p2=stdout,
        stdout=subprocess.PIPE
    )
    
    end_of_pipe = p3.stdout
    # Creating a List
    words = []
    
    for line in end_of_pipe:
        word = line.strip()
        words=word
        
        myfile = open('/home/syscheck/juniper_bgp.log', 'a')
        myfile.write(word + '\n')
        myfile.close()
        #testing 
        print(words)

# Running the define operation 
JUNIPER_BGP_PARSING()

def JUNIPER_VPN_PARSING():
# Same as above just caputue Just on VPN's that go UP/DOWN

    p1 = subprocess.Popen(
        ["cat", "/var/log/ipsec"]
        stdout=subprocess.PIPE,
    )
    
    p2 = subprocess.Popen(
        ["grep", "-i", "KMD_VPN_DOWN_ALARM_USER\|KMD_VPN_UP_ALARM_USER"]'
        stdin=p1=stdout,
        stdout=subprocess.PIPE,
    )
    
    p3 = subprocess.Popen(
        ["awk", '{print $1, $2, $3, $10, $14}'],
        stdin=p2=stdout,
        stdout=subprocess.PIPE
    )
    
    end_of_pipe = p3.stdout
    # Creating a List
    words = []
    
    for line in end_of_pipe:
        word = line.strip()
        words=word
        
        myfile = open('/home/syscheck/juniper_vpn.log', 'a')
        myfile.write(word + '\n')
        myfile.close()
        #testing 
        print(words)
        
JUNIPER_VPN_PARSING()

def CISCO_VPN_BGP_PARSING():
# CISCO VPN/BGP are define by one ipaddresses on a Cisco device 
    p1 = subprocess.Popen(
        ["cat", "/var/log/ipsec"]
        stdout=subprocess.PIPE,
    )
    
    p2 = subprocess.Popen(
        ["grep", "-i", "CRYPTO-5-IKEV2_SESSION_STATUS"]'
        stdin=p1=stdout,
        stdout=subprocess.PIPE,
    )
    
    p3 = subprocess.Popen(
        ["awk", '{print $1, $2, $3, $17, $19}'],
        stdin=p2=stdout,
        stdout=subprocess.PIPE
    )
    
    # Removes the last four characters in each line (rep by four dots)
    p4 = subprocess.Popen(
        ["sed", "s/....$//'],
        stdin=p3.stdout,
        stdout=subprocess.PIPE
    )
    
    end_of_pipe = p4.stdout
    
    # Creating a List
    words = []
    
    for line in end_of_pipe:
        word = line.strip()
        words=word
        
        myfile = open('/home/syscheck/cisco_VPN_BGP.log', 'a')
        myfile.write(word + '\n')
        myfile.close()
        #testing 
        print(words)

CISCO_VPN_BGP_PARSING()

# This next section parses through the new logs created, match them against the DLL to match on a customer 

# Juniper BGP captures 
juniper_ipec_devices = []                                                                   # Empty List
with open('/home/syscheck/juniper_bgp.log') as ipsec:
    for line in ipsec.readlines():
        if 'user' in line:
            continue
        juniper_ipec_devices.append(line)

# Juniper Library of Circuit ID's and address's 
juniper_bgp_neighbors = {}                                                                   # Empty Dictionary 
with open('/home/syscheck/juniper_bgp.dll') as juniper_bgp_connection_library:
    for line_bgp in juniper_bgp_connection_library.readlines():
        for bgp_bounces in juniper_ipsec_devices:
            ip = bgp_bounces.split(' ')[5]
            if ip in line_bgp:
                juniper_bgp_neighbors[ip] = line_bgp.split(' ')[0]

# Juniper Report (report includes on bounces that occur)
with open('/home/syscheck/Bounces-report.txt', 'a') as report_jbgp:
    report_jbgp.write(template)
    for ip in juniper_bgp_neighbors.keys():
        report_jbgp.write(juniper_bgp_neighbors[ip])
        report_jbgp.write('\n' * 2)
        for bgp_bounces in juniper_ipsec_devices:
            # Printing report
            time = ' '.join(bgp_bounces.split(' ')[0:3])
            if 'Established Idle' in bgp_bounces:
                report_jbgp.write('Incident Date and Time: {}     UTC\n'.format(time))
            elif 'OpenConfirm Established' in bgp_bounces:
                report_jbgp.write('Restore Date and Time: {}      UTC\n\n'.format(time))
            else:
                print 'Unknown line: {}'.format(bgp_bounces
report_jbgp.close()

# Cisco VPN and BGP capture 
cisco_ipsec_devices = []                                                                            # Empty List
with open ('/home/syscheck/cisco_VPN_BGP.log') as cisco_log:
    for line in cisco_log.readline():
        if 'user' in line:
            continue
        cisco_ipsec_devices.append(line)
        
# Cisco Library of Circuit ID's and addresses
cisco_vpn = {}                                                                                       # Empty Dictionary
with open('/home/syscheck/cisco.dll') as cisco_connection_library:
    for line_cisco in cisco_connection_library():
        for vpn_bounces in cisco_ipsec_devices:
            ip_vpn = vpn_bounces.split(' ')[4]
            if ip_vpn in line_cisco:
                cisco_vpn[ip_vpn] = line_cisco.split(' ')[0]
                
# Cisco report 
with open ('/home/syscheck/Bounces-report.txt', 'a') as report_cvpn:
    report_cvpn.write(template1)
    for ip_vpn in cisco_vpn.keys():
        report_cvpn.write(cisco_vpn[ip_vpn])
        report_cvpn.write('\n' *2)
        for vpn_bounces in cisco_ipsec_devices:
            # Print report
            if ip_vpn in vpn_bounces:
                time = ' '.join(vpn_bounces.split(' ')[0:3])
                if 'DOWN' in vpn_bounces:
                    report_cvpn.write('Incident Date and Time: {}     UTC\n'.format(time))
                elif 'UP' in vpn_bounces:
                    report_cvpn.write('Restore Date and Time: {}     UTC\n\n'.format(time))
                else:
                    print 'Unknown line: {}'.format(vpn_bounces)
report_cvpn.close()

# Juniper VPN log capture
juniper_ipsec_devices = []                                                                             # Empty list 
with open ('/home/syscheck/juniper_vpn.log') as juniper_vpn_log:
    for line in juniper_vpn_log.readlines():
        juniper_ipsec_vpn_devices.append(line)

# Juniper VPN Library of Circuit ID's and address's 
juniper_vpnike = {}                                                                                     # Empty Dictionary
with open('/home/syscheck/juniper_vpn.dll') as juniper_vpn_library:
    for line_ike in juniper_vpn_library.readlines():
        for ike_bounces in juniper_ipsec_vpn_devices:
            ip_ike = ike_bounces.split(' ')[4]
            if ip_ike in line-ike:
                juniper_vpnike[ip_ike] = line_ike.split(' ')[0]
                
# Juniper Report 
with open ('/home/syscheck/Bounces-report.txt', 'a') as report_jvpn:
    report_jvpn.write(template1)
    for ip_ike in juniper_vpnike.keys():
        report_jvpn.write(juniper_vpnike[ip_ike])
        report_jvpn.write('\n' *2)
        for ike_bounces in juniper_ipsec_vpn_devices:
            if ip_ike in ike_bounces:
                if 'KMD_VPN_DOWN_ALARM_USER:' in ike_bounces:
                    stime = (ike_bounces.split(' ')[:3])
                    startime = '%s %s %s' % (stime[0], stime[1].zfill(2), stime[2])
                elif 'KMD_VPN_UP_ALARM_USER:' in ike_bounces:
                    etime = '%s %s %s' % (etime[0], etime[1].zfill(2), etime[2])
                    delta = datetime.datetime.strptime(endtime, time_format ) - datetime.datetime.strptime(startime, time_format)
                    if delta >= datetime.timedelta(seconds=120):
                        report_jvpn.write('Incident Date and Time: {}    UTC\n' .format(startime))
                        report_jvpn.write('\n' * 1)
                        report_jvpn.write('Incident Date and Time: {}    UTC\n' .format(endtime))
                    else:
                        report_jvpn.write('Incident Date and Time: {}    UTC\n' .format(startime))
                        report_jvpn.write('\n' * 1)
                        report_jvpn.write('Incident Date and Time: {}    UTC\n' .format(endtime))
                        report_jvpn.write('      Conditions under 2 mintues\n')
                        report_jvpn.write('\n' * 1)
                        report_jvpn.write('------\n')
                        report_jvpn.write('\n' * 1)
                    else:
                        print 'Unknownline: {}' .format(ike_bounces)
report_jvpn.close()

COMMAND_LINE = 'mail -s 'Report - BGP's & VPN Bounces " michael.zahn@centurylink.com < /home/syscheck/Bounces-report.txt'


