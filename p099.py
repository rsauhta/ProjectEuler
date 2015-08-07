# https://projecteuler.net/problem=99
# Largest exponential
#

import math

# Instead of computing a**b, we will compute b*log(a)
#

largestValue=0.0
largestLineNumber=0

lineNumber=0
with open("p099_base_exp.txt") as f:
        for line in f: 
                lineNumber += 1
                base,exp = line.strip().split(",")
                value = int(exp) * math.log(int(base))
                if value > largestValue: 
                        largestValue = value
                        largestLineNumber = lineNumber

print "Largest value at line:", largestLineNumber
