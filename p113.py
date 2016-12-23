# https://projecteuler.net/problem=113
# Non-bouncy numbers
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

def findNum(numDigits):
        "Find the number of non-bouncy numbers for numbers of numDigits or less "


        # We will keep track of numbers ending with each digit. Different types are 
        #  stored in a list with the following index : 
        #  0 = Bouncy        # actually we are not going to track this since this number will become very large
        #  1 = Increasing
        #  2 = Decreasing
        #  3 = Both increasing and decreasing e.g. 11
        #  

        # We initialize the tracking list with 1 digit numbers. All these numbers are type both
        TrackList = [[0,0,0,1] for x in range(0,10)]

        # These counters will track cummulative values seen so far. Initialize for 1 digit numbers
        nonBouncy = 9

	#print "Track list for digit position 1: non-bouncy=", nonBouncy
	#printTrackList(TrackList)

        # We will start with 1 digit number and add more digits to the left 
        for pos in range(2,numDigits+1):    # digit position. 

		#print "Details for digit position", pos
                newList = [[0,0,0,0] for x in range(0,10)]    
                for leftDigit in range(0,10): 

                        # For new left digit "d",
                        #    if right digit was 0 to d-1, then we are decreasing
                        #    if right digit = d, then there is no change to type
                        #    if right digit was d+1 to 9, then we are incresaing


                        # For cases of rightDigit < leftDigit,  we are decreasing
                        for rightDigit in range(0,leftDigit):
                                newList[leftDigit][2] += TrackList[rightDigit][2]   # decreasing cases stay the same
                                newList[leftDigit][2] += TrackList[rightDigit][3]   # "both" case becomes decreasing

                        # If the left digit is same as right, no change to any type
                        newList[leftDigit][1] += TrackList[leftDigit][1]
                        newList[leftDigit][2] += TrackList[leftDigit][2] 
                        newList[leftDigit][3] += TrackList[leftDigit][3]

                        # For cases of rightDigit > leftDigit,  we are increasing
                        for rightDigit in range(leftDigit+1,10):
                                newList[leftDigit][1] += TrackList[rightDigit][1]   # increasing cases stays the same 
                                newList[leftDigit][1] += TrackList[rightDigit][3]   # "both" case becomes increasing
                        
                        #print "    For digit=",leftDigit, sum(newList[leftDigit])
			if leftDigit != 0:
				nonBouncy += sum(newList[leftDigit])

			#print "   ======> bouncy added", tempBouncy, "for total", totalAddedPerDigit,

		TrackList = newList 
                #printTrackList(TrackList)

	return nonBouncy
                
                                


assert(findNum(6) == 12951)
print findNum(100)
                        
                        



