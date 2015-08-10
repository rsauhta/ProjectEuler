# https://projecteuler.net/problem=171
#

import math


MaxDigits = 20
#MaxDigits = 5


FactorialDict = None 
def factorial(n):
	global FactorialDict 

	if FactorialDict == None:
		# First time initialization
		FactorialDict = []
		FactorialDict.append(1)
		fact = 1
		for i in range(1,MaxDigits+1):
			fact *= i
			FactorialDict.append(fact)

	return FactorialDict[n]


RepUnit = int("1"*MaxDigits)

def findDigitCombo(digitList):
	divisor = 1
	for count in digitList:
		divisor *= factorial(count)

	comboSum = 0
	for i in range(1,10):
		comboSum += i*digitList[i]

	numCombos =  factorial(MaxDigits)/divisor
	comboTotal = numCombos * RepUnit * comboSum  / MaxDigits
	return numCombos, comboTotal



counter = 0

def findDigitSets(digitList, numDigits, digit=0, funcValue=0):
	'''
	Try different sets of digits that match condition
	digitList = indicates the number of instances of particular digit 
	numDigits = number of digits that need to be allocated 
	digit     = digit being processed now. This would increase from 0 to 9 as we recurse deeper
	funcValue = track the function value so far
	'''

	global counter
	global CacheHits, CacheMiss
	global RecurseCacheHits, RecurseCacheMiss

	# terminating condition for recursion
	if numDigits == 0 or digit == 9: 
		digitList[9] = numDigits    # If the current digit is <9, numDigit will be 0 so this would be a no-op
		funcValue += numDigits*9*9

		# We have now set number of instance for each digit to use
		#
		root = math.sqrt(funcValue)
		if root == int(root):
			counter += 1
			if counter % 1000 ==0:
				print counter

			numCombos, comboTotal = findDigitCombo(digitList)
			return comboTotal
		else:
			return 0

	# Process this digit and then recurse deeper
	total=0
	square = digit*digit
	for pos in range(0,numDigits+1): 
		# We will use "pos" instance of current digit
		digitList[digit] = pos
		total += findDigitSets(digitList,numDigits-pos,digit+1,funcValue+pos*square)

	digitList[digit] = 0  # Reset the current digit to 0 before returning
		
	return total



digitList = [0 for i in range(0,10)]

answer = findDigitSets(digitList, MaxDigits)


print
print "Answer for", MaxDigits, " digits = ", answer%10**9

