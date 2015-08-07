# https://projecteuler.net/problem=70
# Totient permutation
#
import math
import util
import timeit

def phi(n):
	"Returns totient function for given n"

	util.FindFactor(n)
	return 1


def divisorCount(n):
	count=0
	root = math.sqrt(n)
	for i in range(2,1+int(root)):
		if (n % i == 0):      # found a divisor
			count += 2  

	if root == int(root):   # perfect square
		count -= 1
	return count

def divisorCount2(n):
	count=1
	factorDict = util.FindFactor(n)
	print factorDict
	for primePower in factorDict.values():
		count = count*(primePower+1)

	return count-2  # since we counted 1 and n also as divisors


def div2(n):
	count = 0
	for i in range(1,n):
		count += divisorCount2(i)
	return count

def div1(n):
	count = 0
	for i in range(1,n):
		count += divisorCount(i)
	return count

MaxN = 10**7
util.PopulatePrimeList(int(math.sqrt(MaxN)))

#print divisorCount(9), divisorCount2(9)
#print divisorCount(144), divisorCount2(144)
#assert(div1(87109) == div2(87109))
print divisorCount2(87109)

#print timeit.timeit('div1(1000000)', number=1, setup='from __main__ import div1')
#print timeit.timeit('div2(10000000)', number=1, setup='from __main__ import div2')


#util.PopulatePrimeList(MaxN)

#print phi(87109)

