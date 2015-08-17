# https://projecteuler.net/problem=323
# Bitwise-OR operations on random integers
#

from decimal import *

# For nth iteration : 
#  probability of a bit being 0 = (1/2)**n  viz. bit was 0 n times. 
#  probability of all bits being 1 = (1-(1/2)**n) ** 32
# 
# After 1st iteration: Prob of all 1s = (1-1/2)**32
# After 2nd iteration: Prob of all 1s = (1-(1/2)**2) ** 32
#   However this includes probability for both 1st or 2nd iteration =  
#     probaility of all 1st in 2nd iteration = Prob of all 1s by 2nd iteraion - Prob of all 1s in 1st iteration

#


def getAnswer():

	expectedLength = 0

	cummProbOf1sInPrevIters = 0  # cummulative probability of getting all 1s in any of earlier iteration
	probOfBitBeing0 = 1

	for i in range(1,50): 
		probOfBitBeing0 *= 0.5

		probOfBitBeing1 = 1 - probOfBitBeing0
		probOfAllBitsBeing1 = probOfBitBeing1**32

		probOfAll1_ThisIter = probOfAllBitsBeing1 - cummProbOf1sInPrevIters   
		cummProbOf1sInPrevIters = probOfAllBitsBeing1 

		expectedLength += i * probOfAll1_ThisIter 

		#print i, expectedLength, probOfAll1_ThisIter, cummProbOf1sInPrevIters 

	return expectedLength



# My answer kept getting rejected so I thought native floating point may not have sufficient precision
# I wrote this routine to use higher precision floating point numbers from Python. 
# However the error turned out to be a silly one; I was using range(50) instead of range(1,50), causing answer to be off by 1 
#   Keeping this routine as a reference on using Decimal
def getAnswerDec():
	expectedLength = Decimal(0)

	cummProbOf1sInPrevIters = Decimal(0)  # cummulative probability of getting all 1s in any of earlier iteration
	probOfBitBeing0 = Decimal(1.0)

	for i in range(1,50): 
		probOfBitBeing0 *= Decimal(0.5)    # = .5 ** i. We compute this incrementally. 

		probOfBitBeing1 = Decimal(1) - probOfBitBeing0
		probOfAllBitsBeing1 = probOfBitBeing1**32

		probOfAll1_ThisIter = probOfAllBitsBeing1 - cummProbOf1sInPrevIters   
		cummProbOf1sInPrevIters = probOfAllBitsBeing1 

		expectedLength += Decimal(i) * probOfAll1_ThisIter 
		#print i, expectedLength, probOfAll1_ThisIter, probOfAllBitsBeing1, probOfBitBeing0

	return expectedLength



answer = getAnswer()
print round(answer,10)


