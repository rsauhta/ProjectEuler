# https://projecteuler.net/problem=32
#

def isPandigital(panStr, digitLen=9):

	match = False
	if len(panStr) == digitLen:    # exact length
		match = True
		for digit in range(1,digitLen+1):
			if str(digit) not in panStr:
				match=False
	return match


# a*b = c where a > b
#   a cannot be more than 5 digit. if a is 5 digit, b would be 1 digit
#   a cannot be less than 3 digit. if a is 3 digit, b would be 2 or 3 digit 


prodHash = {}
sum = 0
for a in range (111,99999+1):
	for b in range(2,999):
		prod = a*b
		if prod in prodHash:
			continue
		panStr = str(a) + str(b) + str(prod)
		if len(panStr) > 9:	# all future b will only make length longer
			break
		if isPandigital(panStr):
			prodHash[prod]=1
			print a, b, prod
			sum += prod

print sum




		
