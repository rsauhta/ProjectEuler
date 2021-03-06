
# https://projecteuler.net/problem=1
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#


def matches(num):
    if num % 3 == 0 or num % 5 == 0:
        return num
    else:
        return 0

def answerGenerator(maxInt):
    for i in range(maxInt):
        if i % 3 == 0 or i % 5 == 0:
            yield i


def findAnswer2(max):
    total=0
    for i in answerGenerator(max):
        total += i
    return total

def findAnswer(max):
    total = 0
    for i in range(max):
        total += matches(i)

    return total


assert (findAnswer(10) == 23)
print("For numbers upto 1000: {}".format(findAnswer(1000)))
print("For numbers upto 1000: {}".format(findAnswer2(1000)))