# https://projecteuler.net/problem=171
#

import math


MaxDigits = 20
DigitComboCache = {}
CacheHits = 0
CacheMiss = 0

def findDigitCombinations(digitList):
	global MaxDigits

	#  Initially I thought we would have to treat 0 as special since leading zeros are not allowed.
	#  But we do need to process sequence with leading zeros since that gives us numbers like 1, 25, 442
	#  Set lastDigit to 10 to allow any digit 0-9 to be used to start the number
	#

	# reset cache every invocation, so cache is only helping for nested recursions
	DigitComboCache = {}
	return _findDigitCombinations(digitList,MaxDigits,10)



def _findDigitCombinations(inDigitList, numDigits, lastDigit):
	'''
	digitList specifies how many instances of each digit are present
	numDigits gives the number of digit in final number
	lastDigit tracks what digit was used by parent in recursion chain.. we can't use that 
	   for current digit position

	Returns two tuple (numCombos, comboTotal) where
	   	numCombos is number of unique numbers
	   	comboTotal is sum of all the number
	'''

	global CacheHits, CacheMiss
	global DigitComboCache 

	# Cache lookup needs to be inside recursive routine since the next level
	#   recursion with less than 20 digits also benefits from the lookup
	#
	# We use last digit to ensure we don't double count the case when the previous digit is used again 
	#  if lastDigit=1  then 4,1,... is not the same as 4,1,... as 1 is not allowed to be used in this pass. 
	#  So lastDigit needs to be part of the key for caching
	#

	'''
	if lastDigit == 10: 
		digitList = sorted(inDigitList)
	else:
		lastDigitValue = inDigitList[lastDigit]       # save the value 

		digitList = list(inDigitList)
		del(digitList[lastDigit])
		digitList.sort(reverse=True)         # sorting allows equivalent case to hash to same entry

		digitList.append(lastDigitValue)     # we could have added to the start of list but adding to end  should be 
	 					     #   more efficient. We can adapt by setting lastDigit=9
						     # caching should work as long as lastDigit is always 9 before 
						     #   we do lookup
		assert(len(digitList) == 10)
		lastDigit = 9
	
	'''

	digitListStr = str(digitList) + str(lastDigit)
	if digitListStr in DigitComboCache:
		#print "Cache hit ", DigitComboCache[digitListStr], digitList, digitListStr
		CacheHits += 1
		return DigitComboCache[digitListStr]


	comboTotal = 0
	numCombos = 0
	for digit in range(0,10):
		currDigitCount = digitList[digit]
		if digit == lastDigit or currDigitCount == 0:
			continue

		if currDigitCount == numDigits:  # all other digits have to be this
			assert(comboTotal == 0)
			numCombos = 1
			comboTotal = int(str(digit)*numDigits)   # number of form dddd.. n times 
			break

		assert(currDigitCount < numDigits)
		for digitCount in range(1,currDigitCount+1):
			currentNumMultiple = int(str(digit)*digitCount)   # number of form dddd.. n times 
			digitsLeft = numDigits - digitCount

			digitList[digit] -= digitCount
			nextNumCombos, nextComboTotal = _findDigitCombinations(digitList, digitsLeft, digit)
			digitList[digit] += digitCount

			# Let's say we found x combos in next level. For all those combos, current 
			# digit will be present as leading digit so it would contribute x times its value
			#
			#print "***", digit, currDigitCount, currentNumMultiple, digitsLeft, comboTotal
			comboTotal += nextComboTotal + nextNumCombos * currentNumMultiple * (10**digitsLeft)
			numCombos  += nextNumCombos


	DigitComboCache[digitListStr] = (numCombos, comboTotal)
	CacheMiss += 1
	#print "Cache miss ", DigitComboCache[digitListStr], digitList, digitListStr

	return DigitComboCache[digitListStr]


	

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

	# terminating condition for recursion
	if numDigits == 0 or digit == 9: 
		digitList[9] = numDigits    # If the current digit is <9, numDigit will be 0 so this would be a no-op
		funcValue += numDigits*9*9

		# We have now set number of instance for each digit to use
		#
		root = math.sqrt(funcValue)
		if root == int(root):
			counter += 1
			#if counter % 100 ==0:
				#print counter
				#print "Cache miss = %d hits = %d  hit %% = %.2f size = %d"  % (CacheMiss, CacheHits, 100*CacheHits/(CacheHits+CacheMiss), len(DigitComboCache))

			#combos = findDigitCombinations(digitList)
			numCombos, comboTotal = findDigitCombinations(digitList)

			print "%10d %4d " % (numCombos, comboTotal), digitList
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

# answers that didn't work
# 384260908
# 55150845
# 230537404
# 638417039
# 802085511
# 544283400

MaxDigits = 3

answer = findDigitSets(digitList, MaxDigits)
print "Cache miss = %d hits = %d  hit %% = %.2f"  % (CacheMiss, CacheHits, 100*CacheHits/(CacheHits+CacheMiss))


print "Answer for ", MaxDigits, " = ", answer, answer%10**9

