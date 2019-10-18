import paramiko
import time
import sys
import getpass


def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output

def bgp_routing_weight_change(remote_conn):
    '''Modify the Weight for route in question''' 
    remote_conn.send("enable\n")
    remote_conn.send("cisco\n")
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 65019\n")
    remote_conn.send("address-family vpnv4\n")
    remote_conn.send("neighbor 2.2.2.2 route-map WEIGHT in\n")
    remote_conn.send("end\n")
    remote_conn.send("clear ip bgp * in\n")
    remote_conn.send("disable\n")
    time.sleep(5)   


if __name__ == '__main__':


    # VARIABLES THAT NEED CHANGED
    ip = '10.10.10.3'
    username = 'cisco'
    password = getpass.getpass()

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, allow_agent=False, look_for_keys= False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print output

    # Turn off paging
    disable_paging(remote_conn)
    
    # Set BGP Weight on 2.2.2.2 neighbor
    bgp_routing_weight_change(remote_conn)

    # Now let's try to send the router a command

    sys.exit("ALL Done!")
