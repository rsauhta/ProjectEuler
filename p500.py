# https://projecteuler.net/problem=500
# Problem 500
#

# some trial and error shows 
# given a num = p1**a1 * p2**a2 * ...   where p1,p2 are prime factors and a1,a2.. are corresponding power
#    numDivisor = (a1+1)(a2+1)...
#
# One way to get 2**500500 divisor is to use first 500,500 primes but we can do better
# 
#  Consider case of getting 16 (2**4) divisor. Instead of using first 4 primes it is bettet to use 2**3 * 3**1 * 5**1
#    Instead of adding 7 as a factor, we can add 2**2 since 4 < 7. 
#  For larger number we may decide that adding 2**4 is better than adding another prime >16; or even better we would 
#    add 3**2. 
# 

import util
from heapq import *

Target=500500   # we need 2 raise to this number of divisors
NextFactor = []   # track powers of primes that would be next in line to be added to gain 2x more divisors

primeList = util.GetPrimeList(8*10**6)
primeIter = iter(primeList)

nextFactorHeap = []
heappush(nextFactorHeap, primeIter.next())    # start with a single prime
nextPrime = primeIter.next()

answer = 1
divisorPower=0

while (divisorPower < Target):

	if nextFactorHeap[0] > nextPrime:
		heappush(nextFactorHeap, nextPrime)
		nextPrime = primeIter.next()

	nextFactor  = heappop(nextFactorHeap)   # pop the smallest factor from heap
	                                        # Note this can be a prime or a power of prime

	#print divisorPower, "Nextfactor = ", nextFactor
	divisorPower += 1
	answer = (answer * nextFactor) % 500500507

	# put the next power of popped value back into heap
	#
	valueToPush = nextFactor * nextFactor
	heappush(nextFactorHeap, valueToPush)


print answer

