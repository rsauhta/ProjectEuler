# https://projecteuler.net/problem=131
# Prime cube partnership

import util


'''
n^3 - n^2p = n^2(n-p). Only way this is a cube is:
1. n-p is a multiple of n => p is a multiple of n, but p is a prime
2. n is a cube and n-p is also a cube. 
    => x^3 - p = y^3   where n=x^3
    => p = x^3-y^3 = (x-y)(...)
    since p is a prime x-y must be 1. 
So we are looking for two consequetive numbers where x^3-y^3 is a prime
'''

MaxN = 10**6
primeStore = util.PrimeStore(MaxN)

cube=1
count=0

while 1:
	primeCandidate = (cube+1)**3 - cube**3
	if primeCandidate > MaxN:
		break

	if primeStore.isPrime(primeCandidate):
		count+=1
	cube +=1
	if cube % 1000 ==0:
		print cube

print count


