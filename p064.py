# https://projecteuler.net/problem=64
# Odd period square roots
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

#print "23 =>",findSequence(23)
count=0
for i in range(2,10001):
	seq = findSequence(i)
	if seq:
		period = len(seq) - 1  # first element is not part of the repeating sequence
		if period % 2 == 1:      # odd period 
			count += 1
	
print "Answer =",count	


