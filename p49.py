# https://projecteuler.net/problem=49
#

import util
import itertools

def permuteNum(n):
	permList = itertools.permutations([int(x) for x in str(n)])

	permSet = set()
	for l in permList:
		sum = 0
		for digit in l: 
			sum = sum*10 + digit
		permSet.add(sum)

	return sorted(permSet)
	


primeList = util.GetPrimeList(9999)

primeHash = {}
for prime in primeList: 
	primeHash[prime] = 1


for prime in primeList: 
	if prime < 1000:
		continue
	if primeHash[prime] == 2:    # already processed a permutation of this 
		continue
	
	primeSet = set()
	for num in permuteNum(prime):
		if num in primeHash:
			primeHash[num] = 2   # Mark it as being processed 
			primeSet.add(num)
	if len(primeSet) > 2: 
		# Check for an arithmetic sequence
		numList = sorted(primeSet)
		for i in range(0,len(numList)-2):
			num = numList[i]
			for j in range(i+1,len(numList)-1): 
				diff = numList[j] - num
				nextNum = num + 2*diff 
				if nextNum in primeSet:
					print "Found match: %d%d%d" %(num, numList[j], nextNum)


			

		
