# https://projecteuler.net/problem=206
#

import math
import re

# Last unknown digit is going to be 0, so skip that during lookup. We will use 
#   the first 17 digit to keep the computations small
# Second last digit would be 3 or 7 to get 9 as last digit in square. We can 
#   speed up lookup by checking only numbers ending in 3 or 7 
#

pattern     = '1.2.3.4.5.6.7.8.9'
smallestNum =  10203040506070809
largestNum  =  19293949596979899

start = int(math.sqrt(smallestNum))
end   = int(math.sqrt(largestNum))

while (1):
	lastDigit = start % 10
	if (lastDigit == 3 or lastDigit == 7):
		break
	start += 1

prog = re.compile(pattern)

i = start
#for i in range(start, end+1):
while (i <= end): 
	num = i*i
	if (prog.match(str(num))): 
		print "matched :",i*10 ,i*i*100
	lastDigit = i % 10
	if (lastDigit == 3):
		i += 4
	if (lastDigit == 7):
		i += 6



