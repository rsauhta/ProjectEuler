# https://projecteuler.net/problem=7
#

# Summation of p
# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#  we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?rimes
#

import util
import math


NUM = 10001

primeList = util.GetFirstNPrime(NUM)

print NUM, " prime is ", primeList[-1]


