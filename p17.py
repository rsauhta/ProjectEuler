# https://projecteuler.net/problem=17
#



single = [
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
]

teens = [
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen",
]

tens = [
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety",
]

def sum(listInput):
	sum=0
	for num in listInput:
		sum += len(num)
	return sum
	


totalTo99 =  sum(single)    # 1..9
totalTo99 += sum(teens)     # 10..19
totalTo99 += sum(tens)*10 + sum(single)*8   # 20..99

total = totalTo99 * 10 +            \
	sum(single) * 100 +         \
        len("hundred and")*900 +    \
	len("one thousand")            

print total 


