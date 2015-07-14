# https://projecteuler.net/problem=43
#
#

import util
import math

GlobalSum=0


def IterateCombinations(count,digitDict,digitList):
	global GlobalSum

	#print digitList[0:count]

	if (count == 10):
		num = "".join(str(x)[0] for x in digitList)
		GlobalSum += int(num)
		print "..", num
	
	workingNum = 0 
	if (count > 3):
		workingNum = (digitList[count-1] + digitList[count-2]*10) * 10

	for key in digitDict.keys():

		num = workingNum + key
		if ((count == 3) and (num % 2)):   # Skip if not multiple of 2
			continue
		if ((count == 4) and (num % 3)):  
			continue
		if ((count == 5) and (num % 5)):  
			continue
		if ((count == 6) and (num % 7)):  
			continue
		if ((count == 7) and (num % 11)):  
			continue
		if ((count == 8) and (num % 13)):  
			continue
		if ((count == 9) and (num % 17)):  
			continue

		del digitDict[key]
		digitList[count] = key
		IterateCombinations(count+1, digitDict, digitList)
		digitDict[key] = 1




DigitDict = { }
DigitList = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
	DigitDict[i]=1


IterateCombinations(0, DigitDict, DigitList)
print "sum = ", GlobalSum

