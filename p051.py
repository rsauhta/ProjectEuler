# https://projecteuler.net/problem=51
# Prime digit replacements
#

import util
import pickle
import timeit

def storePrimes(filename, maxN):
        primeList = util.GetPrimeList(maxN)
        #print primeList
        pFile = open(filename,'wb')
        pickle.dump(primeList,pFile)
        pFile.close()

def readPrime(filename):
        pFile = open(filename, 'rb')
        primeList = pickle.load(pFile)
        pFile.close()
        return primeList


def findAnswer(primeList):
        " find the lowest prime that creates a family of 8 primes"

        count = 0
        for prime in primeList:
                # check if prime has 3 repeating digits
                numDigits=[0 for i in range(0,10)]
                tmp = prime
                while prime > 0:
                        mod = prime % 10
                        numDigits[mod] += 1
                        prime = int(prime/10)
                for i in range(0,10):
                        if numDigits[i]==3:
                                print tmp
                                count += 1
                                if count > 10: 
                                        break



#print findAnswer(8)
#storePrimes(filename, 10**8)
#print "stored" 

filename = "prime.pkl"
primeList = readPrime(filename)
print "done reading"
print len(primeList)
findAnswer(primeList)

#print timeit.timeit('readPrime("prime.pkl")', number=1, setup='from __main__ import readPrime')
        
