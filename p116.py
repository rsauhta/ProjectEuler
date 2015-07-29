# https://projecteuler.net/problem=116
#

class TileCombinations:
	def __init__(self,tileLength):
		self.cache = {}
		self.tileLength = tileLength
		for length in range(0,self.tileLength):
			self.cache[length] = 1

	def getCombinations(self, totalLength):
		return self._getCombinations(totalLength) - 1
	
	def _getCombinations(self, totalLength):
		if totalLength in self.cache:
			return self.cache[totalLength]

		combos = self._getCombinations(totalLength-1) + self._getCombinations(totalLength-self.tileLength)
		       
		self.cache[totalLength] = combos
		return combos


	 


assert(TileCombinations(2).getCombinations(5) == 7)

print (TileCombinations(2).getCombinations(50) + \
       TileCombinations(3).getCombinations(50) + \
       TileCombinations(4).getCombinations(50))
