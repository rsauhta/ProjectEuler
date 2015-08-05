# https://projecteuler.net/problem=145
#

def countReversiblesBruteForce(numDigits):
	if numDigits == 1:
		return 0

	startNum = int("1" + "0"*(numDigits-1))
	endNum = int("9"*numDigits)

	counter = 0
	#print "Testing numbers from %d to %d" % (startNum, endNum)
	for num in range(startNum, endNum+1):
		if num % 10 == 0: continue
		add = num + int(str(num)[::-1])

		allOdds=True
		for digit in str(add):
			if int(digit) % 2 == 0:
				allOdds = False
				break
		if allOdds:
			#print "   ", num, add
			counter += 1
	return counter


def getReversible(numDigits, carryIn, carryOut, outermost=False):
	"Return number of combinations, given "
	" number of Digits"
	" carryIn = True means we will have carry coming in, so we will need this digit to even"
	" carryOut = True means we want to generate a carry "

	if (outermost == True):
		assert(carryIn == False)

	if numDigits == 0: 
		if carryIn != carryOut:
			return 0
		else:
			return 1

	if numDigits == 1:
		# For a single digit case, the same digit gets multiplied, so we can never get odd sum 
		#  without a carry coming in
		if carryIn == False:
			return 0       # No way to generate odd 

		if carryOut == False:    # we don't want to generate carry so options are 0,1,2,3,4
			return 5
		else:
			return 5	# carry will be generated with 5,6,7,8,9

	assert(numDigits > 1)   # we should have handled all 1 digit cases above


	if carryIn == False : 	# we need to generate odd number for this position
		# The last digit should be opposite parity of the first digit leading  to  40 or 50 combinations 
		#  depending on whether 0 is allowed or not. 0 is not allowed for outermost digit
		#      (0,2,4,6,8) * (1,3,5,7,9)
		#   The next digit in should not generate a carry, else the sum generated in first digit would become even
		# Out of 40 combinations, 20 generate carry, 20 don't 
		# With 0 included, out of 50 combinations, 20 generate carry, 30 don't 

		if carryOut == True: 
				return 20 * getReversible(numDigits-2, True, False)  # carry out from this digit feeds into next
		else: 
			if outermost:
				return 20 * getReversible(numDigits-2, False, False)  
			else: 
				return 30 * getReversible(numDigits-2, False, False)

	else:   # There is a carry in, so we need to generate even numbers
	        #  Also when we go next level in, that digit will also need to generate carry out

		# no need to test for outermost case viz. without 0
		# Ways to generate even (0,2,4,6,8)x(0,2,4,6,8) + (1,3,5,7,9)x(1,3,5,7,9)
		#   25 with carry, 25 without carry
		#  
		if carryOut == True:
			return 25 * getReversible(numDigits-2, True, True)  # carry out from this digit feeds into next 
		else: 
			return 25 * getReversible(numDigits-2, False, True)
	
	# should never reach here
	assert(False)
		    



def countReversibles(numDigits):
	"Find number of reversible numbers with exactly given numDigits digits"

	return getReversible(numDigits, False, False, True) + getReversible(numDigits, False, True, True)


	

for i in range(1,6):
	assert(countReversiblesBruteForce(i) == countReversibles(i))

total = 0
for i in range(1,10):
	total += countReversibles(i)
print total
