#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  int t;
  cin >> t;
  while (t--) {
    cin >> a >> b >> c;
    int res = a ^ b ^ c;
    cout << res << endl;
  }
  return 0;
}
