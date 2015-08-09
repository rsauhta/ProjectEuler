# https://projecteuler.net/problem=171
#

import math


MaxDigits = 20
DigitComboCache = {}
DigitComboDictCache = {}
CacheHits = 0
CacheMiss = 0

def findDigitCombinations(digitList):
	global MaxDigits

	#  Initially I thought we would have to treat 0 as special since leading zeros are not allowed.
	#  But we do need to process sequence with leading zeros since that gives us numbers like 1, 25, 442
	#  Set lastDigit to 10 to allow any digit 0-9 to be used to start the number
	#

	sortedDigitList = sorted(digitList)
	digitListStr = str(sortedDigitList)

	if digitListStr in DigitComboDictCache:
		numCombos, digitDict = DigitComboDictCache[digitListStr]
		#print "Cache hit ", digitDict 
	else: 
		numCombos, multipleList = _findDigitCombinations(sortedDigitList,MaxDigits,10)
		#print "===", numCombos, multipleList, sortedDigitList 
		digitDict = {}
		for i in range(0,10):
			digitInstance = sortedDigitList[i]
			if digitInstance in digitDict:
				assert(multipleList[i] == digitDict[digitInstance])
			digitDict[digitInstance] = multipleList[i]

		DigitComboDictCache[digitListStr] = (numCombos, digitDict)

	# compute sum of different combinations
	comboTotal = 0
	for digit in range(0,10): 
		digitInstances = digitList[digit]
		comboTotal += digit * digitDict[ digitInstances]

	return (numCombos, comboTotal)



def _findDigitCombinations(digitList, numDigits, lastDigit):
	'''
	digitList specifies how many instances of each digit are present
	numDigits gives the number of digit in final number
	lastDigit tracks what digit was used by parent in recursion chain.. we can't use that 
	   for current digit position

	Returns two tuple (numCombos, multipleForDigit) where
	   	numCombos is number of unique numbers
	   	multipleForDigit is a list that gives multiple for each digit to get the sum
		                you would multiply digit value with its corresponding multiple. 
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
		#print "****Cache hit ", DigitComboCache[digitListStr], digitList, digitListStr
		CacheHits += 1
		return DigitComboCache[digitListStr]


	multipleForDigit = [0 for i in range(0,10)]
	numCombos = 0

	for digit in range(0,10):
		currDigitCount = digitList[digit]
		if digit == lastDigit or currDigitCount == 0:
			continue

		#print "     "*numDigits, "**Start", numDigits, digit, numCombos, multipleForDigit

		if currDigitCount == numDigits:  # all other digits have to be this
			assert(numCombos == 0)
			numCombos = 1
			multipleForDigit[digit] = int("1"*numDigits)
			#print "     "*numDigits, "**Between", numCombos, multipleForDigit
			break

		assert(currDigitCount < numDigits)
		for digitCount in range(1,currDigitCount+1):
			currentMultiple = int("1"*digitCount)  # this should be the multiple since we are using 
							       #   digitCount consequetive instances 
			digitsLeft = numDigits - digitCount

			digitList[digit] -= digitCount
			nextNumCombos, nextPositionMultiple = _findDigitCombinations(digitList, digitsLeft, digit)
			digitList[digit] += digitCount

			# Let's say we found x combos in next level. For all those combos, current 
			# digit sequence will be present in front so it would contribute x times its value
			#
			#print "***", digit, currDigitCount, currentNumMultiple, digitsLeft, comboTotal
			multipleForDigit = [x+y for x,y in zip(multipleForDigit, nextPositionMultiple)]
			multipleForDigit[digit] += nextNumCombos * currentMultiple  * (10**digitsLeft)
			numCombos  += nextNumCombos

			#comboTotal += nextComboTotal + nextNumCombos * currentMultiple * (10**digitsLeft)
		#print "     "*numDigits, "**End", numDigits, digit, numCombos, multipleForDigit

	DigitComboCache[digitListStr] = (numCombos, multipleForDigit)
	CacheMiss += 1
	#print "****Cache miss ", DigitComboCache[digitListStr], digitList, digitListStr

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
			if counter % 100 ==0:
				print counter
				print "Cache miss = %d hits = %d  hit %% = %.2f size = %d"  % (CacheMiss, CacheHits, 100*CacheHits/(CacheHits+CacheMiss), len(DigitComboCache))

			#combos = findDigitCombinations(digitList)
			numCombos, comboTotal = findDigitCombinations(digitList)

			#print "%10d %4d " % (numCombos, comboTotal), digitList
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

#digitList[9] = digitList[8] = digitList[7] = 1
#print _findDigitCombinations(digitList, 3, 10)
#exit()

#MaxDigits = 5
answer = findDigitSets(digitList, MaxDigits)
print "Cache miss = %d hits = %d  hit %% = %.2f"  % (CacheMiss, CacheHits, 100*CacheHits/(CacheHits+CacheMiss))


print "Answer for ", MaxDigits, " = ", answer, answer%10**9

