#!/usr/bin/python
#Coding Challenge - MachEight
from sys import argv as input
from json import loads as json
from urllib.request import urlopen as open
url='https://mach-eight.uc.r.appspot.com/'
def read_data():
	with open(url) as response:
		a=response.read()
	b=json(a)
	return b
if len(input) == 2:
	try:
		data=read_data()['values']
		c=0
		for x in range(0,len(data)):
			for y in range(x,len(data)):
				if data[x]!=data[y] and int(data[x]['h_in'])+int(data[y]['h_in']) == int(input[1]):
					print('- '+data[x]['first_name']+' '+data[x]['last_name'],'         ',data[y]['first_name']+' '+data[y]['last_name'])
					c=c+1
		if c==0:
			print('No matches found')

	except:
		print('There is an error with the parameter!')
else:
	print('There is no valid parameter!')
