#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  int t;
  cin >> t;
  string s;
  int x = 0;
  while (t--) {
    cin >> s;
    if (s.find("--") != string::npos) {
      --x;
    }
    else {
      ++x;
    }
  }
  cout << x << endl;
}
