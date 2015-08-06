# https://projecteuler.net/problem=151
#

ProbCache = {}

# Add an entry for terminating the last batch
ProbCache[str([5])] = [0.0 for i in range(0,16)]

def findProb(pageList, batchNum=0):
        ''' 
        Compute probability of finding 1 sheet. 
          pageList contains list of pages represented by size (a1=1, a2=2..)

          a list of probability is returned 
             probList[batchNum] is where we will store the probability for current batch
                  values for all batches after this batch will also be stored in probList
             ProbCache is updated with an entry for this combination of pages
        '''

        global probCache


        pageList = sorted(pageList)
        pageListStr = str(pageList)
        if pageListStr in ProbCache:
                return ProbCache[pageListStr]


        probList = [0.0 for i in range(0,16)]

        numPages = len(pageList)
        if numPages == 1:
                probList[batchNum] = 1.0
                assert(pageList[0] < 5)


        for i in range(0,numPages):
                nextList = list(pageList)
                del nextList[i]

                pageSize = pageList[i]
                for nextPage in range(pageSize+1,6):
                        nextList.append(nextPage)

                nextProbList = findProb(nextList, batchNum+1)
                probList = map( lambda x,y: (x+y/numPages), probList, nextProbList)

        ProbCache[pageListStr] = probList
        return probList

                


probList = findProb([1])
answer = sum(probList[1:])    # Don't count first batch
print round(answer,6)         # round to six decimal places

