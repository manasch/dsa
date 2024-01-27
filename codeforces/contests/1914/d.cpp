#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n, t;
  cin >> n;
  vector<int> a(n), b(n), c(n);
  vector<pair<int, int>> ap, bp, cp;

  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    ap.push_back({a[i], i});
  }

  for (int i = 0; i < n; ++i) {
    cin >> b[i];
    bp.push_back({b[i], i});
  }

  for (int i = 0; i < n; ++i) {
    cin >> c[i];
    cp.push_back({c[i], i});
  }

  sort(ap.begin(), ap.end(), greater<>());
  sort(bp.begin(), bp.end(), greater<>());
  sort(cp.begin(), cp.end(), greater<>());

  int res = 0;
  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < 3; ++j) {
      for (int k = 0; k < 3; ++k) {
        if (ap[i].second != bp[j].second && bp[j].second != cp[k].second && cp[k].second != ap[i].second) {
          res = max(res, ap[i].first + bp[j].first + cp[k].first);
        }
      }
    }
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

