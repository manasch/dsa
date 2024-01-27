#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  vector<int> subs;
  char last = 'a';
  for (int i = n - 1; i >= 0; --i) {
    if (s[i] >= last) {
      subs.push_back(i);
      last = s[i];
    }
  }

  int count = 0;
  for (int i = 0; i < n; ++i) {
    if (s[i] == last) {
      ++count;
    }
  }

  int m = subs.size();
  for (int i = 0; i < m / 2; ++i) {
    swap(s[subs[i]], s[subs[m - i - 1]]);
  }

  int ans = m - count;
  for (int i = 1; i < n; ++i) {
    if (s[i] < s[i - 1]) {
      ans = -1;
      break;
    }
  }

  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
