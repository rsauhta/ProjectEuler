# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.
#
import timeit

def isStringPalindrome (str):
	return str == str[::-1]

def isNumberPalindrome(n):
	"returns True if n is palindrome"
	return isStringPalindrome(str(n))


def testPalindrome():
	assert isNumberPalindrome(0) == True
	assert isNumberPalindrome(1) == True
	assert isNumberPalindrome(10) == False
	assert isNumberPalindrome(99) == True
	assert isNumberPalindrome(989) == True
	assert isNumberPalindrome(988888889) == True
	assert isNumberPalindrome(987888889) == False

def simple():
	"return largest palindrom number as product of two 3 digit numbers"

	maxPalindrome = 0

	for x in range (100,1000):
		for y in range (100,1000):
			product = x*y
			if (isNumberPalindrome(product)):
				if product > maxPalindrome : 
					maxPalindrome = product
	return maxPalindrome		

# This does run faster but I am not absolutely sure that it will find the 
# maximum in all the cases. for e.g. say for sum 100, there is a palindrome
#  formed by 88*2, but there might be a larger palindrome formed by 45*44
def faster(): 
	"same as simple routine above except try to optimize"

	# try to count down instead of up. Start with the largest product first
	# If x and y are the two numbers, then x+y will range from 2*100 to 
	#   2*999. We can start counting down from 1998. For each sum we can 
	#  check all the ways to break it into x,y and check their products

	for sum in range (2*999, 2*100-1, -1): 
		# We don't want to check 8x9 and 9x8 so we'll  
		#  assume x is always equal or lower than y

		x = int(sum/2)
		for y in range(sum-x, 999):
			if (y >= sum) : 
				break
			x = sum - y
			product = x*y
			if isNumberPalindrome(product):
				return product




#testPalindrome()
max = simple()
print "Time for simple  = ",  \
          timeit.timeit(stmt="simple()",  \
                        setup="from __main__ import simple", \
			number=10)

print "Time for faster  = ",  \
          timeit.timeit(stmt="faster()",  \
                        setup="from __main__ import faster", \
			number=10)


print "Max palindrome = " , max
#assert (max == 906609)

