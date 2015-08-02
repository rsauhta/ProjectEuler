# https://projecteuler.net/problem=301
#



MaxNum = 2**30
MaxNum = 2**25

def func(n):
	return (n ^ 2*n ^ 3*n == 0)

def findBruteForce(numBits):
	maxNum = 2**numBits - 1

	counter = 0
	for n in xrange(1,maxNum+1):
		if func(n): 
			counter += 1
	return counter
	
def findFaster(numBits):

	# Track cases when function equals zero
	#   Seed with the starting values for bit 0
	bitZeroWithNoCarry = 1
	bitZeroWithCarry = 0
	bitOneWithNoCarry = 0
	bitOneWithCarry = 0


	for bit in range(0,numBits):
		# Handle case of current bit = 0
		# currBit=0, prevBit=0, no carry => result for curr bit = 0, no carry 
		# currBit=0, prevBit=0, plus carry => result for curr bit != 0
		# currBit=0, prevBit=1, no carry => result for curr bit = 0, no carry 
		# currBit=0, prevBit=1, plus carry => result for curr bit != 0
		currBitZeroWithNoCarry = bitZeroWithNoCarry + bitOneWithNoCarry 
		currBitZeroWithCarry = 0

		# Handle case of current bit = 1
		# currBit=1, prevBit=0, no carry => result for curr bit = 0, no carry 
		# currBit=1, prevBit=0, plus carry => result for curr bit != 0
		# currBit=1, prevBit=1, no carry => result for curr bit = 0, with carry 
		# currBit=1, prevBit=1, plus carry => result for curr bit != 0
		currBitOneWithNoCarry = bitZeroWithNoCarry
		currBitOneWithCarry = bitOneWithNoCarry 

		bitZeroWithNoCarry = currBitZeroWithNoCarry 
		bitZeroWithCarry = currBitZeroWithCarry 
		bitOneWithNoCarry = currBitOneWithNoCarry 
		bitOneWithCarry = currBitOneWithCarry 


	# -1 to remove the case of 0
	return bitZeroWithNoCarry + bitOneWithNoCarry - 1



assert(findBruteForce(3) == findFaster(3))
assert(findBruteForce(10) == findFaster(10))
	
# handle case of < 2^30 by running findFaster routine with 29 bits. Handle the case of 2^30 directly
print  findFaster(29) + func(2**30)



