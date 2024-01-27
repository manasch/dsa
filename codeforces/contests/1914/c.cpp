#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n, k;
  cin >> n >> k;

  vector<int> first(n + 1, 0), second(n + 1, 0);

  for (int i = 1; i <= n; ++i) {
    cin >> first[i];
  }
  for (int i = 1; i <= n; ++i) {
    cin >> second[i];
  }

  for (int i = 2; i <= n; ++i) {
    first[i] += first[i - 1];
    second[i] = max(second[i], second[i - 1]);
  }

  int res = INT_MIN;
  for (int i = 1; i <= min(n, k); ++i) {
    res = max(res, first[i] + (k - i) * second[i]);
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

