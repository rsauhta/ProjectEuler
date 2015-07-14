# https://projecteuler.net/problem=20
#
#

import util
import math


factorial = 1
for i in range(1,101):
	factorial *= i 

print "factorial = ", factorial

sum=0
while (factorial): 
	sum += factorial % 10
	factorial = int(factorial / 10)

print sum
