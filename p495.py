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


'''
Consider a number = 2^4 * 3^2
First figure out different ways of spreading 2^4 into 4 buckets
   1,1,1,16  1,1,2,8 1,1,4,4 1,2,2,4 2,2,2,2   
We can classify these combination into catergories: 
   Three 1s      :  1 (1,1,1,16)
   Two 1s        :  1 (1,1,2,8)
   Two 1s,double :  1 (1,1,4,4)
   One 1,double  :  1 (1,2,2,4)
   Quad          :  1 (2,2,2,2)

Note we can get unique combination by iterating and keeping bucket n+1 <= bucket n
In the above combinations, none of the solutions are unique but we can get unique combos by 
adding 3s as factors. 
For 3, we get the following combinations 
   1,1,1,9  1,1,3,3 
We can classify combinations as
   Three 1s       :  1 (1,1,1,9)
   Two 1s, double :  1 (1,1,3,3)

We multiply the two sets to get the next set. 
   One1Unique : 6 (1,2,8,9                Two1s * Three1s
	 	   1,2,8*3,3 1,2*3,8,3    Two1s * Two1sDouble * 2
                   1,4,4*3,3              Two1sDouble * Two1sDouble
		   1,2,2*9,4              One1Double * Three1s
		   1,2,2*3,4*3            One1Double * Two1sDouble
   No1Unique  : 1 (3,2,2*3,4)             One1Double * Two1sDouble
                  
we can also track the other combinations : 
   Three 1s     : 1 (1,1,1,6*9)   Three 1s x Three 1s
   etc.

We can keep adding further prime factor and their powers and keep track of all combinations
At the end count of One1Unique and No1Unique is the answer. 
We can track categories instead of actual numbers since the numbers we are multiplying in each 
stage are primes. 1,1,8,9 and 1,1,4,18 are equivalent when we trying to multiply a prime other
that 2 or 3 e.g. 5. 1 is a special case causing the number of categories to go up but  I can
figure out how to avoid that :-(
'''

import util

# We will track 
class Category:
	Four1            = 0
	Three1           = 1
	Two1_Unique      = 2
	Two1_Double      = 3
	One1_Unique      = 4
	One1_Double      = 5
	One1_Triple      = 6
	No1_Unique       = 7
	No1_Double       = 8
	No1_DoubleDouble = 9
	No1_Triple       = 10
	No1_Quad         = 11
	Max              = 12


# To generate a test tuple, use a different prime for each row and 
#   raise to the power specified
TestTupleSeed = [
	(0,0,0,0),    # Four1            = 0
	(0,0,0,1),    # Three1           = 1
	(0,0,1,2),    # Two1_Unique      = 2
	(0,0,1,1),    # Two1_Double      = 3
	(0,1,2,3),    # One1_Unique      = 4
	(0,1,2,2),    # One1_Double      = 5
	(0,1,1,1),    # One1_Triple      = 6
	(1,2,3,4),    # No1_Unique       = 7
	(1,2,3,3),    # No1_Double       = 8
	(1,1,2,2),    # No1_DoubleDouble = 9
	(1,2,2,2),    # No1_Triple       = 10
	(1,1,1,1)     # No1_Quad         = 11
]

def generateTestTuple(primeList):
	"Use the primes from the list passed in to generate test tuples"
	global TestTupleSeed

	assert(len(primeList) == len(TestTupleSeed))
	tupleList = []

	for i in range(len(TestTupleSeed)):
		testTuple = (primeList[i]**TestTupleSeed[i][0],  \
		             primeList[i]**TestTupleSeed[i][1],  \
		             primeList[i]**TestTupleSeed[i][2],  \
		             primeList[i]**TestTupleSeed[i][3])
		#print i, primeList[i], TestTupleSeed[i], testTuple
		tupleList.append(testTuple)
	return tupleList



# Helper methods to test out combination maping 
#
def classify(fourTuple):
	"Given a 4 tuples, return the category it falls into"

	sortedTuple = sorted(fourTuple)

	if sortedTuple[0] == 1:
		if sortedTuple[1] == 1: 
			if sortedTuple[2] == 1: 
				if sortedTuple[3] == 1: 
					return Category.Four1
				else:
					return Category.Three1
			else: 
				if sortedTuple[2] == sortedTuple[3]:
					return Category.Two1_Double
				else:
					return Category.Two1_Unique
		else:
			if sortedTuple[1] == sortedTuple[2] == sortedTuple[3]:
				return Category.One1_Triple

			if sortedTuple[1] == sortedTuple[2] or \
			   sortedTuple[2] == sortedTuple[3]:
			   	return Category.One1_Double
			
			return Category.One1_Unique
	else: 
		if sortedTuple[0] == sortedTuple[1] == sortedTuple[2] ==sortedTuple[3]:
			return Category.No1_Quad

		if sortedTuple[0] == sortedTuple[1] == sortedTuple[2] or \
		   sortedTuple[3] == sortedTuple[1] == sortedTuple[2]:
			return Category.No1_Triple

		if sortedTuple[0] == sortedTuple[1] and \
		   sortedTuple[2] == sortedTuple[3]:
			return Category.No1_DoubleDouble

		if sortedTuple[0] == sortedTuple[1] or \
		   sortedTuple[1] == sortedTuple[2] or \
		   sortedTuple[2] == sortedTuple[3]:
			return Category.No1_Double

		if sortedTuple[0] != sortedTuple[1] and \
		   sortedTuple[1] != sortedTuple[2] and \
		   sortedTuple[2] != sortedTuple[3]:
			return Category.No1_Unique

	#print sortedTuple
	assert(False)   # should never reach here



