# https://projecteuler.net/problem=50
#

import util 

primeList = util.GetPrimeList(1000000)   
primeHash = {}
for prime in primeList:
	primeHash[prime]=1

maxPrime = primeList[-1]

maxSeqLen=0
answer=0

for i in range(0,len(primeList)): 
	sum=0
	for j in range(i,len(primeList)):
		sum += primeList[j]
		if sum > maxPrime:
			break
		if sum in primeHash:
			seqLen = j-i+1
			if seqLen > maxSeqLen:
				maxSeqLen = seqLen
				answer = sum 
				#print "Found a new max", maxSeqLen, answer
	

print answer

		
	
