#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  vector<int> a(n, 0), b(n, 0);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> b[i];
  }

  vector<pair<int, int>> p;
  for (int i = 0; i < n; ++i) {
    p.push_back({a[i], b[i]});
  }
  sort(p.begin(), p.end());

  for (int i = 0; i < n; ++i) {
    cout << p[i].first << " ";
  }
  cout << endl;
  for (int i = 0; i < n; ++i) {
    cout << p[i].second << " ";
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
