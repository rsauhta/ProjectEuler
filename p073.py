# https://projecteuler.net/problem=73
# Counting fractions in a range
#

#
# This problem is similar to #72 to create all unique proper fraction. However we need to constrain 
#  these to be within a range. 
#
# For a given denominator n, we find all unqiue fractions with a prime factor as  n*(1-1/p) viz. we are 
#   counting all multiples of p. This gives us the reduced number n' and factors for the next prime p' 
#  are n'/p'  so to get numbers that are prime we multiply as n(1-1/p)*(1-1/p'). This continues
# To count all multiples from range R1,R2 for a given prime p we can compute (R2-R2/p)-(R1-R1/p)
# We compute term R2/p separately so we can round it down the closest integer. In case of n/p we are 
#  guaranteed an integer so we can simplify as 1-1/p but we aren't guaranteed that with R1 and R2
#  
# 

import fractions
import math

def func(phi,ratio, composite):
	if composite == 2: return 0
	return int((phi-1)*(ratio*composite-1)/(composite-2))+1

def computeAnswer(n,r1,r2):
	"Use the sieve method to find phi factors numbers <= n"

	assert(r2 > r1)
	print "Running with ", n,r1,r2

	n = n+1   # pesky python ranges :-) add +1 so I don't have to keep adjusting for range
	phiArray = range(n)
	r1Array = [int(r1*i) for i in range(n)]
	r2Array = [int(r2*i) for i in range(n)]

	total = 0
	total2 = 0
	total3 = 0
	total4 = 0

	for i in range(2,n):
		if phiArray[i] == i:   # this must be a prime
			for k in range(i,n,i):    # go through all multiples of i that are < n
				term = phiArray[k]/i
				phiArray[k] -= term
				r1Array[k] -= int(term*r1)
				r2Array[k] -= int(term*r2)

		# phi has been computed. Add it up
		#print i, r1Array[i], r2Array[i], phiArray[i], func(phiArray[i],r1,i), func(phiArray[i],r2,i)
		#total += (r2Array[i] - r1Array[i])
		total += (func(phiArray[i],r2,i) - func(phiArray[i],r1,i))
		total2 += int(phiArray[i]/2)
		total3 += int(phiArray[i]/3)
		total4 += phiArray[i]

	print "total2 = ",total2
	print "total3 = ",total3
	print "total4 = ",total4
	#print "total phi = ", sum(phiArray) - phiArray[1]
	#print "total r2 = ", sum(r2Array) - r2Array[1]
	#print "total r1 = ", sum(r1Array) - r1Array[1]
	return total


def computeBrute(n):
	count = 0
	# fractions will be of the form numer/denom
	for denom in range(4,n+1):
		minNumer = int(math.ceil(float(denom)/3))
		maxNumer = int(denom/2)
		for numer in range(minNumer,maxNumer+1):
			if fractions.gcd(numer,denom) == 1:
				count += 1
				
	return count



#print computeAnswer(8,1.0/3,1.0/2) 
#print computeAnswer(12000,1.0/3,1.0/2) 

print "brute=",computeBrute(12000)
