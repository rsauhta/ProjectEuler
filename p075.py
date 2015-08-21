# https://projecteuler.net/problem=75
#  Singular integer right triangle
#
import math 
import fractions

MaxPeri = 1500000
#MaxPeri =  120


periSolutions = [0 for i in range(0,MaxPeri+1)]

# Generate primitive pythagorean triplets
#
maxM=int(math.sqrt(MaxPeri))

for n in range(1,maxM+1):
	# m > n
	# If n is odd, m should be even
	if n % 2 == 1:
		incrM=2
	else:
		incrM=1
	for m in range(n+1,maxM+1,incrM):
		peri = 2*m*(m+n)
		if peri > MaxPeri:
			break
		if fractions.gcd(m,n) > 1:
			continue

		for i in xrange(1,MaxPeri+1):    # max range will be much lesser than MaxPeri
			perimeter = i*peri
			if perimeter > MaxPeri:
				break
			periSolutions[perimeter] += 1

			'''
			if periSolutions[perimeter] > 1:
				print "solution=*", perimeter, i*(m*m-n*n), i*2*m*n,i*(m*m+n*n)
			else:
				print "solution=", perimeter, i*(m*m-n*n), i*2*m*n,i*(m*m+n*n)
			'''

count=0
for elem in periSolutions:
	if elem == 1:
		count +=1

print count 

