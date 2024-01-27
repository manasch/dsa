#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  
  int prev = -1;
  int curr = 0;
  int res = 1;
  int streak = 0;

  while (n--) {
    cin >> curr;
    if (curr > prev) {
      ++streak;
      res = max(res, streak);
    }
    else {
      streak = 1;
    }
    prev = curr;
  }
  cout << res;
}

