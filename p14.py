# https://projecteuler.net/problem=14
#
# 
# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.


import util
import math

SequenceListMax = 1000000
# Keep the sequence length for the first million number
SequenceLengthList = [0]*SequenceListMax
SequenceLengthList[1] = 1


def findCollatzSequenceLength(number):

	if (number < SequenceListMax and SequenceLengthList[number] > 0): 
		return SequenceLengthList[number]

	if (number % 2): 
		newNumber = 3*number + 1
	else : 
		newNumber = number / 2

	length = 1 + findCollatzSequenceLength(newNumber)
	if (number < SequenceListMax): 
		SequenceLengthList[number] = length
	return length



def testFindCollatzSequenceLength():
	assert(findCollatzSequenceLength(13) == 10)
	assert(findCollatzSequenceLength(2) == 2)
	assert(findCollatzSequenceLength(4) == 3)


testFindCollatzSequenceLength()

maxLength = 1
for i in range(2,SequenceListMax):
	length = findCollatzSequenceLength(i)
	if length > maxLength: 
		print " found a new max: ", i, " => " , length
		maxLength = length


