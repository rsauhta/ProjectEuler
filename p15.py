# https://projecteuler.net/problem=15
#

def findAnswer(n):
	row = []

	for i in range(0,2*n+1): 
		nextRow=list(row)

		# row[0] stays the same
		# row[1..last-1] are sum of the previous row
		for index in range(1,i):
			nextRow[index]=row[index-1]+row[index]
		# Add a new element to the row. row[last] is 1
		nextRow.append(1)

		assert(len(nextRow) == i+1)
		#for index in range(0,i+1):
			#print "%3d" % (nextRow[index]), 
		#print    # newline at end of the row 
		row = nextRow

	assert(len(row) == 2*n+1)
	return row[n]


	
	

def factorial(n):
	factorial = 1
	for i in range (1,n+1):
		factorial *= i
	return factorial


# I got this solution by thinking like a dynamic programming example. 
#   Look at various lattice point in the grid and compute how many ways you can 
#   reach it. The pattern is Pascal's triangle.
print findAnswer(20)

# I got this solution by finding combiantions. There are 20 right and 20 down steps to be
#  fitted in 40 slots. There are 40x39x..21  ways to fit 20 right steps in 40 slots. 
#  We need to divide by 20! to eliminate permutations 
combinations = factorial(40) / (factorial(20)*factorial(20))

print combinations


