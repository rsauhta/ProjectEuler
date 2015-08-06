# https://projecteuler.net/problem=42
#

import re

def getWordValue(wordStr):
	value = 0
	for char in wordStr:
		value += ord(char) - ord('A') + 1
	return value
		
def getTriangleNum(index):
	return index*(index+1)/2

assert(getWordValue("SKY") == 55)


# Unlikely that a word would have a value greater than 10000
MaxTriangleNumber = 10000

TriangleDict = {}
for n in range(1,1000):
	value = getTriangleNum(n)
	if value > MaxTriangleNumber: 
		break
	TriangleDict[value] = 1
	


with open("p042_words.txt") as f: 
	wordList = re.split(r'[",]+',f.read())
	
# first and last words are empty
print "0=", wordList[0] 	
del wordList[0] 	
print "-1 =",wordList[-1]
del wordList[-1]

print len(wordList)

assert(getWordValue("SKY") in TriangleDict)

counter=0
for word in wordList:
	value = getWordValue(word)
	assert (value < MaxTriangleNumber)
	if value in TriangleDict: 
		counter += 1
	
print counter


