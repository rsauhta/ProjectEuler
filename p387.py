# https://projecteuler.net/problem=387
# Harshad numbers
#

import util


class HarshadCounter:
	def __init__(self, maxDigits):
		self.maxDigits = maxDigits

	def count(self):
		return self.__handle(1,0,0)

	def __handle(self, digitPos, number, digitSum):
		'''digitPos is position of digit being processed in range(0,maxDigits). 
		   number is the number till now
		   digitSum is sum of digits for the number
		'''

		# Initiliaze before any recursion starts
		if digitPos == 1:
			self.total = 0   # track sum of all matching numbers found 
			
		total = 0

		# Terminate one position before the last digit. Check for the last digit is done 
		#  in the nested loop where we check for primality 
		if digitPos > self.maxDigits-1:   
			return total

		# Recursively build right trunctable Harshad number
		#
		number *= 10

		# iterate through 
		for nextDigit in range(0,10): 
			if digitSum and number % digitSum == 0:            # check for harshad number
				prime = number / digitSum
				if (util.CheckPrime(prime)):  # check for strong harshad number

					# This can be optimized to check primality for all 10 number in 
					#  one go but using utility routine for now
					#
					nextCheck = number*10
					for lastDigit in range(0,10):
						if (util.CheckPrime(nextCheck)):  # check for primes 
							print "  ", nextCheck
							total += nextCheck
						nextCheck += 1

				# recurse deeper to handle number with more digits
				total += self.__handle(digitPos+1, number, digitSum)
		
			# increment the number and sum of digit for next digit
			number += 1
			digitSum += 1
			

		return total



assert(HarshadCounter(4).count() == 90619)
print HarshadCounter(14).count()


