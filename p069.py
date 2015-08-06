# https://projecteuler.net/problem=69
# Totient Maximum
#

import util

#
#   To minimize relatively prime numbers, make this number be product of as many primes as possible. 
#   Not sure if this leads to answer always but it is worthy of a try

MaxN = 1000000
primeList = util.GetPrimeList(1000)  # These many primes should be enough to get product over 1 million

product = 1
for prime in primeList:
        if product*prime > MaxN:
                break
        product = product*prime

print product



