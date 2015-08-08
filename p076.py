# https://projecteuler.net/problem=76
# Counting summation
#

def findNumWays(n):
        return _findNumWays(n,n-1)   

NumWayCache={}

def _findNumWays(n, maxAllowed):
        # we have to split "n" into multiple numbers that sum upto n
        # Arrange terms in sum in sorted order
        # Try various values for the first element. To compute others elements, recurse with the constraint
        #   that next elements can't be greater than the first element

        # Only one way to break numbers into all 1s
        #   maxAllowed and n can be set to 0 for terminating conditions
        if maxAllowed <= 1: 
                return 1

        cacheKey = str((n,maxAllowed))
        if cacheKey in NumWayCache:
                return NumWayCache[cacheKey]

        numWays = 0
        for first in range(1,maxAllowed+1):
                leftover = n - first
                numWays += _findNumWays(leftover, min(first, leftover))

        NumWayCache[cacheKey] = numWays
        return numWays


assert(findNumWays(5) == 6)
print findNumWays(100)
