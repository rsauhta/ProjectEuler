# https://projecteuler.net/problem=249
# Prime subset subms

import util

Last16Digit = 10**16

def findCombos2(primeList, primeStore):
	
	#maxN = sum(primeList)
	#countArray = [0 for i in range(maxN+1)]

	countDict = {}
	countDict[0] = 1

	for prime in primeList: 
		# For each element viz. prime, the elemnt can be present or not
		# If it is not present, we get the original combinatinos.
		#  If it is presnte, we get new combinatoins that we have to add to the dictionary 
		#
		newDict = dict(countDict)
		for value in countDict.keys():
			newValue = value + prime
			if newValue in newDict:
				newDict[newValue] = (newDict[newValue] + countDict[value]) % Last16Digit
			else:
				newDict[newValue] = countDict[value]


		countDict = newDict	
	
	count = 0
	print "size =",len(countDict)
	for key,value in  countDict.iteritems():
		if primeStore.isPrime(key):	
			count = (count+value)%Last16Digit

	return count
			
def findCombos(primeList, primeStore):
	
	maxN = sum(primeList)
	countArray = [0 for i in range(maxN+1)]
	tempArray = [0 for i in range(maxN+1)]

	countArray[0] = 1

	for prime in primeList: 
		# For each element viz. prime, the elemnt can be present or not
		# If it is not present, we get the original combinatinos.
		#  If it is presnte, we get new combinatoins that we have to add to the dictionary 
		#
		for i in range(maxN,-1,-1):
			if countArray[i]:
				newValue = i + prime
				countArray[newValue] = (countArray[newValue] + countArray[i]) % Last16Digit
		'''
		for i in range(maxN+1):
			if countArray[i]:
				newValue = i + prime
				tempArray[newValue] += countArray[i]

		for i in range(maxN+1):
			if tempArray[i]:
				countArray[i] += tempArray[i]
				tempArray[i]=0
		'''
	
	count=0
	for i in range(maxN+1):
		val = countArray[i]
		if val and primeStore.isPrime(i):
			count = (count + val) % Last16Digit

	return count
			

#print findCombos(250250,250)

primeStore = util.PrimeStore(16*10**5)
primeList = []
for prime in primeStore:
	if prime > 5000:
		break
	primeList.append(prime)

print findCombos(primeList, primeStore)


#print len(primeStore)
#print len(primeList)


