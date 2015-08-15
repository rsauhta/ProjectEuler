# https://projecteuler.net/problem=61
# cyclic figurate number
#

import pprint

# create a dictionary for each type of polygonal number 
#

polyNumbersList = [[] for i in range(6)]

for n in xrange(400):
	tri = n*(n+1)/2
	if tri > 999 and tri < 10000:
		polyNumbersList[0].append(tri)

	square = n*n
	if square > 999 and square < 10000:
		polyNumbersList[1].append(square)

	penta = n*(3*n-1)/2
	if penta > 999 and penta < 10000:
		polyNumbersList[2].append(penta)

	hexa = n*(2*n-1)
	if hexa > 999 and hexa < 10000:
		polyNumbersList[3].append(hexa)

	hepta = n*(5*n-3)/2
	if hepta > 999 and hepta < 10000:
		polyNumbersList[4].append(hepta)


	octa = n*(3*n-2)
	if octa > 999 and octa < 10000:
		polyNumbersList[5].append(octa)

	if tri > 10000:    # if triangle number is over 1000, all other poly numbers must be over too
		#print tri, square, penta, hexa, hepta, hepta, octa
		break

# create dictionary to lookup the words
polyDicts = [{} for i in range(6)]
for poly in range(6):
	for num in polyNumbersList[poly]:
		n2 = num % 100
		n1 = int(num / 100)

		# n1 will always be 2 digit since we picked only 4 digit numbers viz. no leading zero
		# however n2 may reduce to 1 digit e.g. 4801. Skip over these cases since they 
		#   are not going to match with any leading 2 digits
		if n2 < 10: 
			continue
		if n1 not in polyDicts[poly]:
			polyDicts[poly][n1] = []
		polyDicts[poly][n1].append(n2)


def findLoop(polyDicts, numTracker=None, last2Digit=None):
	if not numTracker:
		numTracker = [0 for i in range(6)]

		for first2,last2List in polyDicts[5].iteritems():
			numTracker[5]=first2
			for last2 in last2List:
				if findLoop(polyDicts, numTracker, last2):
					return numTracker

		
	if 0 not in numTracker:
		if last2Digit  == numTracker[5]:  # check if we looped back to start
			return True
		else: 
			return False


	for poly in range(4,-1,-1):   # count backwards since larger poly have fewer elements
				      #  we don't need to test octa since that is the starting point

		if numTracker[poly] != 0:  # we have already used this poly in chain 
			continue
		if last2Digit not in polyDicts[poly]:
			continue 
		
		for next2 in polyDicts[poly][last2Digit]:
			numTracker[poly]=last2Digit
			if findLoop(polyDicts, numTracker, next2):
				return numTracker
		numTracker[poly]=0

	# We tried all combination but this sequence doesn't lead anywhere
	return False	


seq = findLoop(polyDicts)
# Each 2 digit will appear as left 2 digits (multiply by 100) or right 2 digit. So multiply each number by 101 
# and sum to get the answer. Or sum and multiply by 101 
print "Answer =", sum(seq)*101
	




