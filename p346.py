# https://projecteuler.net/problem=346
# Strong repunits
#

import math

def getRepunitSum(maxNum):

	maxPower = int(math.sqrt(maxNum))

	numHash = {}
	for i in range(2,maxPower+1):
		multiple = i + 1
		while multiple < maxNum:
			if multiple in numHash:
				numHash[multiple] += 1
			else: 
				numHash[multiple] = 1
			multiple = multiple*i + 1

	total = 1    # count 1 as it is a special case. It is always 1 in all bases

	for key,value in sorted(numHash.iteritems()):
		if (value > 1) or \
	   	(key > maxPower+1 and key < maxNum-1):  # any number can be expressed as 11 where base = number-1
		                                        #  we don't track these cases to avoid hash from getting huge
			total += key

	return total 



#getRepunitSum(50)
assert(getRepunitSum(1000) == 15864)
print "Answer = ", getRepunitSum(10**12)

