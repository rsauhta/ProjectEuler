# https://projecteuler.net/problem=31
#

DebugPrint = False
def printCoins(coinHash):
	if not DebugPrint:
		return
	for coin in sorted(coinHash.keys()):
		print "%3d:%3d " % (coin, coinHash[coin]),
	print	

def countWays(target, coinList, coinHash = {}):
	"return number of ways to make target amount using coins"

	if not coinList:		# List is empty. Should not happen
		return 0

	# Pick first (largest denominition) coin 
	currentCoin = coinList[0]
	remainingCoins  = coinList[1:]
	coinHash[currentCoin] = 0

	if not remainingCoins:
		if (target % currentCoin == 0):	   # can get target amount with this coin
			#print printStr, 1
			coinHash[currentCoin] = target/currentCoin
			printCoins(coinHash)
			coinHash[currentCoin] = 0
			return 1 
		else:
			return 0

	# Handle additional coins with recursion
	numWays = 0
	while (1):
		ways = countWays(target,remainingCoins,coinHash)
		numWays += ways
		target -= currentCoin
		coinHash[currentCoin] += 1
		if (target == 0): 
			printCoins(coinHash)
			numWays += 1
		if (target <= 0): 
			break
		
	coinHash[currentCoin] = 0
	return numWays



CoinList = [200,100,50,20,10,5,2,1]
Target = 200

CoinHash = {}
for coin in CoinList:
	CoinHash[coin]=0

assert(countWays(10, CoinList,CoinHash) == 11)
#DebugPrint = True
print countWays(200, CoinList)


