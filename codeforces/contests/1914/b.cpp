#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  int a, b;
  while (t--) {
    cin >> a >> b;
    int change = a - b - 1;

    for (int i = 0; i < change; ++i) {
      cout << (a - i) << " ";
    }
    int cnt = 1;
    for (int i = change; i < a; ++i) {
      cout << cnt << " ";
      ++cnt;
    }
    cout << endl;
  }
}

