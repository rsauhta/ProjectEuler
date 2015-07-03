# https://projecteuler.net/problem=495
#
# Writing n as the product of k distinct positive integers Problem 495 Let
# W(n,k) be the number of ways in which n can be written as the product of k
# distinct positive integers.
# 
# For example, W(144,4) = 7. There are 7 ways in which 144 can be written as a
# product of 4 distinct positive integers:
#
# 144 = 1x2x4x18
# 144 = 1x2x8x9 
# 144 = 1x2x3x24 
# 144 = 1x2x6x12 
# 144 = 1x3x4x12 
# 144 = 1x3x6x8 
# 144 = 2x3x4x6 
# Note that permutations of the integers themselves are not considered distinct.
# 
# Furthermore, W(100!,10) modulo 1 000 000 007 = 287549200.
# 
# Find W(10000!,30) modulo 1 000 000 007.
# 


# Given numSlots find combinations of arranging different integers; explained below using color balls
# each slot takes only one balls. we can use 1 color or N colors. 
# However 3 red,1 black (BBBR) is same as 3 black, 1 red (RBBB). 
# As an example for 4 slots combinations are: 
#  AAAA, AAAB, AABB, AABC, ABCD
# we will be storing combos in a different form
#  [4,0,0,0]  [3,1,0,0] [2,2,0,0] [2,1,1,0] [1,1,1,1]
#  viz. each number represents a different color ball. In example above there we will use at most 4 
#    different colors. So we have a bucker for each color and combo is represneted by how many balls 
#    of a color are being used. 
#

GlobalCount = 0

def findCombos(numBalls, numSlots) : 
        global GlobalCount
        GlobalCount = 0
        comboList = []
        workingList=[0] * numSlots 
        findComboHelper(comboList, workingList, numSlots-1, 0, numBalls, numBalls)
        #print workingList
        return comboList

def findComboHelper(comboList, workList, maxSlot, currentSlot, totalLeft, maxAllowed):
        global GlobalCount
        #print " here ..", workList, maxSlot, currentSlot, totalLeft, maxAllowed

        # early terminating condition for optimization
        if maxAllowed == 0 and totalLeft > 0 : 
                return
        if maxAllowed != 0  and totalLeft/maxAllowed > (maxSlot - currentSlot) : 
                return

        # terminating condition for recursion. We are beyond the last slot
        if (currentSlot > maxSlot):
                if (totalLeft == 0): 
                        #print workList
                        #comboList.append(workList) 
                        GlobalCount += 1 
                return

        # Figure out all possible values to use for the current slot
        for value in xrange(0, maxAllowed+1) : 
                if value > totalLeft: 
                        break
                workList[currentSlot] = value
                findComboHelper(comboList, workList, maxSlot, currentSlot+1, totalLeft - value, value)

        
def main():
        global GlobalCount
        #print " 10,10 => %5d " % len(findCombos(10,10))
        #print " 30,30 => %5d " % len(findCombos(30,30))
        findCombos(10,10)
        print "count = ", GlobalCount 
        findCombos(31,31)
        print "count = ", GlobalCount 
        findCombos(100,10)
        print "count = ", GlobalCount 

import timeit        

print timeit.timeit(main, number=1)


