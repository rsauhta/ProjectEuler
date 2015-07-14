# https://projecteuler.net/problem=81
#
#

import util
import math


#Filename = "p81_test.txt"
Filename = "p81.txt"

def findPath(matrix, size):

	for row in range(1,size):
		for col in range(0,row+1):
			if col == 0: 
				left=9999   # really large value
			else: 
				left=matrix[row-col][col-1]
			if row-col == 0: 
				top=9999 
			else:
				top=matrix[row-col-1][col]
			matrix[row-col][col] += min(top,left)


	for col in range(1,size):
		for row in range(0, size-col):
			left=matrix[size-row-1][col+row-1]
			top=matrix[size-row-1-1][col+row]
			matrix[size-row-1][col+row] += min(top,left)
	print matrix
	



Matrix = []
with open(Filename) as f:
        for line in f:
                numList = [int(x) for x in line.split(',')]
		Matrix.append(numList)
print Matrix

print "solution ...."
findPath(Matrix, 80)

