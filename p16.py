# https://projecteuler.net/problem=16
#

import math

num = int(math.pow(2,1000))    # 2 raised to 1000

sum = 0
for digit in str(num):
	sum += int(digit)

print sum

