# https://projecteuler.net/problem=31
#


def countWays(target, coinList, level=0):
	"return number of ways to make target amount using coins"

	level += 1

	if not coinList:		# List is empty. Should not happen
		return 0

	# Pick first (largest denominition) coin 
	currentCoin = coinList[0]
	remainingCoins  = coinList[1:]

	#printStr = "--"*level + "  " + str(target) + ": " + str(currentCoin) 

	if not remainingCoins:
		if (target % currentCoin == 0):	   # can get target amount with this coin
			#print printStr, 1
			return 1 
		else:
			#print printStr, 0
			return 0

	# Handle additional coins with recursion
	numWays = 0
	while (1):
		ways = countWays(target,remainingCoins,level)
		#print printStr, ways
		numWays += ways
		target -= currentCoin
		if (target == 0): 
			#print printStr, 1
			numWays += 1
		if (target <= 0): 
			break
		
	#print printStr, numWays
	return numWays



CoinList = [200,100,50,20,10,5,2,1]
Target = 200


assert(countWays(10, CoinList) == 11)
print countWays(200, CoinList)


