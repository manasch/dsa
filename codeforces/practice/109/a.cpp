#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  // 4x + 7y = n;
  int n;
  cin >> n;

  int x, y;
  for (y = (n / 7); y >= 0; --y) {
    if ((n - (7 * y)) % 4 == 0) {
      x = (n - (7 * y)) / 4;
      cout << string(x, '4') + string(y, '7') << endl;
      return 0;
    }
  }
  cout << -1 << endl;
  return 0;
}
