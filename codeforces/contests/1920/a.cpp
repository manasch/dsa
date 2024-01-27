#include <bits/stdc++.h>
using namespace std;

void solve() {
  int low = 0;
  int high = INT_MAX;
  vector<int> ignore;

  int n;
  cin >> n;
  int a, b;
  while (n--) {
    cin >> a >> b;
    if (a == 1) {
      low = max(low, b);
    }
    else if (a == 2) {
      high = min(high, b);
    }
    else {
      ignore.push_back(b);
    }
  }

  if (high < low) {
    cout << 0 << endl;
    return;
  }
  int res = high - low + 1;
  for (int &i: ignore) {
    if (i >= low && i <= high) {
      --res;
    }
  }
  if (res < 0) {
    res = 0;
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
