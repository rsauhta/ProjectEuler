# https://projecteuler.net/problem=92
#

def getDigitSum(n):
	digitSum = 0
	for digit in str(n):
		digitSum += int(digit)*int(digit)
	return digitSum

def getSquareChainDigitSum(num):
	"Converge square digit to 89 or 1, without using any cache"

	if num == 0: 
		return 0

	while (1):
		digitSum = getDigitSum(num)
		if digitSum == 1: 
			return 1
		elif digitSum == 89: 
			return 89
		else:
			num = digitSum





def approach1(numberRange):
	# largest possible digital sum for numbers upto 10 Million would be 
	#   9^2 * 7 digits = 567
	CacheNumberRange = 568

	SquareChainList = [getSquareChainDigitSum(x) for x in range(0,CacheNumberRange)]

	counter = 0
	# Re-computing some numbers but those are a small fraction
	for i in range(1,TestNumberRange):
		digitSum = getDigitSum(i)
		if SquareChainList[digitSum] == 89:   # normally I would put an assert here but index de-reference will 
		                                      #  throw exception if my assumption is wrong
			counter += 1
	return counter

def approach2(numberRange):

	squareChainDict = {0:1}        # seed value
	digitSquareList = [n*n for n in range(0,10)]    # we could just compute square everytime but this might be a bit faster

	# look at all combination for digit in each position
	for position in range(1,8): 	# <10 million has 7 digits
		newDict = {}
		for num,count in squareChainDict.iteritems(): # for each existing digit square sum, find 
		                                              #   combinations obtained by adding square for 
							      #   the next digit
			for digitSquare in digitSquareList:
				newSum = num + digitSquare
				if newSum in newDict:
					newDict[newSum] += count
				else:
					newDict[newSum] = count
		squareChainDict = newDict
		
	counter=0
	for num,count in squareChainDict.iteritems():
		if getSquareChainDigitSum(num)  == 89:
			counter += count
	return counter
		
	

TestNumberRange = 10000000
print approach2(TestNumberRange)


