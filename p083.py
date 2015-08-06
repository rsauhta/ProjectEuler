# https://projecteuler.net/problem=83
#
#

import util
import math
import copy

# Seed solution matrix with a value that will be larger than the answer
MAX_POSSIBLE_ANSWER = 2**31


def updateCell(inMatrix, solutionMatrix, cellRow, cellCol, recurse=True):
	matrixSize = len(inMatrix)

	if (cellRow == 0 and cellCol == 0):
		solutionMatrix[cellRow][cellCol] = inMatrix[cellRow][cellCol]
		return

	# Don't process un-initialized cell during recursion
	if recurse and solutionMatrix[cellRow][cellCol] == MAX_POSSIBLE_ANSWER:
		return

	currBest = solutionMatrix[cellRow][cellCol]
	# first find the best path to this cell 
	newBest = currBest    # actually we are going to compute the newBest sum without
	                      #  contribution from current cell but we will account for that later
	if (cellCol > 0):
		newBest = min(newBest, solutionMatrix[cellRow][cellCol-1])
	if (cellCol < matrixSize-1):
		newBest = min(newBest, solutionMatrix[cellRow][cellCol+1])
	if (cellRow > 0):
		newBest = min(newBest, solutionMatrix[cellRow-1][cellCol])
	if (cellRow < matrixSize-1):
		newBest = min(newBest, solutionMatrix[cellRow+1][cellCol])
	
	newBest += inMatrix[cellRow][cellCol]

	# if we didn't find a better path, nothing else needs to be done
	if currBest <= newBest:
		return 

	# if we did find a better path, update current cell and check if any neighbours need to be updated
	solutionMatrix[cellRow][cellCol] = newBest


	if (cellCol > 0) and (newBest+inMatrix[cellRow][cellCol-1] < solutionMatrix[cellRow][cellCol-1]):
		updateCell(inMatrix, solutionMatrix, cellRow, cellCol-1)
	if (cellCol < matrixSize-1) and (newBest+inMatrix[cellRow][cellCol+1] < solutionMatrix[cellRow][cellCol+1]):
		updateCell(inMatrix, solutionMatrix, cellRow, cellCol+1)
	if (cellRow > 0) and (newBest+inMatrix[cellRow-1][cellCol] < solutionMatrix[cellRow-1][cellCol]):
		updateCell(inMatrix, solutionMatrix, cellRow-1, cellCol)
	if (cellRow < matrixSize-1) and (newBest+inMatrix[cellRow+1][cellCol] < solutionMatrix[cellRow+1][cellCol]):
		updateCell(inMatrix, solutionMatrix, cellRow+1, cellCol)

		


def findPath(inMatrix):

	solutionMatrix = copy.deepcopy(inMatrix)
	for row in range(0,len(inMatrix)):
		for col in range(0,len(inMatrix)):
			solutionMatrix[row][col] = MAX_POSSIBLE_ANSWER

	for row in range(0,len(inMatrix)):
		for col in range(0,len(inMatrix)):
			updateCell(inMatrix, solutionMatrix, row, col, False)
			
	return solutionMatrix

	
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


import sys
sys.setrecursionlimit(100)

matrix = readMatrix("p81_test.txt")
solution = findPath(matrix)
assert(solution[4][4] == 2297)



matrix = readMatrix("p81.txt")
assert(len(matrix) == 80)
solution = findPath(matrix)

print "solution = ", solution[79][79] 

