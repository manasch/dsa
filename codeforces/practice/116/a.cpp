#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  int t;
  cin >> t;
  int maxCap = 0;
  int current = 0;
  int a, b;
  while (t--) {
    cin >> a >> b;
    current = current - a + b;
    maxCap = max(maxCap, current);
  }
  cout << maxCap << endl;
  return 0;
}

