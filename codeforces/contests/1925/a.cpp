#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n, k;
  cin >> n >> k;
  string s = "";
  for (int i = 0; i < k; ++i) {
    s += char(97 + i);
  }
  string ans;
  for (int i = 0; i < n; ++i) {
    ans += s;
  }
  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
