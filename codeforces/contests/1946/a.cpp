#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  vector<int> arr(n + 1);

  for (int i = 1; i <= n; ++i) {
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  int med = (n + 1) / 2;
  int idx = med;

  while (idx <= n && arr[idx] == arr[med]) {
    ++idx;
  }

  int res = idx - med;
  cout << res << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
