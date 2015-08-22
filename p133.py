# https://projecteuler.net/problem=133
# large repunit non-factors
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



MaxN=100000
primeStore = util.PrimeStore(MaxN)

total=0
for prime in primeStore:
	k = findK(prime)
	if k == 0:
		#print prime
		total += prime
		continue

	#print prime, k
	# find if k will divide into 10^n
	#  That will only happen if only prime factors of k are 2 and/or 5
	while k % 2 == 0: 
		k = k/2
	while k % 5 == 0: 
		k = k/5
	if k != 1 : 
		#print prime
		total += prime

print "Answer =", total





