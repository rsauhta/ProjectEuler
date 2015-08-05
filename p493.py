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
# We will now try to estimate ways to pick exactly "n" unqiue colors, with 20 picks from 70
#  Ways to pick "n" color buckets out 7 : 7!/(7-n)!n!
#  For the selected color buckets, we need to figure out number of combinations to pick 20 balls
#    To pick n colors from 10*n balls, we can use induction: 
#    answer = total combos - ways to pick n-1,n-2...2 color from in 20 picks 10*n balls
#   
#   This would ultimately come down to picking 2 colors in 20 picks from 20 balls which is 1.
#   
#    
#

def getCombosForNColors(n, total):
        'Combos to pick "n" colors out of "total" colors in 20 picks, where each color has 10 balls'

        global Factorial

        numBalls = total*10
        pickBalls = 20

        if (numBalls == pickBalls):
                return 1

        assert(pickBalls < numBalls)

        # ways to pick "n" color buckets out of "total" color buckets
        colorPickCombos = Factorial[total]/(Factorial[total-n]*Factorial[n])

        # we have reduced the number of balls to "n" color buckets
        ballSet = n*10
        # number of combos to pick 20 balls out of the reduced ball set
        totalCombos = Factorial[ballSet]/(Factorial[ballSet-pickBalls]*Factorial[pickBalls])

        # We need to subtract cases of picking up less than "n" colors 
        minusTotal = 0
        for i in range(2,n): 
                # we have reduced the color choice to "n" buckets so set second param to n
                minusTotal += getCombosForNColors(i,n)    

        #print n, total, colorPickCombos,totalCombos,minusTotal
        return colorPickCombos*(totalCombos - minusTotal)


        
totalCombos=0
weightedSum = 0
for i in range(2,8): 
        combos = getCombosForNColors(i,7)
        #print i, "=", combos
        weightedSum +=  i*combos
        totalCombos += combos

assert(totalCombos == Factorial[70]/(Factorial[50]*Factorial[20]))

expectedNum = float(weightedSum)/ totalCombos
print float(int(expectedNum*10**9)) /10**9


