# https://projecteuler.net/problem=48
#

import math

last10 = 10000000000

a = 12345678901234567890

sum=0
for i in range (1,1001):
	term=1
	for k in range(0,i):
		term = term*i % last10
	sum = (sum + term) % last10

print sum % last10

