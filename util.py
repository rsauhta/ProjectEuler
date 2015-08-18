
#
# Common modules for solving Euler project problems.
#

import math


class PrimeStore:
	def __init__(self, maxN):
		"Create a prime store with primes <= maxN"

		self.maxN = maxN
		self.numList = [1 for i in range(0,maxN+1)]

		for i in range(2,int(math.sqrt(maxN))+1):
			for j in range(2*i,maxN+1,i):
				self.numList[j]=0

		self.length = 0
		for i in range(2,maxN+1):
			if self.numList[i] == 1:
				self.length += 1

	def __iter__(self):
		return _prime_iterator_(self)

	def __len__(self):
		return self.length

	def isPrime(self, n):
		if n > self.maxN:
			raise Exception("range exceeded")

		return self.numList[n] == 1
	
class _prime_iterator_:
	def __init__(self,primeStore):
		self.primeStore = primeStore
		self.index = 2

	def next(self):
		while self.primeStore.numList[self.index] == 0:
			self.index += 1
			if self.index > self.primeStore.maxN:
				raise StopIteration
		self.index += 1
		return self.index - 1

	
def testPrimeStore():
	ps = PrimeStore(10)
	assert(ps.isPrime(9) == False)
	assert(ps.isPrime(3) == True)
	assert(ps.isPrime(7) == True)

	ps2 = PrimeStore(997)
	assert(len(ps2) == 168)







PrimeList = []

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def MillerRabin_isPrime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if MillerRabin_isPrime(x)]




def CheckPrime(n):
	" Returns true if n is prime."

	if (n == 1): return False
	if (n == 2): return True
	if n % 2 == 0: return False

	for i in range(3,int(math.sqrt(n))+1,2):
		if (n % i  == 0) : 
			return False
	return True


def _checkPrime(n): 
	" Returns true if n is prime. Uses PrimeList assuming PrimeList contains all primes upto sqrt(N) " 

	# The max prime we need to test is square root of n
	maxPrime = int(math.sqrt(n))
	PopulatePrimeList(maxPrime)   # Make sure prime list is populated

	for prime in PrimeList : 
		if (prime > maxPrime):
			break
		if (n % prime  == 0) : 
			return False

	return True


def GetDivisors(n):
	" Return a list of all proper divisors for the given number"
	divisors = set([1])
	for i in range(2,1+int(math.sqrt(n))):
		if (n % i == 0):   # found a divisor
			divisors.add(i)
			divisors.add(int(n/i))
	return sorted(divisors)
		



def PopulatePrimeList(n) : 
	"Add primes up to N in PrimeList. Builds on top of exisitng PrimeList"

	if PrimeList: 
		startingN = PrimeList[-1]
	else : 
		startingN = 1

	for number in range (startingN+1, n+1):
		if (_checkPrime(number)) : 
			PrimeList.append(number)
	
def GetFirstNPrime(n) : 
	"Return list of first n primes"

	primeListSize = len(PrimeList)

	if PrimeList: 
		startingN = PrimeList[-1]
	else : 
		startingN = 1

	candidatePrime = startingN 
	while (primeListSize < n) : 
		candidatePrime += 1
		if (_checkPrime(candidatePrime)) : 
			PrimeList.append(candidatePrime)
			primeListSize += 1

	return PrimeList[:n]


	
	           

def GetPrimeList(n) : 
	"Returns list of primes <= n "

	if n < 2: 
		return []

	PopulatePrimeList(n)

	counter=0
	for prime in PrimeList :   
		if prime > n : 
			break
		counter += 1

	return PrimeList[:counter]


def FindFactor(n) : 
	"Return a list of tuples with all prime factors and their powers for n"
	" 18 => [(2,1), (3,2)] "

	primeFactors = dict()

	maxPrimeToTest = int(math.sqrt(n))
	PopulatePrimeList(maxPrimeToTest)

	for prime in PrimeList : 
		if (prime > maxPrimeToTest) : 
			break
		if (n % prime == 0) : 
			count = 0
			while (n % prime == 0) : 
				n = n / prime
				count=count+1
			primeFactors[prime] = count
			maxPrimeToTest = int(math.sqrt(n))
	if (n != 1) : 
		#assert(_checkPrime(n))
		primeFactors[n] = 1

	return primeFactors


def testPrime() : 
	PrimeTo1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

	PopulatePrimeList(1000)
	assert( PrimeList == PrimeTo1000)

def test_checkPrime(): 
	assert(_checkPrime(2) == True)
	assert(_checkPrime(4) == False)
	assert(_checkPrime(7) == True)

def testCheckPrime(): 
	assert(CheckPrime(2) == True)
	assert(CheckPrime(4) == False)
	assert(CheckPrime(997) == True)
	assert(CheckPrime(998) == False)

def testFindFactor():
	assert(FindFactor(2) == {2:1 })
	assert(FindFactor(10) == {2:1 , 5:1})
	assert(FindFactor(23) == {23:1})
	assert(FindFactor(18) == {2:1 , 3:2})
	assert(FindFactor(2520) == dict([(2,3) , (3,2), (5,1), (7,1) ]))

def testGetPrimeList():
	assert(GetPrimeList(1) == [])
	assert(GetPrimeList(2) == [2])
	assert(GetPrimeList(3) == [2,3])


def testGetFirstNPrime():
	assert(GetFirstNPrime(2) == [2, 3])
	assert(GetFirstNPrime(1) == [2])
	assert(GetFirstNPrime(3) == [2, 3, 5])
	assert(GetFirstNPrime(9) == [2, 3, 5, 7, 11, 13, 17, 19, 23])

def testGetDivisors():
	assert(GetDivisors(10) == [1,2,5])
	assert(GetDivisors(81) == [1,3,9,27])
	assert(GetDivisors(28) == [1,2,4,7,14])

def testMillerRabin():
	assert(MillerRabin_isPrime(2) == True)
	assert(MillerRabin_isPrime(4) == False)
	assert(MillerRabin_isPrime(997) == True)
	assert(MillerRabin_isPrime(998) == False)

import timeit

if __name__ == "__main__":
        testMillerRabin()
	test_checkPrime()
	testCheckPrime()
	testPrime()
	testFindFactor()
	testGetPrimeList()
	testGetFirstNPrime()
	testGetDivisors()
	testPrimeStore()

	print "GetPrimeList =", timeit.timeit( 'GetPrimeList(1000000)',setup="from __main__ import GetPrimeList", number = 1)
	print "PrimeStore   =", timeit.timeit( 'PrimeStore(1000000)',setup="from __main__ import PrimeStore", number = 1)



