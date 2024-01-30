#include <bits/stdc++.h>
using namespace std;

void solve() {
  int x, y;
  cin >> x >> y;

  int res = x * (y / 2);
  cout << res << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
