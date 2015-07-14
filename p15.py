# https://projecteuler.net/problem=15
#


def factorial(n):
	factorial = 1
	for i in range (1,n):
		factorial *= i
	return factorial


combinations = factorial(20) / (factorial(10)*factorial(10))

print combinations
		
