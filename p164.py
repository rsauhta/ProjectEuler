# https://projecteuler.net/problem=164
#  Number for which no three consecutive digits have sum greater than given value
#

'''
We first start with the 100 numbers in an array [0][0] .. [9][9] where we track if that number 
 has digits that add up to <=9. 
As we add a new digit to the left we construct a new array. for e.g. for a number starting with 
70, only valid numbers are 700* 701* 702* . 703* onwards would have 3 consecutive digits with sum 
  more than 9
  new[7][0] = old[0][0] + old[0][1] + old[0][2]
similarly 
  new[8][0] = old[0][0] + old[0][1]
  new[8][1] = old[0][0] 

'''

def printDigitArray(digitArray):
	print "   ",
	for i in range(10):
		print "%5d" % (i),
	print
	for i in range(len(digitArray)):
		print i, "=",
		for j in range(len(digitArray[i])):
			print "%5d" % (digitArray[i][j]),
		print 

def sumArray(digitArray):
	total=0
	# Skip the first row since we don't want to add the numbers with leading zeros
	for row in digitArray[1:]:
		total += sum(row)
	return total

def findCombos(numDigits): 

	assert (numDigits >= 2)
	twoDigitArray = [[1 for j in range(10-i)] for i in range(10)]
	
	#print "sum =", sumArray(twoDigitArray)
	#printDigitArray(twoDigitArray)
	for digitCount in range(1,numDigits-1):

		newDigitArray = []
		for newDigit in range(10):
			newArray = []
			for oldDigit1 in range(10-newDigit):
				total = 0
				for oldDigit2 in range(10-oldDigit1-newDigit):
					total += twoDigitArray[oldDigit1][oldDigit2]

				# this will get inserted at index oldDigits
				newArray.append(total)

			# This will get appended at index newDigit 
			newDigitArray.append(newArray)

		twoDigitArray = newDigitArray
		#print "sum =", sumArray(twoDigitArray)
		#printDigitArray( twoDigitArray)
	
	return sumArray(twoDigitArray)

		

def checkCondition(number):

	digitArray = [0,0,0]
	index=0
	while number > 0:
		digitArray[index] = number % 10
		if sum(digitArray) > 9: 
			return False

		number = number/10
		index = (index+1)%3

	return True

def bruteForce(numDigits):
	count=0
	for i in range(10**(numDigits-1),10**numDigits):
		if (checkCondition(i)):
			count+=1
	return count


assert(findCombos(4) == bruteForce(4))

answer = findCombos(20)
print "Answer =", answer 
