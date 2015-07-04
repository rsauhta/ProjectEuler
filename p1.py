
# https://projecteuler.net/problem=1
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#

MaxNumber = 1000

FactorsOf3 = 3
FactorsOf5 = 5
currentValue = 1
SumOfMultiples = 0

while 1: 
        if (currentValue == FactorsOf3):
                FactorsOf3 += 3
        if (currentValue == FactorsOf5):
                FactorsOf5 += 5

        currentValue = min(FactorsOf3, FactorsOf5)
        if (currentValue >= MaxNumber) : 
                break
        SumOfMultiples += currentValue

print "Sum = ", SumOfMultiples

