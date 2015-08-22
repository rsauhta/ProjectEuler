# https://projecteuler.net/problem=130
# Composites with prime repunit property
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



primeStore = util.PrimeStore(100000)

total = 0
count = 0
for i in range(3,100000):
	if primeStore.isPrime(i):
		continue
	k = findK(i)
	if k and (i-1)%k == 0: 
		count += 1
		total += i
		if count == 25:
			break

print total

