# https://projecteuler.net/problem=115
#

class TileCombinations:
	def __init__(self, minLength):
                self.minLength = minLength 
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
		for tileLength in range(self.minLength,totalLength+1):
                        # Use the tile + 1 black tile for gap
		        combos += self.getCombinations(totalLength-tileLength-1)

		self.cache[totalLength] = combos
		return combos


	 
testCombinations = TileCombinations(10)
assert(testCombinations.getCombinations(56) == 880711)
assert(testCombinations.getCombinations(57) == 1148904)


tileCombos = TileCombinations(50)
for totalLength in range(50,1000):    # Fill in a very large terminating value
        numCombos = tileCombos.getCombinations(totalLength)
        if numCombos > 1000000:
                print "Answer = ", totalLength
                break



