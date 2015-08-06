# https://projecteuler.net/problem=59
#

def decrypt(letterList, passList):
	newList = list(letterList)
	passLen = len(passList)

	for i in range(0,len(newList)):
		newList[i] = newList[i] ^ passList[i%passLen]
	return newList


with open("p059_cipher.txt") as f:
	for line in f:
		letterList = [int(x) for x in line.strip().split(",")]


# Create 3 lists, one for each letter in password, to track number of occurences 
#
countList = [[0 for i in range(0,256)] for i in range(0,3)]
for i in range(0,len(letterList)):
	countList[i%3][letterList[i]] += 1

# Find the letter that occurs the most
#   max(aList)  finds the max
#   aList.index(max(aList))   finds the index with the max, assuming no duplicate max

maxOccurence = [ countList[i].index(max(countList[i])) for i in range(0,3) ] 

# max occurence must be space character
passList = [char ^ ord(' ') for char in maxOccurence]
password = "".join([chr(x) for x in passList])


decrypted = decrypt(letterList, passList)
print "".join([chr(x) for x in decrypted])

print 
print "Password is", password
print "Sum is", sum(decrypted)


