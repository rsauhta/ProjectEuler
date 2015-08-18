# https://projecteuler.net/problem=243
# Resilience
#

# Another problem that is related to totient function. Copied from #70
# resilience of a number n is phi(n)/(n-1)
# 

import util

def bruteForce(numer,denom):
	"Use the sieve method to find phi and check for the condition "

	n = 10**8
	phiArray = range(n)

	total = 0

	for i in range(2,n):
		if phiArray[i] == i:   # this must be a prime
			for k in range(i,n,i):    # go through all multiples of i that are < n
				phiArray[k] = phiArray[k]*(i-1)/i

		# phi has been computed for this i 
		# resilience = phi/(i-1) < numer/denom
		if phiArray[i]*denom < numer*(i-1):
			return i



def computeAnswer(numer, denom):
	primeList = util.PrimeStore(100).getList()

	# resilience = phi/(i-1) 
	#    phi = i * (1-1/p1)(1-1/p2)... where p1,p2 are prime factors
	# To minimize phi/(i-1) we must use as many prime as we can 
	#   and use smallest prime possible
	# 
	num = 1
	phi = 1

	for prime in primeList: 
		num *= prime
		phi *= (prime-1)
		#print prime, num, phi, phi*denom,"<", numer*(num-1)
		if phi*denom  < numer*(num-1):
			# roll back
			maxPrime = prime
			num /= prime
			phi /= (prime-1)
			break
	
	# by adding the last prime we probably went much lower than 
	#  we needed to go. 
	# resilience = (1-1/i) (1-1/p1)(1-1/p2)...
	#  If we keep the prime factors the same, we can still reduce resilience
	#  by increasing i

	#print num, phi, maxPrime

	# Created this by looking at the output of previous run
	#   we need to increase i by a factor less than 29 using primes less than 29
	# By definition all numbers <29 must be using primes less than 29
	#
	for multiple in range(1,maxPrime):
		newNum = num * multiple
		newPhi = phi * multiple
		#print multiple, newNum, newPhi, newPhi*denom,"<", numer*(newNum-1)
		if newPhi*denom < numer*(newNum-1):
			return newNum
		
	

#assert (bruteForce(4,10) == 12)
#print bruteForce(15499,94744)
print computeAnswer(15499,94744)
