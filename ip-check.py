#!/bin/python3

import sys
import re


#declare empyt strings to store user input of ip
ip = ''
if len(sys.argv) != 2:
	sys.exit('enter valid args')
else:
#second user arg is assigned as the ip
	ip = sys.argv[1]
#ip regualar expression
	ip_regEx = ('^(25[0-4]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.(25[0-4]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.(25[0-4]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.(25[0-4]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)$')
	
	''' ip address has 5 classes whose octet range from 0-255 and be divided to fit
the regular expression as follows: 
0-199, 200-249, 250-255 '''

#validate ip format using the RegEx
	ip_validate = re.findall(ip_regEx, ip)
	if ip_validate:
		print(f'ip {ip} is a valid ip')
	else:
		sys.exit('enter valid ip address x.x.x.x: (x<=255)')
		
		
