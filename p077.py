# https://projecteuler.net/problem=77
# Prime summation
#

import util

# Guessing that we will find the number within first MaxN numbers
MaxN = 10000
pStore = util.PrimeStore(MaxN)
PrimeList =  pStore.getList()

def countNumCombos(n, minPrime=2):
	"Split n into primes with the smalles prime being >= minPrime "

	count=0
	for prime in PrimeList:
		if prime > n: 
			break
		if prime < minPrime:
			continue
		if prime == n:
			count += 1
			break
		count += countNumCombos(n-prime, prime)
	
	#print n,minPrime, count
	return count


for i in range(100):
	numCombos = countNumCombos(i)
	if numCombos > 5000:
		print "Answer=", i
		break

