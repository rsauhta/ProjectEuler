# https://projecteuler.net/problem=53
#


# Create a hash of factorial values

factorial = {0:1}
fact = 1
for i in range (1,101):
	fact = fact * i
	factorial[i] = fact

counter = 0
for n in range(1,101):
	for r in range(1,n): 
		combo = factorial[n]/(factorial[n-r]*factorial[r])
		if combo > 1000000:
			#print "%3d %3d = %d" %(n,r,combo)
			counter += 1 

print counter
