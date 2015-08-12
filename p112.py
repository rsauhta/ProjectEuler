# https://projecteuler.net/problem=112
# Bouncy numbers
#


TypeList = ["Bouncy  ","Increase","Decrease", "Both    "]



def printTrackList(tList):
	
	print "Digit ==",
	for i in range(0,10):
		print "%3d" %(i),
  	print 


        for type in range(0,4):
                print TypeList[type],
                for digit in range(0,10):

                        print "%3d" % (tList[digit][type]),
                print
	print


# This was a routine that would have allowed the answer to be computed much faster.
# We track number of bouncy numbers as we add a new digit to left. Once we go over the desired ratio, we would have to 
#  look at the previous digit addition to compute the exact number. 
# Invoke findNum(x) to see how the 3 digit case to get 538 would have worked. 
#   See that when digit 5 is added in the 3rd position, we go over the desired ratio
#   Next if we take the bouncy/total of digit 4 in 3rd position and see the numbers for the previous digit we would 
#     see that adding numbers for 3 in 2nd position to 4 in 3rd position pushes us over the ratio. So we look at the 
#     1st digit. 
#  It is quite convoluted to code all of this properly so I tried the brute force approach and that completed pretty quickly
#    so I shelved this approach. I may come back to it later but it is doesn't seem worth the effort
#

def findNum(ratio):
        "Find the digit positoinnumber when ratio of bouncy to total number goes higher than specified"


        # We will keep track of numbers ending with each digit. Different types are 
        #  stored in a list with the following index : 
        #  0 = Bouncy=0
        #  1 = Increasing=1
        #  2 = Decreasing=2
        #  3 = Both increasing and decreasing e.g. 11
        #  

        # We initialize the tracking list with 1 digit numbers. All these numbers are type both
        TrackList = [[0,0,0,1] for x in range(0,10)]
        #TrackList[0] = [0,0,0,0]                #  There are no numbers ending with 0 for single digit numbers.

        # These counters will track cummulative values seen so far. Initialize for 1 digit numbers
        numBouncy = 0
        numTotal = 9

        totalAddedPerDigit = 10 

	print "Track list for digit position 1"
	printTrackList(TrackList)

        # We will start with 1 digit number and add more digits to the left 
        for pos in range(2,4):    # digit position. 

                newList = [[0,0,0,0] for x in range(0,10)]    
                for leftDigit in range(0,10): 
			tempBouncy = 0

                        # For right digit "d",
                        #    if new left digit is 0 to d-1, then it should be an increasing number. 
                        #    if new left digit = d, then no change to type
                        #    if new left digit is d+1 to 9, then number should be decreasing 

                        # For cases of rightDigit < leftDigit,  we are decreasing
                        for rightDigit in range(0,leftDigit):
                                newList[leftDigit][0] += TrackList[rightDigit][0]   # bouncy cases stay the same
                                tempBouncy += TrackList[rightDigit][0]
                                newList[leftDigit][0] += TrackList[rightDigit][1]   # increasing cases become bouncy
                                tempBouncy += TrackList[rightDigit][1]
                                newList[leftDigit][2] += TrackList[rightDigit][2]   # decreasing cases stay the same
                                newList[leftDigit][2] += TrackList[rightDigit][3]   # "both" case becomes decreasing

                        # If the left digit is same as right, no change to any type
                        newList[leftDigit][0] += TrackList[leftDigit][0] 
                        tempBouncy += TrackList[leftDigit][0]
                        newList[leftDigit][1] += TrackList[leftDigit][1]
                        newList[leftDigit][2] += TrackList[leftDigit][2] 
                        newList[leftDigit][3] += TrackList[leftDigit][3]

                        # For cases of rightDigit > leftDigit,  we are increasing
                        for rightDigit in range(leftDigit+1,10):
                                newList[leftDigit][0] += TrackList[rightDigit][0]   # bouncy cases stay the same
                                tempBouncy += TrackList[rightDigit][0]
                                newList[leftDigit][1] += TrackList[rightDigit][1]   # increasing cases stays the same 
                                newList[leftDigit][0] += TrackList[rightDigit][2]   # decreasing cases becomes bouncy 
                                tempBouncy += TrackList[rightDigit][2]
                                newList[leftDigit][1] += TrackList[rightDigit][3]   # "both" case becomes increasing
                        
                        print "For digit=",leftDigit, 
			print "   ======> bouncy added", tempBouncy, "for total", totalAddedPerDigit,
			if leftDigit > 0:
                        	numTotal += totalAddedPerDigit
				numBouncy += tempBouncy
				print  " %4d %5d %f" % (numBouncy, numTotal, float(numBouncy)/numTotal)
			else:
				print 


                totalAddedPerDigit = totalAddedPerDigit*10
                TrackList = newList

                print "Track List for digit position ", pos
                printTrackList(TrackList)
                print "    Stats =",numBouncy, numTotal, float(numBouncy)/numTotal
                
                                
def isBouncy(n):
	" returns 1 if number is bouncy "

	type = 3  #both 
	rightDigit = n % 10

	while n > 0: 
		currDigit = n % 10 
		#print  "n=",n,"type =",type, "rightDigit=", rightDigit, "currDigit=",currDigit
		n = int(n/10)
		if rightDigit > currDigit:   # increasing case
			if type == 2:     # decreasing becomes bouncy
				return True
			elif type == 3:   # both becomes increasing
				type = 1
			# increasing stays increasing 
			
		if rightDigit <  currDigit:  # decreasing case
			if type == 1:     # increasing becomes bouncy
				return True
			elif type == 3:	  # both becomes decreasing
				type = 2

		rightDigit = currDigit

	#print  "n=",n,"type =",type, "rightDigit=", rightDigit, "currDigit=",currDigit

	return False
	


def findAnswer(ratio):
	
	numBouncy = 0
	n = 99   # start counting from 99 since there are no bouncy below that

	while (float(numBouncy)*100/n != ratio):
		n += 1
		if isBouncy(n):
			numBouncy += 1
	return n
		


                        

assert(isBouncy(55) == False)
assert(isBouncy(231) == True)

assert(findAnswer(50) == 538)
print findAnswer(99)

findNum(1)

