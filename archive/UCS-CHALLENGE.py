#!/usr/bin/env python

from UcsSdk import *
import getpass


password = getpass.getpass()

try:
    handle = UcsHandle()
    handle.Login("172.16.48.135", username = "config", password = password)
    
    getRsp = handle.GetManagedObject(None, None ,{OrgOrg.DN:"org-root"})
    # adds a service profile sp_name with-in every Org returned in the previous operation
    addSubOrg = handle.AddManagedObject(getRsp, OrgOrg.ClassId(), { OrgOrg.NAME :"SKYLINE"})
    getRsp2 = handle.GetManagedObject(None, None ,{OrgOrg.DN:"org-root/org-SKYLINE"})
    handle.Logout()
    print "You have successfully logged in!"
    for list in getRsp2:
        print list
except IOError:
    print "You could not login Sir!"
    

TopDN = handle.GetManagedObject(None, None, {"Dn":"org-root"})

handle.StartTransaction()
handle.AddManagedObject(TopDN, "computeServerDiscPolicy", {"Qualifier":"", "ScrubPolicyName":"", "Descr":"", "PolicyOwner":"local", "Action":"user-acknowledged", "Dn":"org-root/server-discovery", "Name":"default"}, True)

handle.AddManagedObject(TopDN, "computePsuPolicy", {"Dn":"org-root/psu-policy", "PolicyOwner":"local", "Descr":"", "Redundancy":"grid"
}, True)

handle.AddManagedObject(TopDN, "computeChassisDiscPolicy", {"Descr":"", "PolicyOwner":"local", "LinkAggregationPref":"none", "Action":
"2-link", "Dn":"org-root/chassis-discovery", "Name":"", "Rebalance":"user-acknowledged"}, True)
handle.CompleteTransaction()

handle.AddManagedObject(TopDN, "computeChassisDiscPolicy", {"Name":"", "LinkAggregationPref":"port-channel", "PolicyOwner":"local", "Dn":"org-root/chassis-discovery", "Descr":"", "Action":"2-link", "Rebalance":"user-acknowledged"}, True)
handle.AddManagedObject(TopDN, "computePsuPolicy", {"PolicyOwner":"local", "Dn":"org-root/psu-policy", "Descr":"", "Redundancy":"grid"}, True)

LAN_A = handle.GetManagedObject(None, None, {"Dn":"fabric/lan/A"})
handle.AddManagedObject(LAN_A, "fabricEthLanEp", {"AdminSpeed":"10gbps", "UsrLbl":"", "AdminState":"enabled", "SlotId":"1", "Dn":"fabric/lan/A/phys-slot-1-port-1", "FlowCtrlPolicy":"default", "EthLinkProfileName":"default", "Name":"", "PortId":"1"})
handle.AddManagedObject(LAN_A, "fabricEthLanEp", {"AdminSpeed":"10gbps", "UsrLbl":"", "AdminState":"enabled", "SlotId":"1", "Dn":"fabric/lan/A/phys-slot-1-port-2", "FlowCtrlPolicy":"default", "EthLinkProfileName":"default", "Name":"", "PortId":"2"})

handle.StartTransaction()
mo = handle.AddManagedObject(LAN_A, "fabricEthLanPc", {"AdminSpeed":"10gbps", "AdminState":"enabled", "Dn":"fabric/lan/A/pc-1", "FlowCtrlPolicy":"default", "Descr":"", "OperSpeed":"10gbps", "PortId":"1", "Name":"TST-PortChannel"})
mo_1 = handle.AddManagedObject(mo, "fabricEthLanPcEp", {"Name":"", "PortId":"1", "EthLinkProfileName":"default", "Dn":"fabric/lan/A/pc-1/ep-slot-1-port-1", "SlotId":"1", "AdminState":"enabled"}, True)
mo_2 = handle.AddManagedObject(mo, "fabricEthLanPcEp", {"Name":"", "PortId":"2", "EthLinkProfileName":"default", "Dn":"fabric/lan/A/pc-1/ep-slot-1-port-2", "SlotId":"1", "AdminState":"enabled"}, True)
handle.CompleteTransaction()

LAN_B = handle.GetManagedObject(None, None, {"Dn":"fabric/lan/B"})
handle.AddManagedObject(LAN_B, "fabricEthLanEp", {"AdminSpeed":"10gbps", "UsrLbl":"", "AdminState":"enabled", "SlotId":"1", "Dn":"fabric/lan/B/phys-slot-1-port-1", "FlowCtrlPolicy":"default", "EthLinkProfileName":"default", "Name":"", "PortId":"1"})
handle.AddManagedObject(LAN_B, "fabricEthLanEp", {"AdminSpeed":"10gbps", "UsrLbl":"", "AdminState":"enabled", "SlotId":"1", "Dn":"fabric/lan/B/phys-slot-1-port-2", "FlowCtrlPolicy":"default", "EthLinkProfileName":"default", "Name":"", "PortId":"2"})

