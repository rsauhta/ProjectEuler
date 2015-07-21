# https://projecteuler.net/problem=26
#


# I believe that length of the recurring pattern is same as the number of 9s that is a multiple of 
#  the denominator. eg. for 1/3, 3*3=9 so recurring pattern length is 1. For 1/7, 142857*7=999999
#  so recurring pattern is length is 6 
# In addition to the above, we also need to remove the all factors of 2 and 5. Again all this based
#  on extrapolation, not based on any proof. 


def findSeqLen(n): 

	# remove factors of 2 and 5.
	while (n % 2 == 0): n = n/2
	while (n % 5 == 0): n = n/5
	
	if n == 1: return 0

	sequenceOf9 = 9	
	seqLen=1
	while ( sequenceOf9 % n != 0):
		sequenceOf9 = sequenceOf9*10 + 9 
		seqLen += 1

	return seqLen


maxSeqLen = 0
dForMaxSeq = 0
for i in range(2,1000):
	seqLen = findSeqLen(i)
	#print "%3d %d" % (i,seqLen)
	if seqLen > maxSeqLen: 
		maxSeqLen = seqLen
		dForMaxSeq =  i 

print "d for max seq len = ", dForMaxSeq
