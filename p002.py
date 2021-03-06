# https://projecteuler.net/problem=2
#
# Even Fibonacci numbers 
# Problem 2 
# Each new term in the Fibonacci sequence is
# generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
#

class FibIterator:
        def __init__(self, maxAllowed):
                self.a = 1
                self.b = 1
                self.max = maxAllowed
        def __iter__(self):
                return self
        def __next__(self):
                while (self.b <= self.max):
                        temp = self.b
                        self.b += self.a
                        self.a = temp
                        return temp
                raise StopIteration()


def generateFibSum2(maxAllowed):
        return sum(filter(lambda x: x % 2 == 0, FibIterator(maxAllowed)))


# Generates sum of even fibonacci numbers less than "maxAllowed"
#
def generateFibSum(maxAllowed):
        num1 = 1
        num2 = 2
        total = 0

        while (num2 <= maxAllowed) : 
                #print num2
                if (num2 % 2 == 0):
                        total += num2
                temp = num1 + num2
                num1 = num2
                num2 = temp
        
        return total


maxAllowed = 4000000

print("for max range of", maxAllowed, " sum of even fibonacci = ",generateFibSum(maxAllowed))
print("for max range of", maxAllowed, " sum of even fibonacci = ",generateFibSum2(maxAllowed))
