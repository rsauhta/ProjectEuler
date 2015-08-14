# https://projecteuler.net/problem=70
# Totient permutation
#

def computeAnswer(n):
	"Use the sieve method to find phi factors numbers < n"

	phiArray = range(n)
	minRatio = 100
	answer = 0

	for i in range(2,n):
		if phiArray[i] == i:   # this must be a prime
			for k in range(i,n,i):    # go through all multiples of i that are < n
				phiArray[k] = phiArray[k]*(i-1)/i

		else:  # phi has been computed. Check if it matches
			phi = phiArray[i]
			ratio = float(i)/phiArray[i]
			if ratio < minRatio:         # only check permutations, if ratio is lower than previous min
				phiStr = str(phiArray[i])
				iStr = str(i)
				if sorted(phiStr) == sorted(iStr):
					minRatio = ratio
					answer = i
					#print "Found new min:", MinRatio, i

	return answer



print "Answer = ", computeAnswer(10**7)



