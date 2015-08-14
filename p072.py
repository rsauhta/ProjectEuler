# https://projecteuler.net/problem=72
# Counting fractions
#

#
# The problem is to find all relatively prime number sets in the give range. S
#  To find relatively prime denominator for a given numerator, we can use approach similar to #70 
# 
# Answer must be sum of totient (phi) for all numbers >=2 and <=10**6
#   Take a number x. For all y that are relatively prime to x, we get x/y which can't be reduced.
#      For y that is not relatively prime to x, we can reduce it further until it hits a rational number
#       that must be covered by totient function for the reduced denominator



def computeAnswer(n):
	"Use the sieve method to find phi factors numbers <= n"

	n = n+1   # pesky python ranges :-) add +1 so I don't have to keep adjusting for range
	phiArray = range(n)

	total = 0

	for i in range(2,n):
		if phiArray[i] == i:   # this must be a prime
			for k in range(i,n,i):    # go through all multiples of i that are < n
				phiArray[k] = phiArray[k]*(i-1)/i

		# phi has been computed. Add it up
		total += phiArray[i]

	return total


assert( computeAnswer(8) == 21)
print computeAnswer(10**6)
