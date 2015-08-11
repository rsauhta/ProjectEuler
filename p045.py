# https://projecteuler.net/problem=112
# Bouncy numbers
#



def printTrackList(tList):
        for type in range(0,4):
                print "    ",
                for digit in range(0,10):
                        print "%3d" % (tList[digit][type]),
                print



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
        TrackList[0] = [0,0,0,0]                #  There are no numbers ending with 0 for single digit numbers.

        # These counters will track cummulative values seen so far. Initialize for 1 digit numbers
        numBouncy = 0
        numTotal = 9

        totalAddedPerDigit = 9  # If we are adding at 3rd position, each digit will 99


        # We will start with 1 digit number and add more digits to the left 
        for pos in range(2,5):    # digit position. 

                print "Track List for digit position ", pos-1
                printTrackList(TrackList)

                newList = [[0,0,0,0] for x in range(0,10)]    
                for leftDigit in range(1,10): 
                        # For right digit "d",
                        #    if new left digit is 0 to d-1, then it should be an increasing number. 
                        #    if new left digit = d, then no change to type
                        #    if new left digit is d+1 to 9, then number should be decreasing 

                        # For cases of leftDigit < rightDigit,  we are increasing
                        for rightDigit in range(0,leftDigit):
                                newList[leftDigit][0] += TrackList[rightDigit][0]   # bouncy cases stay the same
                                numBouncy += TrackList[rightDigit][0]
                                newList[leftDigit][1] += TrackList[rightDigit][1]   # increasing cases stay the same
                                newList[leftDigit][0] += TrackList[rightDigit][2]   # decreasing cases become bouncy 
                                numBouncy += TrackList[rightDigit][2]
                                newList[leftDigit][0] += TrackList[rightDigit][3]   # "both" case becomes increasing

                        # If the left digit is same as right, no change to any type
                        newList[leftDigit][0] += TrackList[leftDigit][0] 
                        numBouncy += TrackList[leftDigit][0]
                        newList[leftDigit][1] += TrackList[leftDigit][1]
                        newList[leftDigit][2] += TrackList[leftDigit][2] 
                        newList[leftDigit][3] += TrackList[leftDigit][3]

                        # For cases of leftDigit > rightDigit,  we are decreasing
                        for rightDigit in range(leftDigit+1,10):
                                newList[leftDigit][0] += TrackList[rightDigit][0]   # bouncy cases stay the same
                                numBouncy += TrackList[rightDigit][0]
                                newList[leftDigit][0] += TrackList[rightDigit][1]   # increasing cases become bouncy 
                                numBouncy += TrackList[rightDigit][1]
                                newList[leftDigit][2] += TrackList[rightDigit][2]   # decreasing cases stay the same
                                newList[leftDigit][2] += TrackList[rightDigit][3]   # "both" case becomes decreasing
                        
                        numTotal += totalAddedPerDigit
                        print "    digit=",leftDigit, numBouncy, numTotal


                print "new List is "
                printTrackList(newList)
                totalAddedPerDigit = totalAddedPerDigit*10 + 9 
                TrackList = newList
                

                                


                        

findNum(10)

