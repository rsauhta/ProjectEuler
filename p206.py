# https://projecteuler.net/problem=206
#

import math
import re

pattern     = '1.2.3.4.5.6.7.8.9'
smallestNum =  10203040506070809
largestNum  =  19293949596979899

start = int(math.sqrt(smallestNum))
end   = int(math.sqrt(largestNum))

prog = re.compile(pattern)

for i in range(start, end+1):
	 num = i*i
	 if (prog.match(str(num))): 
	 	print "matched :",i*10 ,i*i*100
	 	


