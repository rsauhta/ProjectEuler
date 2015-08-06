# https://projecteuler.net/problem=10
#
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million
#

import util
import math


NUM = 2000000

primeList = util.GetPrimeList(NUM)

sum=0
for prime in primeList : 
	sum += prime
	
print "Sum = ", sum
