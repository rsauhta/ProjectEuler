# https://projecteuler.net/problem=5
#
# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all 
#  of the numbers from 1 to 20?
#

import util
import math

def findLCM(n) : 
	" find LCM for all numbers from 1..n"

	factorDict = {}
	for num in range(2,n+1):
		numFactors = util.FindFactor(num)
		for key in numFactors: 
			if (key not in factorDict or
			    numFactors[key] > factorDict[key]) : 
				factorDict[key]=numFactors[key]
	lcm = 1
	for prime in factorDict : 
		lcm = int(lcm * math.pow(prime,factorDict[prime]))

	return lcm
		


print findLCM(10)
print findLCM(20)
		



