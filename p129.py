# https://projecteuler.net/problem=129
# Repunit divisibility
#

import util
import fractions

def findK(num):
	'''
	Given a number find the R(k) divisible by number. Return k. 
	'''

	if num % 2 == 0 or num % 5 == 0:
		return 0

	repunit=1
	for k in xrange(1,num):
		repunit = repunit % num
		if repunit == 0:
			break

		repunit = repunit*10+1
		k += 1

	return k



# Trial and error shows that k is prime-1 or prime for most primes. 
# Also I have a suspicion that for a composite k = lcm(p1)lcm(p2) where p1,p2.. are prime factors
#  In any case k for composite is even lower than the number. 
# So we have to start from 1 million and compute k for each number till the answer is found
#

for i in range(10**6,10**6+1000):
	k = findK(i)
	#print i, findK(i)
	if k > 10**6:
		print "Answer =", i
		break



