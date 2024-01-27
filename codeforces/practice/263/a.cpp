#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  int t = 0;
  int res = 0;
  for (int i = 0; i < 5; ++i) {
    for (int j = 0; j < 5; ++j) {
      cin >> t;
      if (t == 1) {
        res = abs(3 - i - 1) + abs(3 - j - 1);
      }
    }
  }
  cout << res << endl;
  return 0;
}

