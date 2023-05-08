from onep_connect import *
import sys
from onep.interfaces import *

filter = InterfaceFilter(interface = None, interface_type=1 )

try:
    test = connect(sys.argv[1], 'cisco', 'cisco')
    if test:
        print "Connection to Element is Successful\n\n"
        properties = test.properties
        print "The Serial Number of the Chassis is: %s" % properties.SerialNo
        print "The Router Name is: %s" % properties.sys_name
        print "The Router has been up for %s seconds" % properties.sys_uptime
        print properties.product_id
        print properties.sys_descr
        Int_List = test.get_interface_list(filter)
        for interface in Int_List:
        	if interface.get_status().link == InterfaceStatus.InterfaceState.ONEP_IF_STATE_OPER_UP:
        	    intStatus = interface.get_status()
        	    print intStatus
        test.disconnect()
except IOError:
    print "Connection could NOT be established...sorry!"
    test.disconnect()
sys.exit('Completed')
