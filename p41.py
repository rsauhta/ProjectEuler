# https://projecteuler.net/problem=41
#

import util



def tryPermutations(digitList):
	recurseList = list(digitList)  # make a copy
	level = len(digitList)
	num = 0
	return tryPermutationsRecurse(recurseList, level, num)

def tryPermutationsRecurse(digitList, level, num):

	if level == 1: # reached the end 
		#print num
		if (util.CheckPrime(num)):
			return num
		else:
			return 0
		
	nextNum = num*10
	for i in range(len(digitList)-1,0,-1):    # Count backwards
		if (digitList[i]): 		# already used
			continue
		else: 
			digitList[i] = 1   # Mark as used and recurse
			result = tryPermutationsRecurse(digitList, level-1, nextNum + i) 
			if result != 0: 
				return result
			digitList[i] = 0   # Mark as used and recurse
		
	return 0


	
	
digitList = [0 for i in range(0,5)]		# 0th entry is not used
assert(tryPermutations(digitList) == 4231)

digitList = [0 for i in range(0,8)]		# n=9 and n=8 panigital would always be divisible by 3
print tryPermutations(digitList)


