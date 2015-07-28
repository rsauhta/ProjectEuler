# https://projecteuler.net/problem=125
#
import math

def isNumberPalindrome(n):
	"returns True if n is palindrome"
	numStr = str(n)
	return numStr == numStr[::-1]


def palindromeSum(maxNumber):
	MaxN = int(math.sqrt(maxNumber) + 0.5) 

	SquareList = [n*n for n in range(0,MaxN)]   # 0th entry is dummy
	WorkingList = list(SquareList)

	duplicateDict = {}
	
	total=0
	for iteration in range(1,MaxN-1):		# each successive iteration we add more squares
		for index in range(1,MaxN-iteration):    # start adding from index 
			num = WorkingList[index] + SquareList[index+iteration]
			WorkingList[index] = num
			if num < maxNumber and isNumberPalindrome(num): 
				if num in duplicateDict: 
					#print "duplicate"
					continue
				duplicateDict[num]=1
				#print iteration, index, WorkingList[index]
				total += num
	
	
	return total
 

assert(palindromeSum(1000) == 4164)
print palindromeSum(10**8)


