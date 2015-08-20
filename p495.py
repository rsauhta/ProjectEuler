# https://projecteuler.net/problem=495
# Writing n as the product of k distinct positive integers
#

# Figure out how to express n! as factors

import util
def getFactorsInFactorial(n):
	"Return a dict of prime factors in n!"


	primeList = util.PrimeStore(n).getList()

	primeFactors = {}
	for prime in primeList:
		primePowers = prime
		count = 0   # track number of powers of this prime in n!
		while primePowers < n:
			count +=  int(n/primePowers)
			primePowers *= prime
		primeFactors[prime] = count

	return primeFactors

def test_getFactorsInFactorial():
	assert(getFactorsInFactorial(10) == {2:8, 3:4, 5:2, 7:1})


#print getFactorsInFactorial(10000)


def countCombinations(totalCount, maximum=100000):
	"Throw-away routine to count number of possible combination we may have to maintain"
	# We are not counting actual number of combinations but how many categories we need 
	# e.g. 2,2,16,32 is same category as 4,4,8,16 

	# We pass in totalCount = number of slots e.g. 30
	# We decide how many slots to put in the 1st number n=1-30
	#  The next number can only be placed in <=n slots

	if totalCount < 1: 
		return 1

	count=0
	for i in range(1,min(totalCount,maximum)+1):
		count += countCombinations(totalCount-i,i)
	return count

n=30
total=0
for i in range(n+1):
	total += countCombinations(i)
	print i,"=",countCombinations(i)
print total

