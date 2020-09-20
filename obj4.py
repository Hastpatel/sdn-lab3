#! /usr/bin/env python3


try: 
  import subprocess
  import time
except: 
  print("Install required modules.")

c_out = subprocess.Popen(['ovs-vsctl set-controller BR0 tcp:10.20.30.2:6633'], stdout = subprocess.PIPE, shell = True)
(cout,err) = c_out.communicate()
time.sleep(10)
out = subprocess.Popen(['ovs-vsctl show'], stdout = subprocess.PIPE, shell = True)
(out1,err) = out.communicate()
o1 = str(out1).split('\n')
fail = o1[-8].strip()
y = o1[-9].strip().split(' ')
ip = o1[-10].strip().split(':')
port = ip[2][0:4]

if y[1] == 'true':
  print('Controller is connected on {}, port {} .'.format(ip[1],port))
else: 
  print('Controller is not connected.')

print('Current fail mode: {}'.format(fail))