# https://projecteuler.net/problem=231
# prime factorisation of binomial coefficient
#

import math

# Use a sieve approach where for each prime figure out the prime factors  

def findSum(n,m):

# find prime factorisation of mCn. 
#   mCn = n!/m!  /m! 
#  so we want to find the sum of prime factors for two numbers : 
#    n(n-1)(n-2)...(n-m)   and m!
#
	
	numList = [1 for i in range(0,n+1)]

	sum1 = 0  # this will track sum of prime factors for n(n-1)(n-2)..(m)
	sum2 = 0  # this will track sum of prime factors for m!

	for i in range(2,n+1):

		# Nothing do for non-primes
		if numList[i] == 0:
			continue

		# For primes, mark all multiples as non-prime
		for k in range(2*i,n+1,i):   
			numList[k]=0

		# update sum1 and sum2 for factors of this prime
		iPower = i

		# We need to consider every power of this prime (i) separately
		while iPower <= n:
			iPowerMultiple = iPower 
			# This loop will add all multiples for m!
			for iPowerMultiple in range(iPower,n+1,iPower): 
				if iPowerMultiple > n-m:
					sum1 += i
				if iPowerMultiple <= m:
					sum2 += i

			#print iPower, sum1, sum2
			# Try the next multiple
			iPower *= i


	return sum1 - sum2


assert(findSum(10,3) == 14)
print findSum(20*10**6, 15*10**6)


