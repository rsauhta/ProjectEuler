# https://projecteuler.net/problem=58
#

import util


def spiralPrimePercent(targetPercent):

	spiralCount = 1
	primeCount =  0
	num=1
	skip=0
	for side in range (3,100000,2):
		skip += 2 
		for i in range(0,4):
			num += skip
			spiralCount += 1

			if util.CheckPrime(num):
				primeCount += 1
		percent = 100.0*float(primeCount)/spiralCount
		#print "%4d %02.8f %5d %d" % (side, percent, primeCount, spiralCount)
		if percent < targetPercent:
			print "Solution found for target %.2f: side=%d percent=%f primes=%d total=%d" \
			      %(targetPercent,side, percent, primeCount, spiralCount)
			return side
	print "Solution not found for ", targetPercent
	return -1


assert(spiralPrimePercent(50) == 11)
spiralPrimePercent(10)

