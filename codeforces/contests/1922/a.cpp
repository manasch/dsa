#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  int t = n;
  string a, b, c;
  cin >> a >> b >> c;

  for (int i = 0; i < n; ++i) {
    if ((a[i] != b[i] && a[i] != c[i] && b[i] != c[i]) || (a[i] == b[i] && a[i] != c[i])) {
      cout << "YES\n";
      return;
    }
  }
  cout << "NO\n";
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
