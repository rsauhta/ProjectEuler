# https://projecteuler.net/problem=96
# Read sudoku grid from sudoku.txt and solve
#


class Matrix:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.grid = [[0 for row in range(0,rows)] for col in range(0,cols)]

	def print(self):
		for row in self.grid:
			print("".join(map(str,row)))

	def read(self, filehandle):
		for row in range(0,self.rows):
			linestr = filehandle.readline()
			valueList = list(map(int, list(linestr[:-1])))
			assert(len(valueList) == self.cols)
			for col in range(len(valueList)):
				self.grid[row][col] = valueList[col]



class Cell:
	def __init__(self, value):
		# don't think we need row and col
		self.value = value
		if value == 0:
			self.possibleList = list(range(1,10))
		else:
			self.possibleList = []
		self.cellGroupList = []

	def addCellGroup(self, cellGroup):
		self.cellGroupList.append(cellGroup)
		assert(len(self.cellGroupList) < 4)

	# return True if this was the last value removed
	def removePossibleValue(self, value):
		if self.value > 0:
			return False
		if value in self.possibleList:
			self.possibleList.remove(value)
			assert(len(self.possibleList) > 0)
			if (len(self.possibleList) == 1):
				self.value = self.possibleList[0]
				self.possibleList=[]
				return True
		return False


# CellGroup is a collection of 9 cells
#   Row, Col and 3x3 sub-grid each contains 9 cells
class CellGroup:
	def __init__(self):
		self.cellList = []

	def addCell(self, cell):
		self.cellList.append(cell)
		assert(len(self.cellList) < 10)
		cell.addCellGroup(self)


class Grid:


	def __init__(self, matrix):
		grid = []
		resolvedList = []

		#possibleList = range(1,10)
		for row in range(0,9):
			rowList = []
			for col in range(0,9):
				cell = Cell(matrix.grid[row][col])
				rowList.append(cell)
				if matrix.grid[row][col] != 0:
					resolvedList.append(cell)
			grid.append(rowList)

		self.grid = grid
		self.resolvedList  = resolvedList

		groupList = []
		# create sub-groups of cell
		for x in range(0,9):
			rowGroup = CellGroup()
			colGroup = CellGroup()
			subgridGroup = CellGroup()
				# imagine subgrids are numbered as 0 1 2
				#                                  3 4 5
				#                                  6 7 8
			for y in range(0,9):
				rowGroup.addCell(grid[x][y])
				colGroup.addCell(grid[y][x])

				subgridStartRow = 3 * int(x/3)
				subgridStartCol = 3 * (x % 3)
				subgridRow = int(y/3)
				subgridCol = y % 3
				subgridGroup.addCell(grid[subgridStartRow + subgridRow][subgridStartCol+subgridCol])

		groupList.append(rowGroup)
		groupList.append(colGroup)
		groupList.append(subgridGroup)
		self.groupList = groupList

	def validate(self):
		for row in range(0,9):
			for col in range(0,9):
				cell = self.grid[row][col]
				if cell.value == 0:
					assert(len(cell.possibleList) > 0)
				else:
					assert(len(cell.possibleList) == 0)
				assert(len(cell.cellGroupList) == 3)
		for group in self.groupList:
			assert(len(group.cellList) == 9)

	def getMatrix(self):
		matrix = Matrix(9,9)
		for row in range(0,9):
			for col in range(0,9):
				matrix.grid[row][col] = self.grid[row][col].value
		return matrix

		a =  '''

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

'''

	def solve(self):
		print("do nothing")





filename = "p096_sudoku.txt"
with open(filename) as filehandle:
	while True:
		gridName=filehandle.readline()
		if gridName == '': break

		matrix = Matrix(9,9)
		matrix.read(filehandle)
		print(gridName[:-1])
		matrix.print()

		grid = Grid(matrix)
		grid.solve()

		grid.validate()
		mat = grid.getMatrix()
		mat.print()
		#print("Solution")
		#printMatrix(newMatrix)
		#print("")





