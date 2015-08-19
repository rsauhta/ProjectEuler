# https://projecteuler.net/problem=191
# Prize string
#

# approach is to recursively find the solution and using memoization
#

ComboCache = {}

def findComboCount(daysLeft, absentAllowed=True, lateAllowed=True, onTimeAllowed=True):
	''' 
	Recursive routine to find the number of combinations.
	'''

	lookupStr = str((daysLeft,absentAllowed,lateAllowed,onTimeAllowed))
	if lookupStr in ComboCache:
		return ComboCache[lookupStr]

	if daysLeft < 0:
		return 0

	if daysLeft == 0:
		return 1

	count = 0
	if lateAllowed:
		# Since child is late today, he is allowed to be absent next day
		count += findComboCount(daysLeft-1, True, False,True)

	if absentAllowed: 
		# child is absent for 1 day
		count += findComboCount(daysLeft-1, False, lateAllowed,True)
		# child is absent for 2 days
		count += findComboCount(daysLeft-2, False, lateAllowed,True)
	
	if onTimeAllowed:
		for i in range(1,daysLeft+1):
			# child is on time for next "i" days
			count += findComboCount(daysLeft-i, True, lateAllowed,False)

	ComboCache[lookupStr] = count
	return count

assert(findComboCount(4) == 43)
print findComboCount(30)



