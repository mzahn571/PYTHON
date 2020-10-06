#!/usr/local/bin/python

from __future__ import print_function
import os, re
import subprocess
import pdb
#pdb.set_trace()

custs_dict = dict()

with open("/home/mzahn/IPSS-customers/da_networks", 'r') as f:

	for line in f:
		line = line.split()
		if line[1] in custs_dict:
			custs_dict[line[1]].append(line[0])
			
		else:
			custs_dict[line[1]] = [line[0]]

print(custs_dict)
print('\n' * 2)
print(custs_dict.keys())
print('\n' * 5)
print(custs_dict.keys())

****************************

def cust_conf_dict():

	custs_dict = dict()

	with open("/home/mzahn/IPSS-customers/da_networks", 'r') as f:

		for line in f:
			line = line.split()
			if line[1] in custs_dict:
				custs_dict[line[1]].append(line[0])
			
			else:
				custs_dict[line[1]] = [line[0]]
cust_conf_dict()
