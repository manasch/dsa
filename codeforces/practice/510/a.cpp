#include <bits/stdc++.h>
using namespace std;
#define ll long long 

int main() {
  int x, y;
  cin >> x >> y;
  bool last = true;

  for (int i = 0; i < x; ++i) {
    for (int j = 0; j < y; ++j) {
      if (i % 2 == 0) {
        cout << "#";
      }
      else {
        if ((last && j == y - 1) || (!last && j == 0)) {
          /* cout << i << " " << j << endl; */
          cout << "#";
        }
        else {
          cout << ".";
        }
      }
    }
    cout << endl;
    if (i % 2) {
      last = !last;
    }
  }
  return 0;
}

