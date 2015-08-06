# https://projecteuler.net/problem=33
#

numerator = 1
denominator = 1

for commonDigit in range(1,10):   # 1 to 9. 
	for digitA in range(1,10):
		for digitB in range(1,10):
			if digitB == digitA:
				continue
			if float(digitA)/digitB >= 1.0:
				continue
			if float(digitA)/digitB == float(digitA*10+commonDigit)/(commonDigit*10+digitB) or \
			   float(digitA/digitB) == float(commonDigit*10+digitA)/(digitB*10+commonDigit):
				#print "match", str(digitA)+str(commonDigit), "/" , str(commonDigit)+str(digitB)
				#print "match", digitA, digitB
				numerator *= digitA
				denominator *= digitB

print numerator, denominator 


