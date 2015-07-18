# https://projecteuler.net/problem=30
#

import math


powerList = []
for i in range(0,10):
	powerList.append(math.pow(i,5))

print powerList

# 6*9^5 = 354294   6 digit number
# 7*9^5 = 413343
#   i.e. 6 digit number so we don't need to check beyond 6 digits
# 

total = 0
for i in range(2,354294): 
	sum=0
	for digit in str(i): 
		sum += powerList[int(digit)]
	if (i == sum):
		print "fifth power : ", i
		total += i

print "Total = ", total 



