# https://projecteuler.net/problem=54
#

class Poker:
	HighCard, OnePair, TwoPairs, ThreeOfKind, Straight, Flush, FullHouse, FourOfKind, StraightFlush = range(9)


def getPokerValue(hand):
	"Input is a list of 5 cards, with each card represented as a two-tuple (face value, suit)."
	"Output is a 3 tuple (level, value1, value2). "

	# check for flush i.e. all of same suit
	flush = True
	suit = hand[0][1]
	for card in hand:
		if card[1] != suit:
			flush = False
	
	# check for straight ie  consequetive values
	valueList = sorted([x[0] for x in hand])
	straight = True
	for i in range(0,4):
		if valueList[i]+1 != valueList[i+1]:
			straight = False
		

	# straight or flush precludes any other combinations
	if straight and flush:
		value1 = valueList[-1]    # highest card in sequence
		return (Poker.StraightFlush,value1,None)   # value2 doesn't matter

	if flush: 
		value1 = valueList[-1]    # highest card in sequence
		return (Poker.Flush,value1,None)

	if straight: 
		value1 = valueList[-1]    # highest card in sequence
		return (Poker.Straight,value1,None)




	# check of grouping i.e. pair, three or four of a kind
	checkList = list(valueList)

	# Remove any card in front that is not part of group
	highCard=0 			# high card may not always be the largest card in hand e.g. with pair
	while (len(checkList) > 1 and checkList[0] != checkList[1]):
		highCard = max(highCard, checkList[0])
		del(checkList[0])

	if len(checkList) == 1:    # all cards were unique. high card
		highCard = max(highCard, checkList[0])
		return(Poker.HighCard,highCard,None)
	
	# Check the size of the group
	count = 1
	while (len(checkList) > 1 and checkList[0] == checkList[1]):
		del(checkList[0])
		count += 1
	assert(count > 1)
	group1Count = count
	group1Value = checkList[0]
	del(checkList[0])
		

	# Remove any cards that are not part of group
	while (len(checkList) > 1 and checkList[0] != checkList[1]):
		highCard = max(highCard, checkList[0])
		del(checkList[0])

	if len(checkList) == 1: 
		highCard = max(highCard, checkList[0])

	if len(checkList) <= 1:    # There is only one group in this hand
		if group1Count == 2:
			return(Poker.OnePair,group1Value,highCard)
		if group1Count == 3:
			return(Poker.ThreeOfKind,group1Value,highCard)
		if group1Count == 4:
			return(Poker.FourOfKind,group1Value,highCard)
		assert(False)		# should not reach here

	# There must be two groups viz. two pairs or full house
	count = 1
	while (len(checkList) > 1 and checkList[0] == checkList[1]):
		del(checkList[0])
		count += 1
	assert(count > 1)
	group2Count = count
	group2Value = checkList[0]
	del(checkList[0])

	# There can only be one more 
	if len(checkList) == 1: 
		highCard = max(highCard, checkList[0])


	if group1Count > 2:
		return(Poker.FullHouse,group1Value, group2Value)     # value1 is for triplet, value2 is for the pair
	if group2Count > 2:
		return(Poker.FullHouse,group2Value, group1Value) 

	# There must be two pairs
	return(Poker.TwoPairs,max(group1Value,group2Value), min(group1Value,group2Value))     
	

CardLookup = {
	'1' : 1,
	'2' : 2,
	'3' : 3,
	'4' : 4,
	'5' : 5,
	'6' : 6,
	'7' : 7,
	'8' : 8,
	'9' : 9,
	'T' : 10,
	'J' : 11,
	'Q' : 12,
	'K' : 13,
	'A' : 14
}

def splitIntoHands(handStr):
	cardList = [ [CardLookup[str(x)[0]], str(x)[1]] for x in handStr.split()]
	return (cardList[:5], cardList[5:])
	

counter = 0
filename = "p054_poker.txt"	
with open(filename) as f:
	for line in f:
		hand1, hand2 = splitIntoHands(line)
		value1 = getPokerValue(hand1)
		value2 = getPokerValue(hand2)
		#print line.strip(), " => ", value1, value2
		if value1[0] > value2[0]: 
			counter += 1
		if value1[0] == value2[0] and value1[1] > value2[1]:
			counter += 1
		if value1[0] == value2[0] and value1[1] == value2[1] and value1[2] > value2[2]:
			counter += 1
		if value1[0] == value2[0] and value1[1] == value2[1] and value1[2] == value2[2]:
			print line
			assert(False)


print counter

#getPokerValue



