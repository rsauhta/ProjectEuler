# https://projecteuler.net/problem=27
#

import util

MaxPrime = 100000

PrimeList = util.GetPrimeList(MaxPrime)
PrimeHash = {}

for prime in PrimeList:
	PrimeHash[prime]=1


maxSequence=0
answer=0

for a in range(-999,1000):
	for b in range(-999,1000):
		counter=0
		for n in range(0,1000):
			sum = n*n + a*n + b
			if sum > MaxPrime: 
				print "Problem : ", sum
				break

			if sum in PrimeHash: 
				counter = n
			else:
				break
		if (counter > maxSequence):
			maxSequence = counter
			answer = a*b
			#print "Found a new max", counter,a,b
			
print "answer = ", answer
