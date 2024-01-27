#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  string res = "";
  int counter = 1;
  int lastCounter = 1;

  for (int i = 0; i < n; ++i) {
    if (counter == 0) {
      res.push_back(s[i - 1]);
      ++lastCounter;
      counter = lastCounter;
    }
    --counter;
  }
  res.push_back(s[n - 1]);

  cout << res << endl;
  return 0;
}

