// https://projecteuler.net/problem=243
// Resilience


#include <iostream>
#include <vector>
#include <math.h>
#include "common.h"

using namespace std;



uint32 computeResilience(uint32 numer, uint32 denom)
{
	uint32 max = pow(10,9);   // Answer must lie within first "max" numbers
	
	// allocate array for sieve and initialize to number
	uint32 * sieve = (uint32*) malloc(max*sizeof(uint32));

	for (uint32 i=2; i < max; i++) {
		sieve[i] = i;
	}


	cout << "0 =" << int(sieve[0]) << endl;
	cout << "max =" << int(sieve[max-1]) << endl;


	for (uint32 i=2; i < max; i++) {

		// This is a prime
		if (sieve[i] == i) {
			// For prime, adjust totient for all multiples including this prime
			for (uint32 j=i; j < max; j+=i) {
				sieve[j]= sieve[j] * (i-1) / i;
			}
		}

		// phi has been computed. Do this for prime and non-prime
		// resilience = phi/(i-1) < numer/denom
		if (sieve[i]*denom < numer*(i-1)) {
			return i;
		}
	}

	return 0;
} 
 

int main(int argc, char* argv[]) 
{
   uint32 answer;

   //answer = computeResilience(4, 10);
   answer = computeResilience(15499, 94744);
   cout << "Answer = " << answer << endl;
}

