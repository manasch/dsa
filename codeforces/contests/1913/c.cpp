#include <bits/stdc++.h>
using namespace std;

/* int main() { */
/*   long long t; */
/*   cin >> t; */
/*   long long a = 0; */
/*   long long x, y; */
/*   while (t--) { */
/*     cin >> x >> y; */
/*     if (x == 2) { */
/*       if ((y & a) == y) { */
/*         cout << "YES" << endl; */
/*       } */
/*       else { */
/*         cout << "NO" << endl; */
/*       } */
/*     } */
/*     else { */
/*       a += pow(2, y); */
/*     } */
/*   } */
/* } */

int main() {
  int t;
  cin >> t;
  vector<int> cnt(30);
  int x, y;
  while (t--) {
    cin >> x >> y;
    if (x == 1) {
      ++cnt[y];
    }
    else {
      for (int i = 29; i >= 0; --i) {
        int take = min(y >> i, cnt[i]);
        y -= take << i;
      }
      cout << (y == 0 ? "YES" : "NO") << "\n";
    }
  }
}
