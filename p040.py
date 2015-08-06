# https://projecteuler.net/problem=40
#

def getNthDigit(n):
	decimalCount=0
	num = 0
	while (1):
		num +=1
		strNum = str(num)
		if (decimalCount + len(strNum) >= n):
			return int(strNum[n-decimalCount-1])
		else: 
			decimalCount += len(strNum)
	

assert(getNthDigit(5) == 5)
assert(getNthDigit(12) == 1)
			
digitPosition = 1
product = 1
for i in range(0,7):
	digit = getNthDigit(digitPosition)
	print "%8d : %d" % (digitPosition,digit)
	product *= digit
	digitPosition *= 10

print product 
			
		


	
	
	

