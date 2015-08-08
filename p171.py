# https://projecteuler.net/problem=171
#

import math


MaxDigits = 20
DigitComboCache = {}

def findDigitCombinations(digitList):
	global MaxDigits
	global DigitComboCache 

	# sorting digitList is a critical piece 
	#    Number of combos for 18 8s + 2 9s = combos for 2 2s +  18 7s
	#    By sorting both of above case would become 18,2,0,0...
	#  However we have to treat 0 as special since leading zeros are not allowed
	#   One way we handle this is by setting lastDigit to 0 ensuring that first digit will 
	#   not be 0; however this leads to different number of combos for cases that have zero
	# 
	#return _findDigitCombinations(sorted(digitList),MaxDigits,0)

	newDigitList = list(digitList)
	newDigitList[1:] = sorted(newDigitList[1:])

	return _findDigitCombinations(newDigitList,MaxDigits,0)



def _findDigitCombinations(digitList, numDigits, lastDigit):
	'''
	digitList specifies how many instances of each digit are present
	numDigits gives the number of digit in final number

	Return value is the number of unique numbers that can be formed
	'''

	# Cache lookup needs to be inside recursive routine since the next level
	#   recursion with less than 20 digits also benefits from the lookup
	#
	digitListStr = str(digitList)
	if digitListStr in DigitComboCache:
		print "Cache hit ", DigitComboCache[digitListStr], digitList, digitListStr
		return DigitComboCache[digitListStr]

		
	comboTotal = 0
	for digit in range(0,10):
		currDigitCount = digitList[digit]
		if digit == lastDigit or currDigitCount == 0:
			continue
		if currDigitCount == numDigits:  # all other digits have to be this
			assert(comboTotal == 0)
			comboTotal=1
			break

		for digitCount in range(1,currDigitCount+1):
			if digitCount > numDigits:
				break
			digitList[digit] -= digitCount
			comboTotal += _findDigitCombinations(digitList,numDigits-digitCount, digit)
			digitList[digit] += digitCount


	DigitComboCache[digitListStr] = comboTotal
	print "Cache miss ", DigitComboCache[digitListStr], digitList, digitListStr
	return comboTotal


	

counter = 0
funcDict = {}


SquareDict = {}
for i in range(0,41):
	SquareDict[i*i]=1

def findDigitSets(digitList, numDigits, digit=0, funcValue=0):
	'''
	Try different sets of digits that match condition
	digitList = indicates the number of instances of particular digit 
	numDigits = number of digits that need to be allocated 
	digit     = digit being processed now. This would increase from 0 to 9 as we recurse deeper
	funcValue = track the function value so far
	'''

	global counter
	global SquareDict

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

			combos = findDigitCombinations(digitList)
			digitSum=0
			for i in range(0,10):
				if digitList[i]: 
					digitSum += i
			print combos,digitSum, digitList
			return digitSum*combos
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

# answers that didn't work
# 384260908
# 55150845
# 230537404
# 638417039

#answer = findDigitSets(digitList, 20)
MaxDigits = 2
answer = findDigitSets(digitList, MaxDigits)

print "Answer = ", answer, answer%10**9

