#!/usr/bin/python

import pickle
import matplotlib.pyplot as plt


targets = [['dnspX01','blue'],['dnspX02','green'],['dnspX03','red'],['dnspX04','black']]
db = {}

for host in targets:
        db[host[0]] = {'ts': [], 'delay': []}

fh = open('dns_res_profiler.pkl', 'rb')
try:
        while True:
                r = pickle.load(fh)
                db[r[0]]['delay'].append(r[1])
                db[r[0]]['ts'].append(r[2])
except EOFError:
        print 'EOF, bailing out.'

#with open('dns_res_profiler.pkl', 'rb') as f:
#       data = pickle.load(f)

targets = [['dnspX01','blue'],['dnspX02','green'],['dnspX03','red'],['dnspX04','black']]

#for host in targets:
#       for d in data[host[0]]['delay']:
#               d=d*1000
#       plt.scatter(data[host[0]]['ts'], \
#        [d*1000 for d in data[host[0]]['delay']], \
#        color=host[1],label=host[0])


for host in targets:
        print host
        plt.scatter(db[host[0]]['ts'], \
         [d*1000 for d in db[host[0]]['delay']], \
         color=host[1],label=host[0])

plt.legend(loc='upper left')
plt.show()

