
# https://projecteuler.net/problem=9
#
# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 


SUM = 1000

# Assume a is the smallest side always. So the max possible size for a is SUM/3

for a in range(1,int(SUM/3)):
        for b in range(a+1, int((SUM-a)/2)):
                c = SUM - a - b
                if (a*a + b*b == c*c) : 
                        print "match found ",a,b,c
                        print "product ", a*b*c

