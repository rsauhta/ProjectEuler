# https://projecteuler.net/problem=71
# Ordered Fractions
#

target = 3.0/7        # we want to be as close as possible but not greater
closestValue = 0      # Track the closest we have been to target. 
closestNumerator = 1  #  numerator for the closest value   
closestDenom = 1      # Denominator for the closest value. I am tracking the denom 
                      #   since we are not reducing the fractions 


for d in range(2,1000001):
        #if d == 7: 
                #continue

        numerator = int(target * d)    # fractional value
        value = float(numerator)/d
        if (value == target): 
                continue

        assert (value < target)
        if value > closestValue:
                closestValue = value
                closestNumerator = numerator
                closestDenom = d


print "Target = ", target, " Value = ", closestValue
print "Denominator = ", closestDenom
print "Numerator = ", closestNumerator
        
