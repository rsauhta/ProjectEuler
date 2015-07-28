# https://projecteuler.net/problem=62
#

def findPermutedCubes(start, count):
	cubeHash = {}
	cubeValue = {}

	for n in range(start,1000000):	  # sanity end value
		cubeStr = str(n*n*n)
		normStr = "".join(sorted(cubeStr))
		if normStr in cubeHash:
			cubeHash[normStr] += 1

			if cubeHash[normStr] == count: 
				#print "Solution = ", n, cubeValue[normStr]
				return cubeValue[normStr]
				break
		else:
			cubeHash[normStr]  = 1
			cubeValue[normStr] = cubeStr
	


print findPermutedCubes(1,5)
	
	
