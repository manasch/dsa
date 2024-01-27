#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  cout << 2 << endl;
  int a = n;
  int b = n - 1;
  while (--n) {
    int r = ceil((double)(a + b) / 2);
    cout << a << " " << b << endl;
    b = b - 1;
    a = r;
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
