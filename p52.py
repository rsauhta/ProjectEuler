
# https://projecteuler.net/problem=52
# Permuted multiples
# Problem 52
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.
# 

# re-arrange number so digits are sorted.
#  e.g. 1290501 would return 11259  
def getUniqueNum (number) :
        return int(''.join(sorted(str(number))))

number = 2

while 1:
        signature = getUniqueNum(number)
        if (signature == getUniqueNum(number*2)) and  \
           (signature == getUniqueNum(number*3)) and  \
           (signature == getUniqueNum(number*4)) and  \
           (signature == getUniqueNum(number*5)) and  \
           (signature == getUniqueNum(number*6)) : 
           print "found it ", number
           break

        number += 1


