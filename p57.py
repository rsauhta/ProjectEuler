# https://projecteuler.net/problem=57
#

numerator = 1
denominator = 1

counter = 0
for i in range(0,1000):
	newDenominator = numerator + denominator
	newNumerator = newDenominator + denominator
	numerator = newNumerator 
	denominator = newDenominator 
	if len(str(numerator)) > len(str(denominator)):
		counter += 1

print counter
