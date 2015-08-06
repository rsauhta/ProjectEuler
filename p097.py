# https://projecteuler.net/problem=97
#


lastTenDigit=10**10

answer = 1
for i in range(0,7830457):
	answer = (answer*2) % lastTenDigit

answer = (answer*28433 + 1) % lastTenDigit

print answer
