
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#

import math


PrimeList = []

def checkPrime(n): 
	" Returns true if n is prime. Uses PrimeList assuming PrimeList contains all primes upto sqrt(N) " 

	# The max prime we need to test is square root of n
	maxPrime = math.sqrt(n)

	for prime in PrimeList : 
		if (n % prime  == 0) : 
			return False
		if (prime > maxPrime):
			break

	return True



def populatePrimeList(n) : 
	"Add primes up to N in PrimeList. Builds on top of exisitng PrimeList"

	if PrimeList: 
		startingN = PrimeList[-1]
	else : 
		startingN = 2

	for number in range (startingN, n):
		if (checkPrime(number)) : 
			PrimeList.append(number)
	
def findFactor(n) : 
	"Return a list of all prime factors for n"

	primeFactors = []
	maxPrimeToTest = int(math.sqrt(n))
	populatePrimeList(maxPrimeToTest)

	for prime in PrimeList : 
		if (prime > maxPrimeToTest) : 
			break
		if (n % prime == 0) : 
			print " factor = ", prime
			while (n % prime == 0) : 
				n = n / prime
			primeFactors.append(prime)
	return primeFactors


def testPrime() : 
	populatePrimeList(1000)
	print PrimeList 




def main(): 
	# testPrime()
	#INPUT_NUMBER = 13195 
	INPUT_NUMBER = 600851475143 
	print "factors of ", INPUT_NUMBER, " are ", findFactor(INPUT_NUMBER)




main()