handle.StartTransaction()
mo = handle.AddManagedObject(LAN_B, "fabricEthLanPc", {"AdminSpeed":"10gbps", "AdminState":"enabled", "Dn":"fabric/lan/B/pc-1", "FlowCtrlPolicy":"default", "Descr":"", "OperSpeed":"10gbps", "PortId":"1", "Name":"TST-PortChannel"})
mo_1 = handle.AddManagedObject(mo, "fabricEthLanPcEp", {"Name":"", "PortId":"1", "EthLinkProfileName":"default", "Dn":"fabric/lan/B/pc-1/ep-slot-1-port-1", "SlotId":"1", "AdminState":"enabled"}, True)
mo_2 = handle.AddManagedObject(mo, "fabricEthLanPcEp", {"Name":"", "PortId":"2", "EthLinkProfileName":"default", "Dn":"fabric/lan/B/pc-1/ep-slot-1-port-2", "SlotId":"1", "AdminState":"enabled"}, True)
handle.CompleteTransaction()

LAN = handle.GetManagedObject(None, None, {"Dn":"fabric/lan"})
handle.AddManagedObject(LAN, "fabricVlan", {"Sharing":"none", "Dn":"fabric/lan/net-MGMT-VLAN-100", "Id":"100", "CompressionType":"included", "DefaultNet":"no", "McastPolicyName":"", "PubNwName":""
, "Name":"MGMT-VLAN-100", "PolicyOwner":"local"})


TOP_SKYLINE = handle.GetManagedObject(None, None, {"Dn":"org-root/org-SKYLINE"})

handle.StartTransaction() 
mo = handle.AddManagedObject(TOP_SKYLINE, "lsbootPolicy", {"Name":"TST-BOOT-WVOT", "PolicyOwner":"local", "RebootOnUpdate":"no", "Dn":"org-root/org-SKYLINE/boot-policy-TST-BOOT-WVOT", "Descr":"", "BootMode":"legacy",
 "EnforceVnicName":"yes"})
mo_1 = handle.AddManagedObject(mo, "lsbootVirtualMedia", {"Dn":"org-root/org-SKYLINE/boot-policy-TST-BOOT-WVOT/read-only-local-vm", "LunId":"0", "Access":"read-only-local", "Order":"1"})
handle.CompleteTransaction()

handle.AddManagedObject(TOP_SKYLINE, "storageLocalDiskConfigPolicy", {"Dn":"org-root/org-SKYLINE/local-disk-config-WVOT-RAID", "Descr":"", "FlexFlashState":"disable", "Name":"WVOT-RAID", "FlexFlashRAIDReportingState"
:"disable", "Mode":"raid-mirrored", "ProtectConfig":"yes", "PolicyOwner":"local"})

handle.AddManagedObject(TOP_SKYLINE, "lsmaintMaintPolicy", {"Name":"USR-ACK-WVOT", "UptimeDisr":"user-ack", "PolicyOwner":"local", "SchedName":"", "Descr":"", "Dn":"org-root/org-SKYLINE/maint-USR-ACK-WVOT"})

handle.AddManagedObject(TOP_SKYLINE, "computeScrubPolicy", {"BiosSettingsScrub":"yes", "Name":"WVOT-SCRUB", "Dn":"org-root/org-SKYLINE/scrub-WVOT-SCRUB", "DiskScrub":"yes", "Descr":"TST-SCRUB-WVOT", "FlexFlashScrub":
"no", "PolicyOwner":"local"})

handle.AddManagedObject(TOP_SKYLINE, "solPolicy", {"Name":"WVOT-SOL", "PolicyOwner":"local", "Dn":"org-root/org-SKYLINE/sol-WVOT-SOL", "Descr":"", "AdminState":"enable", "Speed":"9600"})

handle.StartTransaction()
mo = handle.AddManagedObject(TOP_SKYLINE, "uuidpoolPool", {"Name":"WVOT-UUID-SUFFIX", "Prefix":"A0000000-0000-0001", "PolicyOwner":"local", "Dn":"org-root/org-SKYLINE/uuid-pool-WVOT-UUID-SUFFIX", "Descr":"", "AssignmentOrder":"sequential"})
mo_1 = handle.AddManagedObject(mo, "uuidpoolBlock", {"Dn":"org-root/org-SKYLINE/uuid-pool-WVOT-UUID-SUFFIX/block-from-0000-000000000001-to-0000-000000000003", "To":"0000-000000000003", "From":"0000-000000000001"})
handle.CompleteTransaction()

