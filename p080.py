# https://projecteuler.net/problem=80
# Square root digital expansion
#
import math
from decimal import *

getcontext().prec = 110  # Set decimal to use precision a bit high to avoid roudning errors

total = 0
for i in range(1,101): 
#for i in range(1,3): 
        root = math.sqrt(i)
        if int(root)== root:  # perfect square
                continue

        root = Decimal(i).sqrt()
        rootStr = str(root)
        dotIndex = rootStr.index(".")+1
        digitSum = 0

        for digit in rootStr[:101]:
                if digit != ".":
                        digitSum += int(digit)
        #print i, digitSum
        total += digitSum

print total
# tried
#   40887 : 

