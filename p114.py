# https://projecteuler.net/problem=114
#

class TileCombinations:
	def __init__(self):
                self.minLength = 3
		self.cache = {}

	def getCombinations(self, totalLength):

                if totalLength < self.minLength:  
                        # totalLengh can be 0 or -1 under terminating condition. 
                        #   we return 1 for even those cases to keep logic clean but 
                        #   it does mean we will return number of combinations as 1 if 
                        #   someone invokes the method directly with value of 0 or -ve value
                        return 1

		if totalLength in self.cache:
			return self.cache[totalLength]

		combos = self.getCombinations(totalLength-1)  #  Use one black tile

                # Try using different sized tiles
		for tileLength in range(3,totalLength+1):
                        # Use the tile + 1 black tile for gap
		        combos += self.getCombinations(totalLength-tileLength-1)

		self.cache[totalLength] = combos
		return combos


	 


assert(TileCombinations().getCombinations(7) == 17)

print TileCombinations().getCombinations(50)


