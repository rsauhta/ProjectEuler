# https://projecteuler.net/problem=347
# Largest integer divisble by two primes
#

import util 
import math

def findAnswer(n):


	#primeList = util.GetPrimeListFast(int(math.sqrt(n)))
	primeList = util.GetPrimeListFast(n)
	#print "prime list size for", n,"= ", len(primeList), primeList


	# Run a modified sieve algorithm
	numList = [0 for i in range(0,n+1)]

	#for i in range(1,int(math.sqrt(n))):
	for prime in primeList:
		#print "looping for prime", prime, i, n
		for j in range(prime,n+1,prime):
			#print "    ", j
			numList[j] += 1
				

	count = 0
	total = 0
	for i in range(0,n+1):
		if numList[i] == 2: 
			#print i,
			count += 1
			total += i

	#print
	#print numList

	print "count =", count, " total=", total
	return total


'''
	primeList= []
	for i in range(2,n+1):
		if numList[i]:
			primeList.append(i)

	return primeList

	#primeList = util.GetPrimeList(int(math.sqrt(maxNum)))
	primeList = util.GetPrimeList(maxNum)

	powerArray = []

	print "prime list size", len(primeList)
	# pre-compute powers for different primes
	for prime in primeList:
		primePowers = []
		multiple = prime

		while multiple < maxNum:
			primePowers.append(multiple)
			multiple *= prime
		powerArray.append(primePowers)

	print "size =", len(powerArray)
	# check all combinations for numbers that can be generated from 2 primes and track in sHash
	sHash = {}
	for i in range(0,len(powerArray)):
		for j in range(i+1, len(powerArray)):
			if (powerArray[i][0]* powerArray[j][0] > maxNum):
				break
			for power1 in powerArray[i]:
				for power2 in powerArray[j]:
					product = power1*power2
					if product > maxNum:
						break
					sHash[product]=1
	print len(sHash), len(powerArray)
	return sum(sHash.keys())

'''

print findAnswer(100)
#print findAnswer(10**7)
MaxNum = 10**7 
