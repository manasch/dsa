#include <bits/stdc++.h>
using namespace std;

void solve() {
  long long n, t;
  cin >> n;
  vector<pair<long long, long long>> arr;
  for (long long i = 0; i < n; ++i) {
    cin >> t;
    arr.push_back({t, i});
  }

  sort(arr.begin(), arr.end());

  vector<long long> pre(n);
  pre[0] = arr[0].first;

  for (long long i = 1; i < n; ++i) {
    pre[i] = pre[i - 1] + arr[i].first;
  }

  vector<long long> res(n);
  long long nxt = n;
  for (long long i = n - 1; i >= 0; --i) {
    res[arr[i].second] = nxt - 1;
    if (arr[i].first > pre[i - 1]) {
      nxt = i;
    }
  }

  for (long long i = 0; i < n ; ++i) {
    cout << res[i] << " ";
  }
  cout << endl;
}

int main() {
  long long t;
  cin >> t;
  while (t--) {
    solve();
  }
}

