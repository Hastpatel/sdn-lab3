try:
	import os
	from scapy.all import *
	from scapy.contrib.openflow import *
	from scapy.contrib.openflow import *
	import json
	import time
except:
	print('Please install required modules.')

def read(fname):
	try:
		with open(fname,'r') as r:
			s=r.read()
			print('Existing data of switches')
			print(s)
			r.close()
		return s
	except:
		print('No existing data of swithces')
		return

def cap():
	os.system("tcpdump -s0 -i enp0s8 port 6633 -c 150 -w lab3.pcap")
	return


def dpid(c):
	a=rdpcap("lab3.pcap")
	i=0
	for packet in a:
		try:
			if a[i][TCP]:
				x=packet.payload.show
				x=str(x)
				#print(x)
				if 'OFPT_HELLO' in x:
					o2='connected'
				if 'OFPT_FEATURES_REPLY' in x:
					o0=x.split("datapath_id")[1][1]
					#print(o0[1][1])
					o1=x.split("src")[1][1:15]
					#print(o1[1][1:15])
					c[o0]={'ip_address':o1,'status':o2}
			i+=1
		except:
			pass
	return connected

def json_file(y):
	#y=json.dumps(f)
	#print(y)
	fname='connected.txt'
	with open(fname, "w") as f: 
		json.dump(y,f)
		f.close()
	print('File {} updated').format(fname)
	print('Updated file:')
	print(connected)
	return

if __name__=='__main__':
	connected={}
	while True:
		read('connected.txt')
		cap()
		y=dpid(connected)
		json_file(y)
