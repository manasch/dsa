#include <bits/stdc++.h>
using namespace std;

void solve() {
  string s;
  cin >> s;

  int n = s.size();
  int zeroCount = 0;
  for (char ch: s) {
    if (ch == '0') {
      ++zeroCount;
    }
  }
  int oneCount = n - zeroCount;

  int i = 0;
  for (i = 0; i < n; ++i) {
    if (oneCount > 0 && s[i] == '0') {
      --oneCount;
    }
    else if (zeroCount > 0 && s[i] == '1') {
      --zeroCount;
    }
    else {
      break;
    }
  }
  cout << (n - i) << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}

