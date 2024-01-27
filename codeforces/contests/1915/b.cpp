#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    vector<int> count(3, 0);
    char ch;
    for (int i = 0; i < 9; ++i) {
      cin >> ch;
      if (ch == '?') {
        continue;
      }
      ++count[ch - 'A'];
    }
    for (int i = 0; i < 3; ++i) {
      if (count[i] == 2) {
        cout << char(int('A') + i) << endl;
      }
    }
  }
  return 0;
}
