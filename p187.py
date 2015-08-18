# https://projecteuler.net/problem=187
#

import util

maxN = 10**8

pStore = util.PrimeStore(maxN/2)   # smallest prime is 2, so the largest prime we would need is < N/2
plist = pStore.getList()

count = 0
for prime1 in plist:
	maxPrime2 = int(maxN/prime1)
	if maxPrime2 < prime1:
		break
	#print "p1 = ", prime1


	for prime2 in plist:
		if prime2 < prime1:
			continue 
		if prime2 > maxPrime2:
			break
		count += 1
		#print "   p2 = ", prime2, count

print "Answer =", count 


