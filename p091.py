# https://projecteuler.net/problem=91
# Right triangles with integer coordinates
#

# Trying a brute force solution to try all cordinate combinations
# Let two points be (x1,y1) and (x2,y2). Point1 will always be to the 
#   left of point2 viz. x1 <= x2
#   If x1==x2, then y1 < y2
# 
MaxLen=50
total = 0
for x1 in range(0,MaxLen+1):
	for y1 in range(0,MaxLen+1):
		if x1 == y1 == 0: 
			continue 
		len1 = x1*x1 + y1*y1

		for x2 in range(x1,MaxLen+1):
			if x2 == 0: 
				continue
			for y2 in range(0,MaxLen+1):
				if x2 == y2 == 0: 
					continue 
				if y1 == y2 == 0: 
					continue
				if x1 == x2 and y1 >= y2:
					continue

				len2 = x2*x2 + y2*y2

				len3 = (x2-x1)**2 + (y2-y1)**2
				if len1 + len2 == len3 or \
				   len2 + len3 == len1 or \
				   len1 + len3 == len2:
				   	#print x1,y1,x2,y2
					total += 1


print total



