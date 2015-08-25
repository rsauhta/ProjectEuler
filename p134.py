# https://projecteuler.net/problem=134
# Prime pair connections
#

import math
import util

def solveEquation(origA,origB,origC):
	'''
	Solve diaphontine equation of form ax - by = c. 
	Assume a and b are co-prime. 
	Return (x,y) tuple where x is +ve
	'''

	#print "Solve %dx - %dy = %d" % (origA,origB,origC)
	a=origA
	b=origB
	sMinus1 = 0
	sMinus2 = 1
	tMinus1 = 1
	tMinus2 = 0

	remainder=1  # set to any non zero value to get loop started
	while (remainder != 0):
		quotient = int(b/a)
		remainder = b % a
		s = sMinus2 + sMinus1*quotient
		t = tMinus2 + tMinus1*quotient

		sMinus2 = sMinus1
		sMinus1 = s
		tMinus2 = tMinus1
		tMinus1 = t
		b = a
		a = remainder

		#print "**",a,b,s,t

	# b contains the gcd 
	gcd = b
	if (gcd != 1): 
		if origC % gcd == 0:
			return solveEquation(origA/gcd, origB/gcd, origC/gcd)
		else: 
			return (None,None)

		
	assert(b == 1)
	assert(s == origA)
	assert(t == origB)
	# tMinus2 and sMinus2 contain the solution for 
	#  ax - by = +/- 1 

	unitX = tMinus2
	unitY = sMinus2
	oneSolution = origA*unitX - origB*unitY
	assert(abs(oneSolution) == 1)
	#print "Unity solution", unitX, unitY, oneSolution

	# We need to scale solution and also adjust depending on if we got + or -1 in previous step
	# To scale we multiply by c
	# Multiply by c to scale solution from 1

	x = unitX*origC*oneSolution
	y = unitY*origC*oneSolution
	#print "solution", x,y, origA*x-origB*y

	#  To get a +ve solution we use the fact that there are multiple solutions of the 
	# form x1 = x + k*b 
	#  So we find k where x1 is the smallest positive number 
	k = x/origB
	x =  x - k*origB
	y = y - k*origA

	#print "      %d*%d - %d*%d = %d, k = %d" % (origA,x,origB,y,origC, -k)

	return (x,y)


def findNBruteForce(p1,p2):
	"Let  n*p2 mod 10**l = p1, where p1 has l digits. Return n "

	# Brute force implementation. Using this for validation

	numDigits = math.ceil(math.log(p1,10))
	modNumber = 10**numDigits

	count=1
	p2Multiple=p2
	while p2Multiple != p1:
		p2Multiple = (p2Multiple + p2) % modNumber
		#print "  ",p2Multiple
		count += 1
		
	return count


def findNFaster(p1,p2):
	"Let  n*p2 mod 10**l = p1, where p1 has l digits. Return n "

	# tenPower is the lowest power of 10 that is greater than p1
	tenPower = 10**int(math.ceil(math.log(p1,10)))

	# n*p2 = m*tenPower + p1   
	# p2*n - m*tenPower = p1   
	#   This is a linear diophantine eqn of form ax+by=c
	#
	(x,y) = solveEquation(p2,tenPower,p1)
	
	return x



#
# Main 
#

'''
# Some test cases since I extended the routine for cases that are not needed for this problem
print solveEquation(7,10,5)
print solveEquation(14,20,10)
print solveEquation(14,20,9)
'''

assert(findNBruteForce(5,7) == findNFaster(5,7))
assert(findNBruteForce(19,23) == findNFaster(19,23))


# It took some trial and error to find +10 to get just one prime over 10**6
primeList = util.PrimeStore(10**6+10).getList()

# Skip first 2 primes viz. (2,3)
primeList = primeList[2:] 

'''
# Test to verify the fsat routine works properly
for i in xrange(1000):
	p1 = primeList[i]
	p2 = primeList[i+1]
	assert(findNFaster(p1,p2) == findNBruteForce(p1,p2))
'''


total = 0
for i in xrange(len(primeList)-1):
	#if i%100 == 0: print "loop at ",i, total
	p1 = primeList[i]
	p2 = primeList[i+1]
	n = findNFaster(p1,p2)
	total += n*p2

print "Answer =",total


