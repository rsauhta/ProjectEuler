# https://projecteuler.net/problem=28
#


def spiralSum(n):
	"sum of numbers on diagonal of the spiral"

	total=1
	num=1
	skip=0
	for side in range (3,n+1,2):
		skip += 2 
		for i in range(0,4):
			num += skip
			total += num
	return total


assert(spiralSum(5) == 101)
print spiralSum(1001)

