# https://projecteuler.net/problem=205
# Dice game 
#


def getProbList(diceSides, numDice):
	maxTotal = diceSides * numDice
	probList = [0 for i in range(0,maxTotal+1)]

	diceList = [1 for i in range(0,numDice)]   # start with all dice = 1

	while 1:
		diceTotal = sum(diceList)
		probList[diceTotal] += 1

		# flip through to next dice combinations
		for diceIndex in range(0,numDice):
			diceList[diceIndex] += 1
			if diceList[diceIndex] > diceSides: 
				if diceIndex == numDice-1: 
					break
				diceList[diceIndex] = 1   # continue on to next dice
			else:
				break

		if diceList[-1] > diceSides:   # we have gone through all combinations 
			break
			
	totalCombo = sum(probList)
	assert(totalCombo == diceSides**numDice)

	return [float(x)/totalCombo for x in probList]
		
		
pentaProb = getProbList(4,9)
cubicProb = getProbList(6,6)

cubicCummProb = []
cummProb = 0
for prob in cubicProb:
	cummProb += prob
	cubicCummProb.append(cummProb)


assert(len(pentaProb) == len(cubicCummProb))

probOfWin= 0
for i in range(1,len(pentaProb)):
	probOfWin += pentaProb[i]*cubicCummProb[i-1]

print round(probOfWin,7)

