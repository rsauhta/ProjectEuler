# https://projecteuler.net/problem=56
#

def findDigitalSum(n):
	digitalSum = 0
	for digit in str(n):
		digitalSum += int(digit)
	return digitalSum


maxSum = 0
for a in range(1,100):
	for b in range(1,100):
		digitalSum = findDigitalSum(a**b)
		maxSum = max(maxSum,digitalSum)
		
print maxSum
