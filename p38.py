# https://projecteuler.net/problem=38
#

def findMaxPandigital(min, max): 

	maxPanNumber = 0
	for i in range(max,min-1,-1):
		panStr = ""
		for k in range(1,9):  	# Multiples
			panStr += str(i*k)
			if len(panStr) > 9: 	# we went over. Try next number
				break		
			if len(panStr) == 9:    # exact length
				match = True
				for digit in range(1,9):
					if str(digit) not in panStr:
						match=False
				if match:
					panNumber = int(panStr)
					if (panNumber > maxPanNumber):
						maxPanNumber = panNumber
			# else length is less than 9. Try adding another multiple

	return maxPanNumber	
				

assert(findMaxPandigital(1,192) == 918273645)
print findMaxPandigital(193,99999)   # Max has to be less than 5 digits

