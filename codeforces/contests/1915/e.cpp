#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve() {
  ll n;
  cin >> n;
  vector<ll> arr(n);
  for (ll i = 0; i < n; ++i) {
    cin >> arr[i];
    if (i & 1) {
      arr[i] = -arr[i];
    }
  }

  map<ll, int> lastSum;
  lastSum[0] = 1;
  ll s = 0;
  for (ll i = 0; i < n; ++i) {
    s += arr[i];
    if (lastSum[s]) {
      cout << "YES\n";
      return;
    }
    ++lastSum[s];
  }
  cout << "NO\n";
}

int main() {
  ll t;
  cin >> t;
  while (t--) {
    solve();
  }
}
