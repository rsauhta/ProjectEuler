# https://projecteuler.net/problem=63
#

counter = 0
for power in range(1,100):
	# if we can't get  raise 9 to power
	if len(str(9**power)) < power:
		break		
	for digit in range(1,10):
		if (len(str(digit**power)) == power):
			counter += 1
	#print power, " = ", counter

print counter
