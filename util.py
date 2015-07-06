
#
# Common modules for solving Euler project problems.
#

import math

PrimeList = []

def CheckPrime(n): 
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



def PopulatePrimeList(n) : 
	"Add primes up to N in PrimeList. Builds on top of exisitng PrimeList"

	if PrimeList: 
		startingN = PrimeList[-1]
	else : 
		startingN = 1

	for number in range (startingN+1, n+1):
		if (CheckPrime(number)) : 
			PrimeList.append(number)
	

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
	PopulatePrimeList(n)

	#if (CheckPrime(n)) : 
		#primeFactors[n]=1
		#return primeFactors

	maxPrimeToTest = int(math.sqrt(n))
	for prime in PrimeList : 
		if (prime > maxPrimeToTest) : 
			break
		if (n % prime == 0) : 
			count = 0
			while (n % prime == 0) : 
				n = n / prime
				count=count+1
			primeFactors[prime] = count
	if (n != 1) : 
		assert(CheckPrime(n))
		primeFactors[n] = 1

	return primeFactors


def testPrime() : 
	PrimeTo1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

	PopulatePrimeList(1000)
	assert( PrimeList == PrimeTo1000)

def testCheckPrime(): 
	assert(CheckPrime(2) == True)
	assert(CheckPrime(4) == False)
	assert(CheckPrime(7) == True)

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



if __name__ == "__main__":
	testCheckPrime()
	testPrime()
	testFindFactor()
	testGetPrimeList()


