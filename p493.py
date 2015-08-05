# https://projecteuler.net/problem=493
#
import math

Factorial= [1]

fact = 1
for i in range(1,71):
        fact *= i
        Factorial.append(fact)


# Assume each ball is numbered uniquely. We will try to find out the various combinations
#
# Total combinations to pick 20 balls from 70 = 70!/(70-20)!20!
# 
# We will now try to estimate ways to pick exactly "n" unqiue colors
#  Ways to pick "n" color buckets out 7 : 7!/(7-n)!n!
#  For the selected color buckets, we need to figure out number of combinations to pick 20 balls
#    First pick one ball from each color bucket: 10^n  
#    Now there are 9*n balls left and we need to pick 20-n more balls:
#        (9n)!/(9n-(20-n))!(20-n)!  = (9n)!/(10n-20)!(20-n)! 
#


def getCombosForNColors(n):
        global Factorial

        colorPickCombos = Factorial[7]/(Factorial[7-n]*Factorial[n])
        pickOneBallEach = int(math.pow(10,n))
        ballPickCombos  = Factorial[9*n]/(Factorial[10*n-20]*Factorial[20-n])

        print colorPickCombos,pickOneBallEach,ballPickCombos  
        return colorPickCombos*pickOneBallEach*ballPickCombos  


        
print Factorial[70]/(Factorial[50]*Factorial[20])

sum=0
for i in range(2,8): 
        print i, "=", getCombosForNColors(i)
        sum += getCombosForNColors(i)
print sum


