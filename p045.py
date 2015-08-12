# https://projecteuler.net/problem=45

def getTriangleNum(index):
	return index*(index+1)/2
def getPentaNum(index):
	return index*(3*index-1)/2
def getHexNum(index):
	return index*(2*index-1)


def getMatching(triIndex, pentaIndex, hexIndex):
	triNum = getTriangleNum(triIndex)
	pentaNum = getPentaNum(pentaIndex)
	hexNum = getHexNum(hexIndex)

	while not (triNum == pentaNum == hexNum):
		while (triNum < pentaNum):
			triIndex += 1
			triNum = getTriangleNum(triIndex)
		while (pentaNum < hexNum):
			pentaIndex += 1
			pentaNum = getPentaNum(pentaIndex)
		while (hexNum < triNum):
			hexIndex += 1
			hexNum = getHexNum(hexIndex)
	return (triIndex, pentaIndex, hexIndex)
	

answer = getMatching(2,2,2)
assert(answer == (285,165,143))
answer = getMatching(286,165,143)

print answer
assert(getTriangleNum(answer[0]) == getPentaNum(answer[1]) == getHexNum(answer[2]))
print getTriangleNum(answer[0])

