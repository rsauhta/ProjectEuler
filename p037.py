# https://projecteuler.net/problem=37
#

import util 

primeList = util.GetPrimeList(1000000)

primeHash = {2:1, 3:1, 5:1, 7:1 }


truncatableCounter = 0
truncatableSum = 0

for prime in primeList[4:]:
	primeHash[prime] = 1
	primeDigits = str(prime)
	truncatable = True
	for i in range(1,len(primeDigits)):
		if not (int(primeDigits[i:]) in primeHash and \
		        int(primeDigits[:-i]) in primeHash):
			truncatable = False
			break
	if truncatable:
		truncatableSum += prime
		truncatableCounter += 1
		print  truncatableCounter, " = ", prime
		if truncatableCounter > 11: 
			print "breaking"
			break
		    	
print truncatableSum 



