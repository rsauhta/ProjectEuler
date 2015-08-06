# https://projecteuler.net/problem=24
#

def factorial(n):
	factorial = 1
	for i in range (1,n+1):
		factorial *= i
	return factorial



def getNth(digitListIn, number):
		
	number -= 1   # off by 1 since we are counting from 0
	digitList = list(digitListIn)
	length = len(digitList)
	numStr = ""

	for i in range(length-1,0,-1): 
		fact = factorial(i)
		multiple = int(number / fact)
		number = number % fact 
		numStr += str(digitList[multiple])
		del digitList[multiple]

	numStr += str(digitList[0])
	return numStr




digitList = range(0,3)
assert(getNth(digitList,5) == "201")

print getNth(range(0,10), 1000000)



