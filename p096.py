# https://projecteuler.net/problem=96
# Read sudoku grid from sudoku.txt and solve
#

import math
import copy
from collections import namedtuple


def printMatrix(matrix):
	for row in matrix:
		print("".join(map(str,row)))


def readMatrix(filehandle):
	matrix = []
	for rows in range(0,9):
		linestr = filehandle.readline()
		matrix.append(list(map(int, list(linestr[:-1]))))
	return matrix




class Grid:
	def __init__(self, matrix):
		self.Cell = namedtuple('Cell', "row col value possibleList")
								# row, col for this cell. Possibly redundant
								# value = for the cell if known, 0 => value not known yet
								# possibleList = list of possible values for this cell
		grid = []
		possibleList = range(1,10)
		for row in range(0,9):
			rowList = []
			for col in range(0,9):
				if matrix[row][col] == 0:
					rowList.append( self.Cell(row, col, matrix[row][col],list(possibleList)))
				else:
					rowList.append(self.Cell(row, col, matrix[row][col], []))
			grid.append(rowList)

		self.grid = grid
		self.almostResolvedList  = []  # keep track of cells with single value in possibleList



	def solve(self):

		grid = self.grid

		for row in range(0,9):
			for col in range(0,9):
				if grid[row][col].value != 0:
					# this is a known value. This value can not occur in this sub-grid, row or column.
					self.resolveValue(row,col,grid[row][col].value)

		while (len(self.almostResolvedList) > 0):
			(row,col) = self.almostResolvedList.pop()
			self.resolveValue(row,col, grid[row][col].possibleList[0])

		resultMatrix = []
		for row in range(0,9):
			rowList = []
			for col in range(0,9):
				#assert(grid[row][col].value != 0)
				rowList.append(grid[row][col].value)
			resultMatrix.append(rowList)
		return resultMatrix

	# this cell has known value. Remove this "knownValue" from the corresponding row, col and sub-grid
	def resolveValue(self,row,col,knownValue):
		if knownValue in self.grid[row][col].possibleList:
			self.grid[row][col].possibleList.remove(knownValue)
		assert(len(self.grid[row][col].possibleList) == 0)
		if (self.grid[row][col].value == 0):
			self.grid[row][col] = self.Cell(row,col, knownValue, [])

		for x in range(0, 9):
			self.removeValue(row, x, knownValue)
			self.removeValue(x, col, knownValue)

		subgridRowStart = row - row % 3
		subgridColStart = col - col % 3
		for subrow in range(0, 3):
			for subcol in range(0, 3):
				self.removeValue(subgridRowStart + subrow, subgridColStart + subcol, knownValue)


	def removeValue(self,row,col,value):
		possibleList = self.grid[row][col].possibleList
		if value in possibleList:
			possibleList.remove(value)
			if (len(possibleList) < 1):
				print("failed at", row, col, self.grid[row][col])
			if len(possibleList) == 1:
				self.almostResolvedList.append((row,col))


def solveSudoku(matrix):
	solver = Grid(matrix)
	return solver.solve()




filename = "p096_sudoku.txt"
with open(filename) as filehandle:
	while True:
		gridName=filehandle.readline()
		if gridName == '': break

		matrix=readMatrix(filehandle)
		print(gridName[:-1])
		printMatrix(matrix)

		newMatrix = solveSudoku(matrix)
		print("Solution")
		printMatrix(newMatrix)
		print("")





