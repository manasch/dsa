#include <bits/stdc++.h>
using namespace std;

void solve() {
  int x, n;
  cin >> x >> n;

  int res = 1;
  int start = x / n;
  for (int i = start; i >= 1; --i) {
    int gcd = i;
    int rem = x - (gcd * n);
    if ((rem % gcd) == 0) {
      res = max(res, gcd);
    }
  }

  cout << res << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}

