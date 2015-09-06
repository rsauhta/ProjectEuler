# https://projecteuler.net/problem=523
#

'''
Observe that sort proceeds by sorting the first n-1 elements, before tackling
 the last element. 
Let X be the last number in list. Sort the first n-1 elements. Now
- if X is n, we are already sorted.
- if X is 1, we need A(1)=1 steps
- if X is 2, we will need A(2)=2 steps  (1..n,2) -> (2,1..n) -> (1,2,...n)
...
- if X is i, we will need A(i) steps  
	where A(i) is steps needed to sort a list of form (1, 2, 3,...n, i)

E(n) = E(n-1) + sigma(A(i) to n-1) / n
A(i) = 2*A(i-1)

E(n) = n*E(n-1) + (n-1) + sigma( A(i) to n-1)
A(n) = 2*A(n-1) + 1

'''

def computeAnswer(maxN):
	valueA = 1
	sigmaA = 0
	valueE = 0
	
	for i in range(2,maxN+1):
		sigmaA += valueA
		valueE = valueE + float(sigmaA)/i
		valueA *= 2
		#print i,valueA, valueE
	
	return valueE

		

answer=computeAnswer(30)	
print round(answer,2)

