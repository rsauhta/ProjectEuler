# https://projecteuler.net/problem=44
#

def getPentaNum(index):
	return index*(3*index-1)/2

def findClosestPentaOld():
	PentaCount = 1000000    # Hope to find answer within first n pentagon numbers. Count is actually 1 less than this 
	PentaList = [0]       #  first 0th entry is dummy
	PentaHash = {}

	for i in range(1,PentaCount): 
		pentaNum = getPentaNum(i)
		PentaList.append(pentaNum)
		PentaHash[pentaNum] = 1
		
	minDiff = None
	for gap in range(1,500):    # Unlikely we would have to go beyond this gap
		print "Handling gap", gap
		for i in range(1,PentaCount - gap):
			#print "Trying", gap, PentaList[i+gap],PentaList[i]
			pentaDiff = PentaList[i+gap] - PentaList[i]
			pentaSum = PentaList[i+gap] + PentaList[i]

			if minDiff and pentaDiff > minDiff:   # No point in checking further since we have a smaller solution
				if i == 1: 	  # if the very first entry for this gap is too large, no point in checking larger gaps
					return minDiff
				break
			if (pentaSum in PentaHash):	
				print "At least sum is penta", PentaList[i], PentaList[i+gap]
			if (pentaDiff in PentaHash):	
				print "At least diff is penta", PentaList[i], PentaList[i+gap]

			if (pentaDiff in PentaHash and pentaSum in PentaHash):
				print "Found a match", PentaList[i], PentaList[i+gap]
				minDiff = pentaDiff
				break


def findClosestPenta():
	PentaCount = 100000    # Hope to find answer within first n pentagon numbers. Count is actually 1 less than this 
	PentaList = []       
	PentaHash = {}

	for i in range(1,PentaCount): 
		pentaNum = getPentaNum(i)
		PentaList.append(pentaNum)
		PentaHash[pentaNum] = 1
		
	MaxPentaNum = PentaList[-1]

	for pentaDiff in PentaList:
		for penta1 in PentaList:
			penta2 = penta1 + pentaDiff
			if penta2 > MaxPentaNum: 
				break
			if penta2 in PentaHash: 
				#print "Found a potential diff", penta1, penta2
				pentaSum = penta2 + penta1
				if pentaSum > MaxPentaNum: 
					break

				if pentaSum in PentaHash: 
					print "Found a match", pentaDiff, pentaSum, penta1, penta2
					return pentaDiff
	




print findClosestPenta()
