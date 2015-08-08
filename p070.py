# https://projecteuler.net/problem=70
# Totient permutation
#
import math
import util
import timeit



def phi(n):
	"Returns totient function for given n"
	factorsDict = util.FindFactor(n)

        # It is easier to compute the opposite of phi
        notPrimeTotal = 0  # count numbers <=n and share at least one factor with n
              
        # Let's say number has prime factor 2, then notPrimeTotal = (n/2)
        # If number has prime factors 2,3   notPrimeTotal = (n/2 + n/3) - (n/6)
        # If number has prime factor 2,3,5  notPrimeTotal = (n/2 + n/3 + n/5) - (n/6+n/10+n/15) + (n/30)
        #   See how each successive row builds on the previous one. We will track that using a two dimensional
        #   array

        grid = []   # A two dimensional array. 1st row contains factor one at a time, second contains factors 2 at a time and so on
                    # We will keep computing notPrimeTotal at the same time
        for factor in factorsDict.keys(): 
                #print "processing", factor, grid

                # work bottom up in the grid to add larger factor combos first since those build on the previous rows
                grid.append([])   
                for i in range(len(grid)-1,0,-1): 
                        # multiply each element of previous row with current factor and add to current row
                        for num in grid[i-1]:
                                newNum = factor*num
                                grid[i].append(newNum)
                                quotient = n/newNum
                                if i%2 == 0:
                                        notPrimeTotal += quotient
                                else:
                                        notPrimeTotal -= quotient

                grid[0].append(factor)
                notPrimeTotal += n/factor


        #print grid
        #print "not primes = ", notPrimeTotal, " for ", n
        return n - notPrimeTotal

                

MaxN = 10**7
util.PopulatePrimeList(int(math.sqrt(MaxN)))

assert(phi(9) == 6)
assert(phi(10) == 4)


for n in range(2,MaxN):
        if n % 10000 == 0: print n
        val = phi(n)


