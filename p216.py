# https://projecteuler.net/problem=216
#
import util

def writeList(inList, filename):
	with open(filename,'w') as f:
		for entry in inList:
			f.write(str(entry))
			f.write("\n")

def readList(filename):
	outList = []
	with open(filename) as f:
		for line in f:
			outList.append(int(line))
	return outList

def checkPrime(maxRange):
	count = 0
	for n in range(2,maxRange+1):
		tn = 2*n*n - 1
		if util.MillerRabin_isPrime(tn):
			count +=1

		if n % 10000 == 0 :
			print n, count

	print "possible primes", count
	return count
	

def genList(maxRange):
	outList = []
	count=0
	for n in range(0,maxRange+1):
		tn = 2*n*n - 1
		if tn % 7 == 0 :
			continue
		if tn % 17 == 0 :
			continue
		outList.append(tn)
	return outList
	

MaxNum = 5*10**7

print checkPrime(MaxNum)

#print "{:,}".format(len(tnList))

'''
count=0
count7=0
Max = 1000
for i in range(1,Max):
	func = 2*i*i-1
	if util.CheckPrime(func):
		#print i, func, 
		#print "Prime"
		a=3
	else:
		count += 1
		factors = util.FindFactor(func)
		print i, func, factors.keys()
		for factor in factors.keys():
			#if factor % 10 == 7:
			if factor  == 7:
				count7 += 1
				break
print "Non prime = ", count
print "Non prime with *7 as factor = ", count7
'''

#writeList(tnList,"216.out")
#tnList = readList("216.out")

#print len(tnList)

