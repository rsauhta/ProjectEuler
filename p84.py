# https://projecteuler.net/problem=84
# Monopoly odds
#

import random

NumSquares = 40


def computeNextSquare(currSquare,sidesInDice):

	
	# make a move and increment counts
	dice1 = random.randint(1,sidesInDice)
	dice2 = random.randint(1,sidesInDice)
	if dice1 == dice2:
		computeNextSquare.numDoubles += 1
	else:
		computeNextSquare.numDoubles = 0

	if computeNextSquare.numDoubles > 2: 
		nextSquare = 10 # if you roll 3 doubles, you go to jail
	else:
		nextSquare = (currSquare + dice1+dice2) % NumSquares

	if nextSquare == 30:  # go to jail square
		nextSquare = 10

	# Community Chest
	if nextSquare == 2 or nextSquare == 17 or nextSquare == 33:
		ccCard = random.randint(1,16)
		if ccCard == 1:
			nextSquare = 0      # proceed to Go
		elif ccCard == 2:
			nextSquare = 10     # go to jail

	# Chance
	if nextSquare == 7 or nextSquare == 22 or nextSquare == 36:
		chCard = random.randint(1,16)
		if chCard == 1:
			nextSquare = 0      # proceed to Go
		elif chCard == 2:
			nextSquare = 10     # go to jail
		elif chCard == 3:
			nextSquare = 11     # go to C1
		elif chCard == 4:
			nextSquare = 24     # go to E3
		elif chCard == 5:
			nextSquare = 39     # go to H2
		elif chCard == 6:
			nextSquare = 5      # go to R1
		elif chCard == 7 or chCard == 8:
			# go to next railway
			if nextSquare == 7: 
				nextSquare = 15
			elif nextSquare == 22:
				nextSquare = 25
			elif nextSquare == 36:
				nextSquare = 5
		elif chCard == 9:
			# go to next utility
			if nextSquare == 22:
				nextSquare = 28
			else:
				nextSquare = 12
		elif chCard == 9:
			nextSquare -= 3

	return nextSquare

computeNextSquare.numDoubles = 0


def runSimulation(numRuns, sidesInDice):
	squareList = [0 for i in range(NumSquares)]
	nextSquare=0
	numDoubles = 0 
	for runCount in xrange(numRuns):
		nextSquare = computeNextSquare(nextSquare, sidesInDice)
		squareList[nextSquare] += 1
					
	
	maxNum = 4  # how many max we want to find
	maxValue = [0 for i in range(maxNum)]
	maxIndex = [0 for i in range(maxNum)]

	for i in range(maxNum): 
		maxValue[i] = max(squareList)
		maxIndex[i] = squareList.index(maxValue[i])
		squareList[maxIndex[i]]=0

	for i in range(maxNum): 
		squareList[maxIndex[i]]=maxValue[i]
		print "Max #", i, maxIndex[i], maxValue[i], float(maxValue[i])*100/numRuns
	
	return str(maxIndex[0]) + str(maxIndex[1]) + str(maxIndex[2])



# Nested simulation was my appraoch to do an successive approximation based on previous result
#  however the answer doesn't converge and keeps bouncing between different top numbers
def runNestedSimulation(numRuns, sidesInDice, probList = None, nestLevel=0):

	if nestLevel > 10:
		return

	if probList == None:
		probList = [10000 for i in range(NumSquares)]
		#probList[0] = numRuns


	squareList = [0 for i in range(NumSquares)]

	for squareIndex in range(NumSquares):
		for i in range(probList[squareIndex]):
			nextSquare = computeNextSquare(squareIndex, sidesInDice)
			squareList[nextSquare] += 1
		
	maxNum = 4  # how many max we want to find
	maxValue = [0 for i in range(maxNum)]
	maxIndex = [0 for i in range(maxNum)]

	for i in range(maxNum): 
		maxValue[i] = max(squareList)
		maxIndex[i] = squareList.index(maxValue[i])
		squareList[maxIndex[i]]=0

	print "Nest level =", nestLevel
	for i in range(maxNum): 
		squareList[maxIndex[i]]=maxValue[i]
		print "    Max #", i, maxIndex[i], maxValue[i], float(maxValue[i])*100/numRuns

	runNestedSimulation(numRuns, sidesInDice, squareList, nestLevel+1)


#runSimulation(10**7, 6)
answer = runSimulation(10**7, 4)
print "Answer=", answer


