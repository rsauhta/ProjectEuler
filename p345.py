# https://projecteuler.net/problem=345
#
import copy

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


class CacheEntry:
	def __init__(self, colList = []):
		self.columnList = colList

	def printout(self):
		print self.columnList

	def __hash__(self):
		return hash(str(sorted(self.columnList)))

	def __eq__(self, other):
		return sorted(self.columnList) == sorted(other.columnList)

	@staticmethod
	def testCacheEntry():
		a = CacheEntry([1,2,3])
		b = CacheEntry([3,1,2])
		assert(a == b)
		cacheDict = {a:33}
		assert(cacheDict[b] == 33)

CacheEntry.testCacheEntry()




def findMax(matrix):

	# To understand the approach, imagine you remove the last row. With the previous n-1 rows, you can 
	#  form n-1 matrix of n-1xn-1 viz. col 2..n, 1,3..n, 1,2,4..n --  1..n-1 
	# If you now add the last row the max sum would be mat[n,1]+maxFor[2..n]  mat[n,2]+max[1,3..n] -- so forth
	# 
	# We will use this approach of incrementally building the solution. First start with the first row and 1x matrix
	# Then for the next row, iterate through each column (1..n). Add this column to each of the sums from previous iteration
	#  for the second row we would end up with n*(n-1) sums, each caches by column combinations (1,2) (1,3) ... (n-1)n. 
	#  However (1,2) and (2,1) are the same matrix so we should collapse that to get n(n-1)/2 sums. We do this by mapping 
	#    (1,2) and (2,1) to same key as can be seen in class CacheEntry 
	#  As we iterate the number of sums being maintained in cache would grow until the midpoint and then unique sum being
	# maintained will start reducing till we have just one at the end for 1..n columns.
	# 


	matrixSize = len(matrix)

	# see the cache 
	prevCachedEntries = {CacheEntry():0}


	# Add a new row a
	for row in range(0,matrixSize):
		
		# Build a new cache for the row x row matrix. This will build on previous cache for (row-1)x(row-1) matrix 
		newCachedEntries = {}

		# For each cache entry, try all combination of adding all column position for the row being processed
		for prevEntry,prevSum in prevCachedEntries.iteritems():
			for col in range(0,matrixSize):

				# Ignore cols that are already in the cache entry. 
				if col not in prevEntry.columnList:
					newEntry = copy.deepcopy(prevEntry)
					newEntry.columnList.append(col)
					newSum = prevSum + matrix[row][col]
					if newEntry not in newCachedEntries:
						newCachedEntries[newEntry] = newSum
					elif newSum > newCachedEntries[newEntry]:
						# round about way but this way the entry stored as the key
						#  would contain the right column sequence
						# for e.g [1,2,3] maybe replaced by [3,2,1] since the second combination
						#   has a larger sum. If we didn't do the below logic, [1,2,3] would be
						#   stored as the key
						del(newCachedEntries[newEntry])
						newCachedEntries[newEntry] = newSum

		prevCachedEntries = newCachedEntries

		#print "Processed row ", row
		#for entry,maxSum in prevCachedEntries.iteritems():
			#print entry.columnList, maxSum
			
	assert(len(prevCachedEntries) == 1)   # There should be only one entry at the end
	keyValue =prevCachedEntries.items()[0]
	return(keyValue[1], keyValue[0].columnList)



def maxMatrixSum(matrixStr):
	matrix = [[int(x) for x in line.split()] for line in matrixStr.split("\n")]
	#printMatrix(matrix)

	columnList = range(0,len(matrix))
	return findMax(matrix)


assert(maxMatrixSum(testString)[0] == 3315)
(maxSum, answerList) = maxMatrixSum(string)
print answerList
print "Answer =",maxSum



