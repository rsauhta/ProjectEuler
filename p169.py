# https://projecteuler.net/problem=169
# Exploring the number of different ways a number can be expressed as a sum of powers of 2
#


# Imagine the number in binary and move from left most bit to right as you try different combinations
#  First take simple case of a number like 8
#  Combinations are 8 (1000), 4+4 (0100,0100), 4+2+2, (0100,0010,0010), 4+2+1+1 ((0100,0010,0001,0001)
#    Out of these combinations 1 uses left most bit, other 3 free up the left most bit
#
# Now imagine 40 viz. 32+8 => 101000 
#  Consider possible combinations 
#    32+8(100000 + xxxx)            => 4 combinations. since 8 can be expressed in 4 ways
#    16+16+8 (010000,010000, xxxx)  => 4 combinations

#    16+8+8+8 (010000,001000,001000, yyy)  => We can't use all combinations for 8 since 3rd bit conflicts 
# 					      but we can use combinations of 8 that free up the 3rd bit viz 3
# So for 40: 
#   4 combinations while keeping leading bit intact
#   7(4+3)  combinations while freeing up the leading bit
# 

def findAnswer(num):
	binStr = bin(num)

	index = len(binStr)-1   # count backwards
	prevCombosWithLeadingBit1 = 1
	prevCombosWithLeadingBit0 = 0

	while (binStr[index] != 'b'):
		leadingZeros=0
		while (binStr[index] == '0'):
			index -=1
			leadingZeros += 1

		assert(binStr[index] == '1')
		index -= 1

		combosWithLeadingBit1 =	prevCombosWithLeadingBit1 + prevCombosWithLeadingBit0 
		combosWithLeadingBit0 = leadingZeros * (prevCombosWithLeadingBit1 + prevCombosWithLeadingBit0)
		combosWithLeadingBit0 += prevCombosWithLeadingBit0

		#print "Iteration:"
		#print "    zeros =", leadingZeros
		#print "   prevCombos Leading1 = %3d  Leading0 = %3d" % (prevCombosWithLeadingBit1,prevCombosWithLeadingBit0)
		#print "   currCombos Leading1 = %3d  Leading0 = %3d" % (combosWithLeadingBit1,combosWithLeadingBit0)

		prevCombosWithLeadingBit0 = combosWithLeadingBit0
		prevCombosWithLeadingBit1 = combosWithLeadingBit1

	return combosWithLeadingBit0 + combosWithLeadingBit1


assert(findAnswer(10) == 5)
assert(findAnswer(52) == 13)
print findAnswer(10**25)