handle.StartTransaction()
mo = handle.AddManagedObject(TOP_SKYLINE, "macpoolPool", {"Name":"WVOD-MAC-POOL-A", "PolicyOwner":"local", "Dn":"org-root/org-SKYLINE/mac-pool-WVOD-MAC-POOL-A", "Descr":"", "AssignmentOrder":"sequential"})
mo_1 = handle.AddManagedObject(mo, "macpoolBlock", {"Dn":"org-root/org-SKYLINE/mac-pool-WVOD-MAC-POOL-A/block-00:25:B5:10:AA:01-00:25:B5:10:AA:64", "To":"00:25:B5:10:AA:64", "From":"00:25:B5:10:AA:01"})
handle.CompleteTransaction()

handle.StartTransaction()
mo = handle.AddManagedObject(TOP_SKYLINE, "macpoolPool", {"Name":"WVOD-MAC-POOL-B", "PolicyOwner":"local", "Dn":"org-root/org-SKYLINE/mac-pool-WVOD-MAC-POOL-B", "Descr":"", "AssignmentOrder":"sequential"})
mo_1 = handle.AddManagedObject(mo, "macpoolBlock", {"Dn":"org-root/org-SKYLINE/mac-pool-WVOD-MAC-POOL-B/block-00:25:B5:10:BB:01-00:25:B5:10:BB:64", "To":"00:25:B5:10:BB:64", "From":"00:25:B5:10:BB:01"})
handle.CompleteTransaction()

SAN = handle.GetManagedObject(None, None, {"Dn":"fabric/san"})
handle.AddManagedObject(SAN, "fabricVsan", {"FcZoneSharingMode":"coalesce", "ZoningState":"disabled", "FcoeVlan":"1010", "PolicyOwner":"local", "Dn":"fabric/san/", "Name":"Invicta-10", "Id":"10"})

handle.StartTransaction()
mo = handle.AddManagedObject(TOP_SKYLINE, "fcpoolInitiators", {"Descr":"", "PolicyOwner":"local", "AssignmentOrder":"sequential", "Purpose":
"node-wwn-assignment", "Dn":"org-root/org-SKYLINE/wwn-pool-WVOT-WWNN", "Name":"WVOT-WWNN"})
mo_1 = handle.AddManagedObject(mo, "fcpoolBlock", {"To":"20:00:00:25:B5:01:00:0A", "From":"20:00:00:25:B5:01:00:01", "Dn":"org-root/org-SKYLINE/wwn-pool-WVOT-WWNN/block-20:00:00:25:B5:01:00:01-20:00:00:25:B5:01:00:0A"})
handle.CompleteTransaction()

handle.StartTransaction()
mo = handle.AddManagedObject(TOP_SKYLINE, "fcpoolInitiators", {"Descr":"", "PolicyOwner":"local", "AssignmentOrder":"sequential", "Purpose":
"port-wwn-assignment", "Dn":"org-root/org-SKYLINE/wwn-pool-WVOT-WWPN-A", "Name":"WVOT-WWPN-A"})
mo_1 = handle.AddManagedObject(mo, "fcpoolBlock", {"To":"20:01:00:25:B5:AA:00:14", "From":"20:01:00:25:B5:AA:00:01", "Dn":"org-root/org-SKYLINE/wwn-pool-WVOT-WWPN-A/block-20:01:00:25:B5:AA:00:01-20:01:00:25:B5:AA:00:14"})
handle.CompleteTransaction()

handle.StartTransaction()
mo = handle.AddManagedObject(TOP_SKYLINE, "fcpoolInitiators", {"Descr":"", "PolicyOwner":"local", "AssignmentOrder":"sequential", "Purpose":
"port-wwn-assignment", "Dn":"org-root/org-SKYLINE/wwn-pool-WVOT-WWPN-B", "Name":"WVOT-WWPN-B"})
mo_1 = handle.AddManagedObject(mo, "fcpoolBlock", {"To":"20:01:00:25:B5:BB:00:14", "From":"20:01:00:25:B5:BB:00:01", "Dn":"org-root/org-SKYLINE/wwn-pool-WVOT-WWPN-B/block-20:01:00:25:B5:BB:00:01-20:01:00:25:B5:BB:00:14"})
handle.CompleteTransaction()

sys.exit('Completed Successfully!!!')
