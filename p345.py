# https://projecteuler.net/problem=345
#

def printMatrix(matrix):
	for row in matrix:
		str = ""
		for col in row: 
			str += "%6d" % (col)
		print(str)

testString =  ''' 7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303 '''

string = '''7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805'''


def getMatrixSum(matrix, columnList):
	currentRow = len(matrix) - len(columnList)
	if len(columnList) == 1:
		return (matrix[currentRow][columnList[0]], [columnList[0]]) 

	maxSum = 0
	maxCol = 0

	for col in range(0, len(columnList)): 
		if (currentRow < 4): 
			print currentRow, col
		tempList = list(columnList)
		del tempList[col]
		(maxTempSum, maxTempList) = getMatrixSum(matrix,tempList)
		#total = matrix[currentRow][columnList[col]] + getMatrixSum(matrix,tempList)
		total = matrix[currentRow][columnList[col]] + maxTempSum
		if total > maxSum: 
			maxSum = total
			maxCol = columnList[col]
			maxAnswerList = maxTempList
			#maxSum = max(maxSum, total)
	#print columnList
	#print "row = ", currentRow, " col = ", maxCol, "sum = ", maxSum, columnList
	#maxAnswerList.append(maxCol)
	maxAnswerList[:0] = [maxCol]
	return (maxSum, maxAnswerList)


def maxMatrixSum(matrixStr):
	matrix = [[int(x) for x in line.split()] for line in matrixStr.split("\n")]
	#printMatrix(matrix)

	columnList = range(0,len(matrix))
	return getMatrixSum(matrix, columnList)


assert(maxMatrixSum(testString)[0] == 3315)
(maxSum, answerList) = maxMatrixSum(string)
print maxSum, answerList



