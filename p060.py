# https://projecteuler.net/problem=60
#

import util


#GeneratedPrimeMax = 100000
GeneratedPrimeMax = 1000000

primeList = util.GetPrimeList(GeneratedPrimeMax)	
primeDict = {}
for prime in primeList:
	primeDict[prime]=1


primePairDict = {}    # Stores a list of prime-pairs keyed by str((p1,p2)) where p1 < p2
		      # list grows as more primes are processed

LastMax = 999999    # 

for prime1 in primeList:
	# find prime-pairs for this prime, using primes processed so far
	pairList = []
	for prime2 in primeList:
		if prime2 >= prime1:
			break

		num1 = int(str(prime2)+str(prime1))
		if num1 > GeneratedPrimeMax:
			if not util.CheckPrime(num1):
				continue
		else:
			if num1 not in primeDict:
				continue
				
		num2 = int(str(prime1)+str(prime2))
		if num2 > GeneratedPrimeMax:
			if not util.CheckPrime(num2):
				continue
		else:
			if num2 not in primeDict:
				continue
			
		# Both combinations are primes
		pairList.append(prime2)
		assert(str((prime2,prime1)) not in primePairDict)
		primePairDict[str((prime2,prime1))] = 1

	numPairs = len(pairList)
	if numPairs > 4:
		# pair list contains all primes that form a prime pair with the current prime(prime1)
		# Try all sets of 4 at a time to see if they form a 5 prime set with prime1
		for i1 in range(0,numPairs-3):
			p1 = pairList[i1]
			for i2 in range(i1+1,numPairs-2):
				p2 = pairList[i2]
				if str((p1,p2)) not in primePairDict:
					continue

				for i3 in range(i2,numPairs-1):
					p3 = pairList[i3]
					if str((p1,p3)) not in primePairDict:
						continue
					if str((p2,p3)) not in primePairDict:
						continue

					for i4 in range(i3,numPairs):
						p4 = pairList[i4]
						if str((p1,p4)) not in primePairDict:
							continue
						if str((p2,p4)) not in primePairDict:
							continue
						if str((p3,p4)) not in primePairDict:
							continue
						print "Found a match ", p1,p2,p3,p4,prime1
						print "Answer = ", p1+p2+p3+p4+prime1

print "All done"

