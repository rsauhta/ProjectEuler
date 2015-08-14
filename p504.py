# https://projecteuler.net/problem=504
# Square on the Inside
#

# To compute the number of lattice points in a quadrilateral, break it into 4 triangles with origin
# There are only 100x100 possible triangle combinations. Pre compute sum for all these combination. 
# Then iterate over each combination of a,b,c,d and check if sum of 4 triangles (a,b)(b,c)(c,d) and (d,a) is
#   a square.
#   Each triangle can be compu

from pprint import pprint


# compute number of lattice point strictly inside the triangle formed with side of length a and b
# Do not count points on any of the edges viz, x, y and hypotenuse 
# 
def computeTriangle(a,b):
	# imagine a line through origin y = (b/a) x 
	#  if a <= b, this would run a bit faster 
	total = 0
	for x in range(1,a):
		xd = x - .00001
		total += int(b*xd/a)
	return total



# Compute sums for various possible triangles and store in a hash
def ComputeSumForTriangles(size):
	# Ignore index 0 values.
	TriangleSums = [ [0 for i in range(size+1)] for j in range(size+1)]

	for a in range(1,size+1):
		for b in range(a,size+1):
			assert(TriangleSums[a][b] == 0 == TriangleSums[b][a])
			TriangleSums[a][b] =  TriangleSums[b][a] = computeTriangle(a,b)

	return TriangleSums


def findAnswer(size):
	tSum = ComputeSumForTriangles(size)
	squareDict =  dict( [n*n,1] for n in range(200))

	count = 0
	for a in range(1,size+1):
		print a, "/",size
		for b in range(1,size+1):
			for c in range(1,size+1):
				for d in range(1,size+1):
					total = tSum[a][b] + tSum[b][c] + tSum[c][d] + tSum[d][a]

					# we need to add the points on the x and y axis. a+b+c+d will 
					#  give these points but count origin 4 times, so subtract 3
					total += a+b+c+d-3

					if total in squareDict:
						count += 1
	return count						

assert(findAnswer(4) == 42)
answer = findAnswer(100)

print
print "Answer=",answer


