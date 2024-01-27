#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  vector<int> freq(27, 0);

  int count = 0;
  for (int i = 0; i < n; ++i) {
    ++freq[s[i] - 'A' + 1];
  }

  for (int i = 1; i < 27; ++i) {
    if (freq[i] >= i) {
      ++count;
    }
  }

  cout << count << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
