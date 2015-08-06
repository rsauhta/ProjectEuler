# https://projecteuler.net/problem=79
#


pHash = {}
filename = "p079_keylog.txt"
with open(filename) as f:
	for line in f:
		pHash[int(line)]=1

pList = [[int(y) for y in str(x)] for x in pHash.keys()]

#print pList


# for each digit print all other digits that come before it and after it 
for digit in range(0,10):
	beforeDict = {}
	afterDict = {}
	for code in pList:
		digitFound=0
		if digit == code[0]:
			digitFound+=1
			afterDict[code[1]] = afterDict[code[2]] = 1
		if digit == code[1]:
			digitFound+=1
			afterDict[code[2]] = 1
			beforeDict[code[0]] = 1
		if digit == code[2]:
			digitFound+=1
			beforeDict[code[0]] = beforeDict[code[1]] = 1

		assert(digitFound <= 1)
	print digit, " => ", sorted(beforeDict.keys()), sorted(afterDict.keys()) 


# Solved this problem by looking at the before and after list e.g. for 7, there is no before,
#  and everything in after list; so 7 is the first digit. 
#  Found the answer 73162890

