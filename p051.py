# https://projecteuler.net/problem=51
# Prime digit replacements
#

import util


def findAnswer(primeList, primeDict):
        " find the lowest prime that creates a family of 8 primes"

        for prime in primeList:

                # count instance of each digit in the prime
		# For every digit we also track the multiple to replace that number.
		#  e..g for 8 in 1828 , we would have 101 as multiple. We can replace 8 by 3 by
		#    p - 8*multiple + 3*multiple
		#
                digitCount=[0 for i in range(0,10)]
		digitMultiple=[0 for i in range(0,10)]
                tmp = prime
		multiple = 1
                while tmp > 0:
                        mod = tmp % 10
                        tmp = int(tmp/10)

                        digitCount[mod] += 1
                        digitMultiple[mod] += multiple
			multiple *= 10


		# check if any digit has 3 instances. 
		# some analysis shows that number of instances being replaced needs to be a multiple 
		#   of 3 viz. 3, 6 or 9. If you replace 2 digits, sum of all digits will become multiple of 
		#   3 more than 2 times= => those replacement instances would be multiple of 3 => not prime
		# It is possible that the first instance found happens to have 4 instance, of which we would 
		#  only replace 3 to get the answer. However I didn't handle that case but routine was able to find 
		#  the right answer 
		# 
                for i in range(0,10):
                        if digitCount[i]==3 or digitCount[i]==6:
				baseNum = prime - digitMultiple[i]*i
        			count = 0
				for k in range(0,10):  # try all digits
					tryNum = baseNum + digitMultiple[i]*k

					# If we put zero as the leading digit, number would 
					#  end up being smaller than prime. That's not allowed
					# k==0 check ensures that we do stringfy only for the case of 
					#  0 replacement
					if k == 0 and  \
					   len(str(tryNum)) < len(str(prime)):
						continue

					if tryNum in primeDict:
						count += 1
				if count >= 8:
					#print "Found match", prime
					for k in range(0,10):  # try all digits
						tryNum = baseNum + digitMultiple[i]*k
						if tryNum in primeDict:
							return tryNum


# start with 6 digit primes 
primeList = util.GetPrimeList(10**6)

primeDict = {}
for p in primeList:
	primeDict[p] = 1


answer=findAnswer(primeList, primeDict)
print "Answer =", answer

