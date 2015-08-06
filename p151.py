# https://projecteuler.net/problem=151
#


def findProb(pageList, probList, probIn, batchNum):
        ''' 
        Compute probability of finding 1 sheet. 
          pageList contains list of pages represented by size (a1=1, a2=2..)
          probList[batchNum] is where we will store the probability
          probIn is probability of this particular event 
        '''

        if batchNum <= 7: 
                print probIn, pageList


        numPages = len(pageList)
        if numPages == 1: 
                # Found 1 page. Add the probability
                probList[batchNum] += probIn
                if pageList[0] == 5:
                        return

        for i in range(0,numPages):
                pageSize = pageList[i]
                newList = pageList[:i] + pageList[i+1:]

                for newPage in range(pageSize+1,6):
                        newList.append(newPage)

                findProb(newList, probList, probIn/numPages, batchNum+1)

        return

                

        

probList = [0 for i in range(0,16)]

findProb([1], probList, 1.0, 0)
print probList
