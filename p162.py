# https://projecteuler.net/problem=162
# Hexadecimal numbers
#

import math

# I am taking the approach of starting from left most digit and recursing
#  f(16,3,True) => 16 digits, mandatory digits=3 viz. "01A" and  we have constraint of no leading 0
#     13 * f(15,3,False)  => one of 13 non-O1A digit used, constraint of 0 removed
#      2 * f(15,2,False)  => Either 1 or A used so mandatory=2, constraint of 0 removed 
#      1 * f(15,3,True)   => 0 used, so all constraints stay 
# 
#  Note that multiple 13 above is actually (16-mandatory)
#  Also note that if mandatory < 3, zero constraint must no longer be applicable 
#  Recursion can end in following cases
#    f(n,0,False) => 16**n
#    f(3,3,True)  => 4     
#    f(3,3,False) => 6    
#    f(2,2,False) => 2
#    f(1,1,False) => 1
# 


def countValidCombos(digitPositions, mandatoryDigits, zeroFlag=True):
        NumDigits = 16   # 16 possible values for hexadecimal

        if zeroFlag:
                assert(mandatoryDigits == 3)

        if mandatoryDigits == 0:    
                return NumDigits**digitPositions    # any digit allowed for next digitPositions digits

        assert(digitPositions >= mandatoryDigits)

        if digitPositions == mandatoryDigits:        # can't use any non-O1A digits
                if mandatoryDigits == 3  and zeroFlag:
                        return 4
                if mandatoryDigits == 3:
                        return 6
                if mandatoryDigits == 2:
                        return 2
                if mandatoryDigits == 1:
                        return 1

                assert(False)  # should never reach here


        count = 0
        count += (NumDigits-mandatoryDigits) * countValidCombos(digitPositions-1, mandatoryDigits, False)
        if zeroFlag: 
                count += 2*countValidCombos(digitPositions-1, mandatoryDigits-1, False)  # Use 1 or A for current digit
                count += countValidCombos(digitPositions-1, mandatoryDigits, True)       # Use 0 for current digit
        else:
                count += mandatoryDigits * countValidCombos(digitPositions-1, mandatoryDigits-1, False)


        return count


answer = countValidCombos(16,3)
print "%X" % (answer)

