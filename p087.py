# https://projecteuler.net/problem=87
# Prime power triplets
#
import math
import util

MaxNum = 50*10**6

MaxPrime = int(math.sqrt(MaxNum))

primeStore =  util.PrimeStore(MaxPrime)

squareList = []
cubeList = []
quadList = []


for prime in primeStore:
	power2 = prime*prime
	power3 = power2*prime
	power4 = power3*prime

	if power2 < MaxNum:
		squareList.append(power2)
	if power3 < MaxNum:
		cubeList.append(power3)
	if power4 < MaxNum:
		quadList.append(power4)



count=0
numTracker = [0 for i in range(MaxNum)] 
for power4 in quadList:
	for power3 in cubeList:
		if power4 + power3 >= MaxNum:
			break
		
		for power2 in squareList:
			total = power4 + power3 + power2
			if total >= MaxNum:
				break

			# Only count the first time we set the tracker 
			if numTracker[total] == 0:
				count += 1
				numTracker[total]=1


print count
				







