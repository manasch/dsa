#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  int res = 0;
  while (cin >> s) {
    int l = 0;
    int r = s.size() - 1;
    while (s[l] - '1' > 8 || s[l] - '1' < 1) {
      ++l;
    }
    while (s[r] - '1' > 8 || s[r] - '1' < 1) {
      --r;
    }
    cout << l << r << endl;
  }
  return 0;
}

