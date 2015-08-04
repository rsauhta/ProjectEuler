# https://projecteuler.net/problem=85
#

import math

def getNumRectangles(width, height):
        return width*(width+1)*height*(height+1)/4

def getOtherDimension(x, total):
        "Given total and one dimension (height or width), find the other dimension"
        return int(math.sqrt(total*4/(x*(x+1))))



DesiredTotal = 2000000
closestGap =  2000000    # seed value
areaForClosestGap = 0

for width in xrange(1,getOtherDimension(1, DesiredTotal)):
        height = getOtherDimension(width, DesiredTotal)
        total = getNumRectangles(width,height)
        diff = abs(DesiredTotal - total)
        if diff < closestGap:
                closestGap = diff
                areaForClosestGap = height*width
                
print areaForClosestGap 
                
