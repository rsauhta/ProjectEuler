# https://projecteuler.net/problem=250
#  sum upto 250

import pprint

Last16Digit = 10**16

def findCombos(maxN, modN):
	
	# There are 250250 elements but they would all map to a value in range 0-249 
	# This array will track number of combinations for getting each mod value 
	# We only care about 0 value at the end, but we need to track each value as we iterate 
	#   through each element
	comboArray = [0 for i in range(250)]
	comboArray[0] = 1

	# We will incrementally add each of the maxN elements one by one
	# To find all combinations, we consider each element one by one. 
	
	for i in range(1,maxN+1):
		# Map the value to mod 250 value
		value = pow(i,i,250)

		#  Element can be present or not. 
		# If element is not present, we get all the previous combinations
		newArray = list(comboArray)

		# If element is present, we get new combinations by adding the value
		for j in range(modN):
			newValue = (j + value) % modN
			newArray[newValue] = (newArray[newValue]+ comboArray[j]) % Last16Digit

		comboArray = newArray

	# We need to subtract 1, since we don't want the combination when no element is present
	return comboArray[0] - 1
			

print findCombos(250250,250)


