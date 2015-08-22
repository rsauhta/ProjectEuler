# https://projecteuler.net/problem=132
# large repunit factors
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
	k=1
	for k in xrange(1,num):
		repunit = repunit % num
		if repunit == 0:
			break

		repunit = repunit*10+1
		k += 1

	return k



MaxN=10**6
primeStore = util.PrimeStore(MaxN)

TargetK = 10**9

count = 0
total=0
for prime in primeStore:
	k = findK(prime)
	if k == 0:
		continue
	if TargetK % k == 0: 
		count += 1
		total += prime
		#print count, prime
		if count == 40:
			break

print "Answer =", total

