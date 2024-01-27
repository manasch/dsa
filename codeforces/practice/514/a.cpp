#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  ll n;
  cin >> n;

  string s = to_string(n);
  ll res = 0, diff;
  for (ll i = 0; i < s.size(); ++i) {
    if (i == 0 && s[i] == '9') {
      res = 9;
      continue;
    }
    diff = s[i] - '0';
    if (diff > 4) {
      res = res * 10 + (9 - diff);
    }
    else {
      res = res * 10 + diff;
    }
  }
  cout << res << endl;
}
