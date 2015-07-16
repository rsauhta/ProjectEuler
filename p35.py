# https://projecteuler.net/problem=35
#

import util
import math



primeHash = {}
primeList = util.GetPrimeList(1000000)
for entry in primeList: 
	primeHash[entry]=1

circularCounter = 0
for entry in primeList:
	num = str(entry)
	circular = True 
	for i in range(0,len(num)-1):
		num = num[1:] + num[:1]   # rotate left by 1 
		if int(num) not in primeHash:
			circular = False
			break
	if circular == True: 
		#print entry
		circularCounter += 1
	

print "Circular prime counter = ", circularCounter


