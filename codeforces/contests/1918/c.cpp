#include <bits/stdc++.h>
using namespace std;

void solve() {
  int a, b, c;
  cin >> a >> b >> c;

  for (int i = 0; i <= c; ++i) {
    cout << i << ": ";
    cout << (a ^ i) << " - " << (b ^ i) << " = " << abs((a ^ i) - (b ^ i)) << endl;
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
