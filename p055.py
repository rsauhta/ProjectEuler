# https://projecteuler.net/problem=55
#



def checkLychrel(n):

	#print "Testing ", n
	strNum = str(n)
	for i in range(1,50):   # Less than 50 iterations
		newNum = int(strNum) + int(strNum[::-1])
		#print "%2d %d" %(i,newNum)
		strNum = str(newNum)
		if (strNum == strNum[::-1]):     # if number is palindrome
			return False

	return True



assert(checkLychrel(4994) == True)
assert(checkLychrel(47) == False)
assert(checkLychrel(349) == False)


counter = 0
for num in range(1,10000):
	if checkLychrel(num):
		counter += 1

print counter
