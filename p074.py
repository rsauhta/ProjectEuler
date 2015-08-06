
# https://projecteuler.net/problem=74
# Digit factorial chains
#
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

# 169 -> 363601 -> 1454 -> 169
# 871 -> 45361 -> 871
# 872 -> 45362 -> 872
# 
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
# 
# 69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
# 78 -> 45360 -> 871 -> 45361 (-> 871)
# 540 -> 145 (-> 145)
# 
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
# 
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
#

MAX_NUM = 10000000

# Global variables 
TrackList = [0]* MAX_NUM    # Entry i in trackList stores the number of links in 
                            #   chain for that number e.g. trackList[145]=1

TrackList[145] = 1
TrackList[169] = TrackList[36301] = TrackList[1454] = 3 
TrackList[871] = TrackList[45361] = 2 
TrackList[872] = TrackList[45362] = 2 

FactorialList = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def findFactorialSum(n): 
        " give 145, return 1! + 4! + 5!"

        sum = 0
        for digit in str(n): 
                sum += FactorialList[int(digit)]

        return sum

def testFindFactorialSum():
        assert findFactorialSum(145) == 145
        assert findFactorialSum(69) == 363600


def findChains(maxN):
        #  Initialize everything to 0 to indicate value has not been calculated yet

        sixtyCounter = 0  # count sequence 60 link long
        for i in range(1, maxN) : 
                length = findChainLengthFor(i)
                #print i, " ====> ", length
                if ( length == 60):
                        #print "Found 60 length for ", i
                        sixtyCounter += 1
                if (length > 60) : 
                        print "****Error*** got length ", lenght, " for ", i
                        assert(0)

        print "Sixty counter = ", sixtyCounter
        return sixtyCounter




def findChainLengthFor(n):

        if (TrackList[n] > 0) : 
                return TrackList[n]

        sum = findFactorialSum(n)

        # Caller responsible for ensuring that sum won't greater than index in TrackList
        #
        if (sum == n):
                TrackList[n] = 1
        else : 
                TrackList[n] = findChainLengthFor(sum) + 1


        return TrackList[n]

        


testFindFactorialSum()
findChains(1000000)




