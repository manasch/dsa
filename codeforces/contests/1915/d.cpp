#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  string res = "";
  while (!s.empty()) {
    int x;
    if (s.back() == 'a' || s.back() == 'e') {
      x = 2;
    }
    else {
      x = 3;
    }

    while (x--) {
      res.push_back(s.back());
      s.pop_back();
    }
    res.push_back('.');
  }
  res.pop_back();
  reverse(res.begin(), res.end());
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
