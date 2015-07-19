# https://projecteuler.net/problem=21
#

import util

MaxNumber = 10000

total=0
for i in range(1,MaxNumber):
	s = sum(util.GetDivisors(i))

	if (s == i or s > MaxNumber-1): 
		continue

	if (sum(util.GetDivisors(s)) == i): 
		total += i	# This number will be encountered again. We could 
		 		#  optimize by using a cache but keep it simple for now

	
print total


