#include <bits/stdc++.h>
using namespace std;

void solve() {
  string s;
  cin >> s;

  int remove = 0;
  int prev = -1;

  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == '1') {
      if (prev != -1) {
        remove += i - prev - 1;
      }
      prev = i;
    }
  }
  cout << remove << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}