def classifyList(tupleList, printFlag=True):
	"Takes a list of tuples. Eliminates any duplicates. Classify each of them using classify() and return an array with total for each category"

	categoryList = [0 for i in range(Category.Max)]
	tupleDict = {}

	for pTuple in tupleList:
		sortedTuple = sorted(pTuple)
		tupleStr = str(sortedTuple)
		if tupleStr in tupleDict:
			if printFlag:
				print pTuple, "duplicate of",sortedTuple
			continue
		else:
			tupleDict[tupleStr] = 1

		category = classify(sortedTuple)
		if printFlag:
			print pTuple, category
		categoryList[category] += 1
	
	return categoryList

def multiplyTuples(tuple1, tuple2):
	"Multiply 2 tuples and get all combinations"  

	# Brain dead implemenation 
	tupleList = []
	for i0 in range(4):
		for i1 in range(4):
			if i0 == i1: continue
			for i2 in range(4):
				if i2 == i0 or i2 == i1: continue
				for i3 in range(4):
					if i3 == i0 or i3 == i1 or i3 == i2: continue
					newTuple = (tuple1[0]*tuple2[i0],
					            tuple1[1]*tuple2[i1],
					            tuple1[2]*tuple2[i2],
					            tuple1[3]*tuple2[i3])
					tupleList.append(newTuple)
	return tupleList


def generateMultiplyMatrix():
	primeList = util.GetPrimeList(100)
	testList1 = generateTestTuple(primeList[:12])
	testList2 = generateTestTuple(primeList[12:24])

	assert(len(testList1) == len(testList1) == Category.Max)

	# To find out what you get by multiplying Category.X with Category.Y
	#  look up matrix[X][Y] 
	matrix = [ [None for i in range(Category.Max)] for j in range(Category.Max)]

	for cat1 in range(Category.Max):
		for cat2 in range(Category.Max):
			matrix[cat1][cat2] = classifyList(multiplyTuples(testList1[cat1],testList2[cat2]),False)
			if matrix[cat2][cat1] != None:
				assert(matrix[cat2][cat1] == matrix[cat1][cat2])
	return matrix

def printMultiplyMatrix(matrix):
	for cat1 in range(Category.Max):
		print "Category", cat1
		for cat2 in range(cat1+1):
			print "      ",cat2, "=",matrix[cat1][cat2]


CategoryMultiplyMatrix = generateMultiplyMatrix()
printMultiplyMatrix(CategoryMultiplyMatrix)


#tupleList = classifyList(multiplyTuples(testList1[0], testList2[0]))
#print testList1[0], testList2[0], '=',tupleList
#tupleList = classifyList(multiplyTuples(testList1[3], testList2[3]))
#print testList1[3], testList2[3], '=',tupleList




# =========================
# test and old code below 
# =========================

'''
# Verified that multiply works properly by looking at the output of the following code
tupleList = multiplyTuples([1,2,4,8], [3,9,27,81])
for i in range(len(tupleList)):
	print i, tupleList[i]
categoryList = classifyList(tupleList)
print categoryList
print sum(categoryList)
'''

# List of unique combos of each category above
#  Use a different prime in each category 
TestTupleList = [
	(1  ,1     ,1     ,1    ),    # Four1            = 0
	(1  ,1     ,1     ,2    ),    # Three1           = 1
	(1  ,1     ,3     ,3**2 ),    # Two1_Unique      = 2
	(1  ,1     ,5     ,5    ),    # Two1_Double      = 3
	(1  ,7     ,7**2  ,7**3 ),    # One1_Unique      = 4
	(1  ,11    ,11**2 ,11**2),    # One1_Double      = 5
	(1  ,13    ,13    ,13   ),    # One1_Triple      = 6
	(17 ,17**2 ,17**3 ,17**4),    # No1_Unique       = 7
	(19 ,19**2 ,19**3 ,19**3),    # No1_Double       = 8
	(23 ,23    ,23**2 ,23**2),    # No1_DoubleDouble = 9
	(29 ,29**2 ,29**2 ,29**2),    # No1_Triple       = 10
	(31 ,31    ,31    ,31   )     # No1_Quad         = 11
]



def test_genCombo(prime):
	" test routine to blindly generate 4 tuple combos"
	factorList = [prime**i for i in range(5)]

	tupleList = []
	for factor1 in  factorList: 
		for factor2 in  factorList: 
			for factor3 in  factorList: 
				for factor4 in  factorList: 
					primeTuple = (factor1,factor2,factor3,factor4) 
					#print primeTuple, classify(primeTuple)
					tupleList.append(primeTuple)
	return tupleList



'''
# Tested classifyList with following snippet and analysis
categoryList = classifyList(test_genCombo(2))
print "category list =", categoryList
print "sum = ", sum(categoryList)
#
#  classifyList eliminated 555 duplicates out of 625 blind combos
#    manually verified that indeed 70 (625-555) is the # of unique combos
#    There was only 1 case of all unique, no 1 : as expected
#    Verified a few other cases
'''

'''
# Tested TestTupleList with the following code to verify that we did generate all combos
#  Look at console output to spot check few cases
assert(len(TestTupleList) == Category.Max)
for i in range(Category.Max):
	cat = classify(TestTupleList[i])
	print cat, TestTupleList[i]
	assert(cat == i)

primeList = util.GetPrimeList(100)
testList1 = generateTestTuple(primeList[:12])
testList2 = generateTestTuple(primeList[12:24])
print testList1
print testList2
for i in range(Category.Max):
	cat1 = classify(testList1[i])
	cat2 = classify(testList2[i])
	print cat1, testList1[i], testList2[i]
	assert(cat1 == cat2 == i)

'''

# old code. park for now
'''
#
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
'''

#Not solved yet... work in progress
