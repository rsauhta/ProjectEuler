# https://projecteuler.net/problem=36
#

MaxNum = 1000000   # It is actually max number + 1

sum = 0
for i in range(1,MaxNum):
	numStr = str(i)
	if not (numStr == numStr[::-1]):
		continue
	binStr = bin(i)[2:]
	if not (binStr == binStr[::-1]):
		continue
	#print "Found palindrom pair : ", i, binStr
	sum += i

print "answer = ", sum


