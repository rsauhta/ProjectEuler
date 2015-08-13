# https://projecteuler.net/problem=78
# Coin partitions
#

# Look up generating function from wiki https://en.wikipedia.org/wiki/Partition_(number_theory)
#

def getPentaNumber(n):
	return (3*n-1)*n/2

pentaList = [0]
for i in range(1,1000): # create a large number of pentagon number
	pentaList.append(getPentaNumber(i))
	pentaList.append(getPentaNumber(-1*i))


# generate number of coin partition and keep building a list
CoinPartitions = []    # index n stores number of partitions for "n" coins
CoinPartitions.append(1)    
CoinPartitions.append(1)

signSeq = [1,1,-1,-1]    # 1st,2nd term have to be added, 3rd,4th have to be subtracted. This sequence is repeated

for n in xrange(2,pentaList[-1]):

	#print "For ", n 
	numPartitions=0
	for index in xrange(1,1000):    # we will break before we get close to the max
		if pentaList[index] > n:    
			break
		sign = signSeq[(index-1) % 4]
		numPartitions += sign * CoinPartitions[ n - pentaList[index]]
		#print "     ", sign, pentaList[index], CoinPartitions[ n - pentaList[index]]

	CoinPartitions.append(numPartitions)
	if numPartitions % 10**6 == 0:
		print " Found answer = ", n
		break
	#print n, "=", CoinPartitions[n]
		


