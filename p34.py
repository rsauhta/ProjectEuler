# https://projecteuler.net/problem=34
#

def factorial(n):
	fact = 1
	for i in range (1,n+1):
		fact *= i
	return fact




factorialList = []
for i in range(0,10):
	factorialList.append( factorial(i))


# 7*9! = 2540160
# 8*9! = 2903040 i.e. 7 digit number so we don't need to 
#   check beyond 7 digit numbers
# 
curiousTotal = 0
for i in range(3,2540160): 
	sum=0
	for digit in str(i): 
		sum += factorialList[int(digit)]
	if (i == sum):
		print "curious : ", i
		curiousTotal += i

print "Total = ", curiousTotal 



