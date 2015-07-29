# https://projecteuler.net/problem=117
#

class TileCombinations:
	def __init__(self,tileList):
		self.cache = {}
		self.tileList = tileList
		self.cache[0] = 1

	def getCombinations(self, totalLength):
		if totalLength in self.cache:
			return self.cache[totalLength]

		combos = self.getCombinations(totalLength-1)
		for tileLength in self.tileList:
			if tileLength <= totalLength:
				combos += self.getCombinations(totalLength-tileLength)

		self.cache[totalLength] = combos
		return combos


	 


assert(TileCombinations([2,3,4]).getCombinations(5) == 15)

print TileCombinations([2,3,4]).getCombinations(50)

