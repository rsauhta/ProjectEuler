# https://projecteuler.net/problem=171
#

import math

counter = 0

DigitComboCache = {}

def findDigitCombinations(digitList, numDigits=20, lastDigit=10):
	return _findDigitCombinations(sorted(digitList), numDigits, lastDigit)

def _findDigitCombinations(digitList, numDigits=20, lastDigit=10):
	'''
	digitList specifies how many instances of each digit are present
	numDigits gives the number of digit in final number

	Return value is the number of unique numbers that can be formed
	'''

	digitListStr = str(digitList)
	if digitListStr in DigitComboCache:
		return DigitComboCache[digitListStr]

	comboTotal = 0
	for digit in range(0,10):
		currDigitCount = digitList[digit]
		if digit == lastDigit or currDigitCount == 0:
			continue
		if currDigitCount == numDigits:  # all other digits have to be this
			return 1

		for digitCount in range(1,currDigitCount+1):
			if digitCount > numDigits:
				break
			digitList[digit] -= digitCount
			comboTotal += findDigitCombinations(digitList,numDigits-digitCount, digit)
			digitList[digit] += digitCount

	DigitComboCache[digitListStr] = comboTotal
	return comboTotal


	



def findDigitSets(digitList, numDigits, digit=0):
	'''
	Try different sets of digits that match condition
	digitList = indicates the number of instances of particular digit 
	numDigits = number of digits that need to be allocated 
	digit     = digit being processed now. This would increase from 0 to 9 as we recurse deeper
	'''

	global counter

	if numDigits == 0 or digit == 9: 
		digitList[9] = numDigits    # If the current digit is <9, numDigit will be 0 so this would be a no-op

		# We have figured out the number of each unit to use
		func = 0
		for i in range(0,10):
			func += i*i*digitList[i]
		root = math.sqrt(func)
		if root == int(root):
			#print func
			counter += 1
			if counter % 100 ==0:
				print counter
			return findDigitCombinations(digitList)
			#return 0
		else:
			return 0

	total=0
	for pos in range(0,numDigits+1): 
		# We will use "pos" instance of current digit
		digitList[digit] = pos
		total += findDigitSets(digitList,numDigits-pos,digit+1)
		total = total % 10**9
		
	return total



#digitDict = dict((i,0) for i in range(0,10))
digitList = [i for i in range(0,10)]


answer = findDigitSets(digitList, 20)
print 
print "Answer = ", answer

