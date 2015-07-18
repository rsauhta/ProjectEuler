# https://projecteuler.net/problem=22
#

import re

def alphabeticValue(string):
	value = 0
	for char in string:
		value += ord(char) - ord('A') + 1
	return value
		
	
assert(alphabeticValue("COLIN") == 53)



with open("p022_names.txt") as f: 
	lines = re.split(r'[",]+',f.read())

print len(lines)
lines.sort()

totalValue = 0 
counter=0
for line in lines: 
	if not line: continue 
	counter += 1
	totalValue += counter * alphabeticValue(line)


print "Total value = ", totalValue

