# https://projecteuler.net/problem=101
#

import math
import numpy 

def testFunction(n):
	return int(math.pow(n,3))


def genFunction(n):
	return 1 - n                \
	         + int(math.pow(n,2))    \
		 - int(math.pow(n,3))    \
		 + int(math.pow(n,4))    \
		 - int(math.pow(n,5))    \
		 + int(math.pow(n,6))    \
		 - int(math.pow(n,7))    \
		 + int(math.pow(n,8))    \
		 - int(math.pow(n,9))    \
		 + int(math.pow(n,10))



def getSolution(valList, maxPoly):
	"Assuming maxPoly power of polynomial, find a solution. Return the first incorrect term"

	terms = maxPoly+1
	#print terms, valList[:terms]

	B = numpy.matrix(numpy.zeros((terms,1)))
	for i in range(0,terms):
		B[i,0] = valList[i]

	A = numpy.matrix(numpy.zeros((terms,terms)))
	for i in range(0,terms): 
		for j in range(0,terms):
			A[i,j] = math.pow(i+1,j)

	#print A
	#print B

	fit = 0
	#solution = A.I * B 
	solution = numpy.linalg.solve(A , B )

	for j in range(0,terms): 
		print "%9d" % (solution[j][0]),
		#fit += int(solution[j][0]*math.pow(terms+1,j))
		fit += int(solution[j][0]*math.pow(terms+1,j))
	print 
	return fit






testList = [testFunction(i) for i in range(1,5)]
assert(74 == getSolution(testList,0) + getSolution(testList,1) + getSolution(testList,2))
getSolution(testList,3)   # check if we get the correct solution
print "Unit test passed"
print 


valueList = [genFunction(i) for i in range(1,12)]

total = 0
for i in range(0,10):
	total += getSolution(valueList,i)

getSolution(valueList,10)
print "Sum of FIT = ", total

