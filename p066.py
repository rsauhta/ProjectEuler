# https://projecteuler.net/problem=66
# Diophantine equation
#
import math

def findSequence(n):
	# After each round we will have term of the form a+(root(n)-b)/d
	#
	rSqrt = math.sqrt(n)
	nSqrt = int(rSqrt)

	if rSqrt == nSqrt:
		return None

	# first round
	a = nSqrt
	bOrig = b = nSqrt
	dOrig = d = 1
	seq = [a]
	
	#print a, b, d

	while 1:
		newD = (n - b*b)/d
		newB = -1*b
		while newB <= nSqrt:
			newB += newD
		newB -= newD
		newA = float(b+newB)/newD
		assert(newA == int(newA))


		a = int(newA)
		b = newB
		d = newD
		seq.append(a)

		#print a, b, d

		if bOrig == b and dOrig == d: 
			break

	return seq


def findSolution(n, fractionSequence):
        #assert(n <= len(fractionSequence))

	maxLength = len(fractionSequence)
	#print n, maxLength, fractionSequence

	# try convergeents one by one
	for length in range(2,maxLength+1): 
		#print "    ",length
        	numer = 1
        	denom = 0

        	for i in range(length-1,-1,-1): # count backwards from the end
                	newTerm = fractionSequence[i]

                	tempDenom = numer
                	numer = newTerm*numer + denom
                	denom = tempDenom

		#print "--",numer,denom
		if numer*numer - n*denom*denom == 1:
			#print "  found answer", numer,denom
			return (numer,denom)

        return (None,None)


#print "23 =>",findSequence(23)
maxX = 1
dForMaxX=1

for i in range(2,1001):
	seq = findSequence(i)
	#print i, seq
	if seq:
		# Some trial and error showed that there are some numbers that require the
		#   sequence needs to be repeated one more time to get a solution 
		seq = seq + seq[1:]
		(numer,denom)=findSolution(i, seq)
		if numer == None:
			print "No solution for", i, seq
			assert(False)
		if numer > maxX:
			maxX = numer
			dForMaxX = i
			#print "found a new max", maxX, dForMaxX, numer,denom
	
print "Answer =",dForMaxX

