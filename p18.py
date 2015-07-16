# https://projecteuler.net/problem=18
#


# Read file into a grid

def readFile(filename):
	triangleGrid = []

	with open(filename) as f:
        	for line in f:
			numList = [int(x) for x in  line.split()]
			triangleGrid.append(numList)
		
	return triangleGrid


def printGrid(grid):
	size = len(grid)

	for row in range(0,size):
		for col in range(0,row+1):
			print grid[row][col],
		print ""
	

def findMax(grid):
	size = len(grid)

	for row in range(size-2, -1, -1):   # from bottom row to top
		for col in range(0,row+1):
			grid[row][col] += max(grid[row+1][col], grid[row+1][col+1])



# Test 
grid = readFile("p18_test.txt")
findMax(grid)
assert(grid[0][0] == 23)

grid = readFile("p18.txt")
findMax(grid)
print "Problem 18 = ", grid[0][0]

grid = readFile("p067_triangle.txt")
findMax(grid)
print "Problem 18 = ", grid[0][0]


