# https://projecteuler.net/problem=46
#

import util
import math

MaxNum = 100000  # Hopefully the answer is within this range
primeList = util.GetPrimeList(MaxNum)


for i in range(3,MaxNum,2):
	if i in primeList: 
		continue
	
	found=True
	for prime in primeList: 
		if prime > i:
			break
		diff = (i - prime)/2 
		sqrt = math.sqrt(diff)
		if sqrt == int(sqrt): 
			found=False
			break
	if found:
		print "Found answer : ", i
		exit()


print "Didn't find answer"
			

