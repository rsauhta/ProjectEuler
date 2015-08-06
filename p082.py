# https://projecteuler.net/problem=82
#
#

import util
import math
import copy
import logging

#logging.basicConfig(format='%(message)s',level=logging.DEBUG)


def findPath(inMatrix):
	size = len(inMatrix)
	sMatrix = copy.deepcopy(inMatrix)  # sMatrix for solution matrix
	
	printMatrix(sMatrix)	

	logging.debug("Input")
	printMatrix(sMatrix)	

	# Start with column 1. First (0th) column doesn't need to be processed
	for col in range(1,size):

		# Update value for move right
		for row in range(0,size):
			sMatrix[row][col] = sMatrix[row][col-1] + inMatrix[row][col]

		logging.debug("Processing column %d " % (col))
		printMatrix(sMatrix)

		if (col == size-1):	# Don't need to check up/down for the last column
			break

		# Account for any up or down moves 

		for row in range(0,size):

			# Process from current row till top 
			moveTotal = 0
			for moveRow in range(row-1,-1,-1): 
				moveTotal += inMatrix[moveRow+1][col]
				# Update, if moving down from moveRow will be better
				sMatrix[row][col] = min(sMatrix[row][col], \
							sMatrix[moveRow][col] + moveTotal)
					
			# Process from current row to bottom
			moveTotal = 0
			for moveRow in range(row+1,size): 
				moveTotal += inMatrix[moveRow-1][col]
				# Update, if moving up from moveRow will be better
				sMatrix[row][col] = min(sMatrix[row][col], \
							sMatrix[moveRow][col] + moveTotal)

		logging.debug("After up and down ")
		printMatrix(sMatrix)	


	minCost = sMatrix[0][size-1]
	for row in range(1,size):
		minCost = min(minCost, sMatrix[row][size-1])

	logging.debug("Returning mininum cost %d " % (minCost))

	return minCost

	
def printMatrix(matrix):
	for row in matrix:
		str = ""
		for col in row: 
			str += "%6d" % (col)

		logging.debug(str)


def readMatrix(filename):
	
	matrix = []
	with open(filename) as f:
        	for line in f:
                	numList = [int(x) for x in line.split(',')]
			matrix.append(numList)
	return matrix



matrix = readMatrix("p81_test.txt")
assert(len(matrix) == 5)
assert(findPath(matrix) == 994)


matrix = readMatrix("p082_matrix.txt")
assert(len(matrix) == 80)
print "Solution = ", findPath(matrix)


