#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool find(ll num) {
  ll l = 1;
  ll r = 1e9;

  while (l <= r) {
    ll mid = l + ((r - l) >> 1);
    if (mid * mid == num) {
      return true;
    }
    if (mid * mid > num) {
      r = mid - 1;
    }
    else {
      l = mid + 1;
    }
  }
  return false;
}

void solve() {
  ll t, res = 0, s;
  cin >> t;
  while (t--) {
    cin >> s;
    res += s;
  }

  if (find(res)) {
    cout << "YES" << endl;
  }
  else {
    cout << "NO" << endl;
  }
}

int main() {
  ll t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}

