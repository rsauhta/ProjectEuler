# https://projecteuler.net/problem=92
#

def getDigitSum(n):
	digitSum = 0
	for digit in str(n):
		digitSum += int(digit)*int(digit)
	return digitSum


# largest possible digital sum for numbers upto 10 Million would be 
#   9^2 * 7 digits = 567
CacheNumberRange = 568
TestNumberRange = 10000000

SquareChainList = [0 for x in range(0,CacheNumberRange)]


for i in range(1,CacheNumberRange):
	num = i
	while (1):
		digitSum = getDigitSum(num)
		if digitSum == 1: 
			SquareChainList[i] = 1
			break
		elif digitSum == 89: 
			SquareChainList[i] = 89
			break
		else:
			num = digitSum


counter = 0
# Re-computing some numbers but those are a small fraction
for i in range(1,TestNumberRange):
	digitSum = getDigitSum(i)
	if SquareChainList[digitSum] == 89:   # normally I would put an asser there but index de-reference will 
	                                      #  throw exception if my assumption is wrong
		counter += 1


print counter


