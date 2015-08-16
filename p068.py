# https://projecteuler.net/problem=62
# Magic 5-gon ring
#

# We are only looking for 16 digit combinations, so 10 can not be in the inner nodes.
#  If 10 was in in the inner node, it would get listed twice leading to 17 digits

# For 5-gon ring, inner nodes get counted twice, while other numbers get counted once
# So min sum = (sum(1..10) + sum(1..5))/5 = (55+15)/5 = 14
#   10 is not allowed in inner nodes so max sum is achieved by keeping 5-9 in inner node
#    max sum = (sum(1..10) + sum(5..9))/5 = (55+35)/5 = 18 

# sum for segment n = OuterNodes[n] + InnerNodes[n] + InnerNodes[(n+1)%5]

# We can set OuterNodes[0] to be the smallest of all the outer nodes. This should not restrict any combinations
#   Accordingly OuterNodes[0] can only be in range 1-6. If OuterNodes[0] was 7, 1-6 can not be in outer nodes and 
#   neither could these 6 numbers fit in 5 inner nodes.


def fillSegment(segmentId, total, numUsed, outerNodes, innerNodes):
	global MaxSoFar

	nesting = "    " * segmentId
	#print nesting, "FillSegment = ", segmentId, total, numUsed, outerNodes, innerNodes

	if segmentId == 4:
		if innerNodes[4] + innerNodes[0] + outerNodes[4] != total:
			print "Missed at last step"
			return 

		seq = ""
		for segId in range(0,5):
			seq += str(outerNodes[segId])
			seq += str(innerNodes[segId])
			seq += str(innerNodes[(segId+1)%5])
		print "Answer: ", seq
		exit()

	nextInner = total - outerNodes[segmentId] - innerNodes[segmentId]
	if nextInner < 1 or nextInner > 9 or numUsed[nextInner] == 1:
		#print nesting, "shortcut"
		return
	innerNodes[segmentId+1] = nextInner
	NumUsed[nextInner] = 1

	#print nesting, "set inner to", nextInner

	#for nextOuter in range(OuterNodes[0]+1,11):  # outer nodes should be greater than first one (index 0)
	for nextOuter in range(9,OuterNodes[0],-1)+[10]:  # outer nodes should be greater than first one (index 0)
		if numUsed[nextOuter] == 1:
			continue
			
		#print nesting, "trying next outer", nextOuter
		outerNodes[segmentId+1] = nextOuter
		numUsed[nextOuter] = 1
		# recurse to check the next segment
		fillSegment(segmentId+1, total, numUsed, outerNodes, innerNodes)
		numUsed[nextOuter] = 0
		outerNodes[segmentId+1] = 0


	innerNodes[segmentId+1] = 0    # not needed. just makes debbugging easier
	numUsed[nextInner] = 0


NumUsed = [0 for i in range(0,11)]
OuterNodes = [0 for i in range(0,5)]
InnerNodes = [0 for i in range(0,5)]



# We will look for solution by counting backwards so we get the max solution first. 

for outermost in range(6,0,-1):		# this node has to be the smallest outer node so it has smaller range 
	OuterNodes[0] = outermost
	NumUsed[outermost] = 1

	for innermost in range(9,0,-1):   	# 10 not allowed for inner nodes
		if NumUsed[innermost]: 
			continue
		InnerNodes[0] = innermost
		NumUsed[innermost] = 1

		# Not sure if I should be couting backwars for this too..Given a OuterNodes[0] 
		# and InnerNodes[0], smaller total would ensure a larger InnerNodes[1] so this 
		# order is probably ok
		# I have a suspicion that given a value for OuterNodes[0] and InnerNodes[0], all 
		#  other nodes are pre-determined
		for segTotal in range(14,19):

			# Walk through each semgent, making sure they add up to segTotal
			# Shouldn't need to check the last segment.
			# For each segment: set the missing inner node and outer node for the next segment

			fillSegment(0, segTotal, NumUsed, OuterNodes, InnerNodes)
	
		NumUsed[innermost] = 0
	NumUsed[outermost] = 0

print "Answer = " , MaxSoFar

