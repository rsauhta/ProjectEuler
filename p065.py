# https://projecteuler.net/problem=65
# Convergent of e
#


def getTermN(n, fractionSequence):
        assert(n <= len(fractionSequence))

        numer = 1
        denom = 0

        for i in range(n-1,-1,-1): # count backwards from the end
                newTerm = fractionSequence[i]

                tempDenom = numer
                numer = newTerm*numer + denom
                denom = tempDenom

        return numer


# Construct sequence of numbers to generate e. We need only the first 100 terms
#
eSequence = [2]
for k in range(1,34):  
        eSequence.append(1)
        eSequence.append(2*k)
        eSequence.append(1)


assert(getTermN(10, eSequence) == 1457)

term =  getTermN(100, eSequence)

digitList = [int(d) for d in str(term)]
print sum(digitList)


