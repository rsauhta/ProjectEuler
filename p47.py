# https://projecteuler.net/problem=47
#
#

import util
import math

def findConsecutive(n):
	" Find n consecutive number that n distinct prime factors"

	number=1
	consecutive=0

	while (1):
		number +=1 
		if (number % 1000 == 0):
			print "Processing ", number

		factorsDict = util.FindFactor(number)
		if len(factorsDict.keys()) == n:
			consecutive += 1
		else : 
			consecutive=0

		if consecutive >= n:
			return number - n + 1 
			



assert(findConsecutive(2) == 14)
assert(findConsecutive(3) == 644)

print "Match starting from %d " % (findConsecutive(4)) 

