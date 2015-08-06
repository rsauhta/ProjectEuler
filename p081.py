# https://projecteuler.net/problem=81
#
#

import util
import math
import copy



def findPath(inMatrix, size):
	matrix = copy.deepcopy(inMatrix)
	for row in range(1,size):
		for col in range(0,row+1):
			if col == 0: 
				matrix[row-col][col] += matrix[row-col-1][col]
			elif row-col == 0: 
				matrix[row-col][col] += matrix[row-col][col-1]
			else:
				left=matrix[row-col][col-1]
				top=matrix[row-col-1][col]
				matrix[row-col][col] += min(top,left)

	for col in range(1,size):
		for row in range(0, size-col):
			left=matrix[size-row-1][col+row-1]
			top=matrix[size-row-1-1][col+row]
			matrix[size-row-1][col+row] += min(top,left)
	return matrix

	
def printMatrix(matrix):
	for row in matrix:
		for col in row: 
			print "%4d" % (col),
		print


def readMatrix(filename):
	
	matrix = []
	with open(filename) as f:
        	for line in f:
                	numList = [int(x) for x in line.split(',')]
			matrix.append(numList)
	return matrix



matrix = readMatrix("p81_test.txt")
solution = findPath(matrix, len(matrix))
assert(solution[4][4] == 2427)



matrix = readMatrix("p81.txt")
assert(len(matrix) == 80)
solution = findPath(matrix, len(matrix))

print "solution = ", solution[79][79] 

