#include <bits/stdc++.h>
using namespace std;

void solve() {
  string s;
  cin >> s;

  int n = s.size();
  int p = n / 2;
  bool flag = true;

  while (p > 0) {
    string firstNum = s.substr(0, p);
    string secondNum = s.substr(p);
    if (secondNum[0] != '0' && stoi(firstNum) < stoi(secondNum)) {
      cout << stoi(firstNum) << " " << stoi(secondNum) << endl;
      flag = false;
      break;
    }
    --p;
  }

  if (flag) {
    cout << -1 << endl;
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
