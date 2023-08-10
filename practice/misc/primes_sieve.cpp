#include <iostream>
#include <vector>
using namespace std;

void generatePrimes(int n, vector<int>& primes) {
	vector<bool> isPrime(n + 1, true);
	for (int i = 2; i * i <= n; ++i) {
		if (isPrime[i]) {
			for (int j = i * i; j <= n; j += i) {
				isPrime[j] = false;
			}
		}
	}

	for (int i = 0; i <= n; ++i) {
		if (isPrime[i]) {
			primes.push_back(i);
		} 
	}
}

int main() {
	int n;
	cout << "Enter Upper Limit: ";
	cin >> n;

	vector<int> primes;
	generatePrimes(n, primes);

	for (int p: primes) {
		cout << p << " ";
	}
	cout << endl;
	return 0;
}
