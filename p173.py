# https://projecteuler.net/problem=173
# Using up to one million tiles how many different "hollow" square laminae can be formed ? 
#

import math

def findNumSquare(numTiles):

	# Max square would consist of a perimiter of tiles. For such a sqaure of size n,
	#  we would need 4n-4 tiles
	maxSize = int((numTiles+4)/4)

	total = 0
	for size in xrange(1,maxSize+1):
		outer = size 
		diff = outer*outer - numTiles   # compute if the outer square is so big that 
						# we can't make a solid square
		if (diff <= 0): 
			# solid square is possible. 
			# Set inner to the size of the smallest inner square that is possible
			if (outer % 2 == 0):
				inner=2
			else:
				inner=1     
		else:
			# we need to round up to the next size square 
			inner=int(math.ceil(math.sqrt(diff)))

			if (outer-inner) % 2 != 0:       # inner and outer should be same parity
				inner += 1            
		total += int((outer - inner)/2)
		#print "size = %3d inner %3d tiles=%3d combos=%3d" %(outer,inner, (outer*outer-inner*inner),(outer-inner)/2)

	return total

assert(findNumSquare(100) == 41)
print findNumSquare(10**6)


