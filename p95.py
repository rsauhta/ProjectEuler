# https://projecteuler.net/problem=95
#

import util

MaxNumber = 1000000
processedList = [0 for x in range(0,MaxNumber)]


maxLength=0  	   # max length for a sequence encountered so far
minElement=0       # min element in the longest sequence

for i in range(1,MaxNumber):
	if (processedList[i]):    # Already processed
		continue

	processedList[i]=1
	aList = [i]		# Keep track of elements in current sequence

	currElement = i
	found = False           # last element that caused a loop
	while (1):
		currElement = sum(util.GetDivisors(currElement))
		if currElement in aList:
			found = True
			break

		if currElement >= MaxNumber:
			break
		if (processedList[currElement]):
			break

		processedList[currElement]=1
		aList.append(currElement)

	if found:
		index = aList.index(currElement)
		seqLen = len(aList) - index
		if seqLen > maxLength:
			maxLength = seqLen
			minElement=  min(aList[index:])


print minElement


