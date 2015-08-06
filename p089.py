# https://projecteuler.net/problem=89
#

RomanDict = {
	"I":1,
	"V":5, 
	"X":10,
	"L":50,
	"C":100,
	"D":500,
	"M":1000
}

def getRomanValue(romanStr):

	romanNum = [RomanDict[x] for x in romanStr]
	maxIndex = len(romanNum)-1

	total = 0
	for index in range(0,maxIndex+1):
		# check for -ve case
		if index < maxIndex  and romanNum[index] < romanNum[index+1]:
			total = total - romanNum[index]
		else: 
			total = total + romanNum[index]
	return total


def getRomanStr(number):
	romanStr = ""

	# Handle 1000s
	romanStr = "M" * int(number/1000)
	number = number % 1000

	assert (number >= 0 and number < 1000)

	# Handle 100s  (M,D,C)
	if number < 400: 
		romanStr += "C" * int(number/100)
		number = number % 100
	elif number < 500:
		romanStr += "CD"
		number = number - 400
	elif number < 900:
		romanStr += "D"
		number = number - 500
		romanStr += "C" * int(number/100)
		number = number % 100
	else:  # number must be 9xy
		romanStr += "CM"
		number = number - 900

	assert (number >= 0 and number < 100)

	# Handle 10s  (C,L,X)
	if number < 40: 
		romanStr += "X" * int(number/10)
		number = number % 10
	elif number < 50:
		romanStr += "XL"
		number = number - 40
	elif number < 90:
		romanStr += "L"
		number = number - 50
		romanStr += "X" * int(number/10)
		number = number % 10
	else:  # number must be 9x
		romanStr += "XC"
		number = number - 90

	assert (number >= 0 and number < 10)

	# Handle units  (X,V,I)
	if number < 4: 
		romanStr += "X" * number
	elif number < 5:
		romanStr += "IV"
	elif number < 9:
		romanStr += "V"
		number = number - 5
		romanStr += "I" * number
	else:  # number must be 9
		romanStr += "IX"

	return romanStr





filename = "p089_roman.txt"

totalSaving = 0
with open(filename) as f:
	for line in f:
		romanString = line.strip()
		value = getRomanValue(romanString)
		newString = getRomanStr(value)

		saving = len(romanString) - len(newString)
		assert(saving >= 0)

		totalSaving += saving

print "Total saving ", totalSaving
			

