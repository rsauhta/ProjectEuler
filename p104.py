# https://projecteuler.net/problem=104
#


def isPandigital(panStr):
	if (len(panStr) < 9):
		return False
	for digit in range(1,10):
		if str(digit) not in panStr:
			return False
	return True



assert(isPandigital("123456789") == True)
assert(isPandigital("123456709") == False)

	
fibOne = 1
fibTwo = 1 
fibCounter=2

trailerOne = 1
trailerTwo = 1

while True:
	temp = fibTwo
	fibTwo = fibOne + fibTwo
	fibOne = temp

	temp = trailerTwo
	trailerTwo = (trailerOne + trailerTwo) % 10**9   # Only track last 9 digits
	trailerOne = temp

	fibCounter += 1

	#if fibCounter % 100 == 0:
		#print fibCounter

	
	if isPandigital(str(trailerTwo)):
		#print "Trailing matches ", fibCounter
                fibCounter
	else: 
		continue

	fibStr = str(fibTwo)
	if isPandigital(fibStr[:9]):
		print "Answer is ", fibCounter
		break



