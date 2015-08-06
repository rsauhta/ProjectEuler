# https://projecteuler.net/problem=39
#

def findSolutions(perimeter):
	maxHyp = int(perimeter/2)    # Max possible value for hypotenuse. A side can not 
	                             #  be greater than sum of the other two sides
	minHyp = int (perimeter/3)   # Hypotenuse has to be the longest side
	
	solutions = 0
	for hyp in range(minHyp, maxHyp):
		# Let the non-hypotenuse sides be a and b, where a >= b 
		minA = int(0.5 + (perimeter - hyp)/2)
		maxA = perimeter - hyp  # Actually it should be -1 but this works out 
		                        #  for python ranges 
		
		for a in range(minA, maxA): 
			b = perimeter - hyp - a
			if (a*a + b*b) == hyp*hyp:
				#print hyp, a, b
				solutions += 1

	return solutions
	

maxSolutions = 0
maxSoutionPerimeter = 0

for peri in range(1,1000):
	solutions = findSolutions(peri) 
	#print "%3d = %d" %(peri,solutions)
	if solutions > maxSolutions: 
		maxSolutions = solutions 
		maxSolutionPerimeter = peri

print "Max solution perimeter = ", maxSolutionPerimeter


