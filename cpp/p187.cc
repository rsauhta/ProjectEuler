#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

// https://projecteuler.net/problem=187
// Semiprimes
//


typedef unsigned long uint32;  // it will probably be uint64 for 64 bit machine but 32 bit should be enough 
typedef unsigned char uint8;

// Returns number of semiprimes less than supplied max
//
uint32 sieveSemiprimes(uint32 maxN)
{
	uint32 max = int(maxN/2);    // we only need to generate primes upto maxN/2
	
	// allocate array for sieve and init to zero
	uint8 * sieve = (uint8*) malloc(max*sizeof(uint8));
	memset(sieve, 0, max*sizeof(uint8));

	cout << "0 =" << int(sieve[0]) << endl;
	cout << "max =" << int(sieve[max-1]) << endl;


	for (uint32 i=2; i <= int(sqrt(max)); i++) {
		// Not a prime
		if (sieve[i] == 1) continue;

		// For prime, mark all multiples as not prime
		for (uint32 j=2*i; j <= max; j+=i) {
			sieve[j]=1;
		}
	}

	vector<uint32> primeVector;
	for (uint32 i=2; i <= max; i++) {
		if (sieve[i] == 0) {
			primeVector.push_back(i);
		}
	}
	cout << "Size " << primeVector.size() << endl;

	uint32 count = 0;
	for (uint32 i=0; i < primeVector.size(); i++) {
		uint32 prime1 = primeVector[i];
		uint32 maxPrime2 = int(maxN/prime1);

		for (uint32 j=i; j < primeVector.size(); j++) {
			if (primeVector[j] > maxPrime2) {
				break;
			}
			count++;
		}
	}


	return count;

} 
 

int main(int argc, char* argv[]) 
{
   uint32 answer;

   answer = sieveSemiprimes(pow(10,8));
   cout << "Answer = " << answer << endl;
}

