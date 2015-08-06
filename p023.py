# https://projecteuler.net/problem=23
#

import util

MaxNumToCheck = 28124     # 1 more than max to make range check easier

abundantSum = [0 for x in range(0,MaxNumToCheck)]

abundantList = []

for i in range(1,MaxNumToCheck):
	if (sum(util.GetDivisors(i)) > i):
		abundantList.append(i)

for i in range(0,len(abundantList)):
	for j in range(i,len(abundantList)):
		if (abundantList[i]+abundantList[j] >= MaxNumToCheck):
			break
		abundantSum[abundantList[i]+abundantList[j]]=1

sum = 0
for i in range(0,len(abundantSum)):
	if not abundantSum[i]:
		sum += i

print sum
