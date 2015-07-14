# https://projecteuler.net/problem=43
#
#

import util
import math



term1 = 1
term2 = 1 

for i in range (3,5000):
	temp = term2
	term2 = term1 + term2  
	term1 = temp

	if (len(str(term2)) > 999):
		print i, " has ", 999, " digits"
		break



