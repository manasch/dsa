#include <bits/stdc++.h>
using namespace std;

char lower_case(char ch) {
  int diff = ch - 'A';
  if (diff < 26) {
    return char(int('a') + diff);
  }
  return ch;
}

int main() {
  string s;
  cin >> s;
  string res = "";

  for (int ch: s) {
    char lower = lower_case(ch);
    if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u' || lower == 'y') {
      continue;
    }
    res.push_back('.');
    res.push_back(lower);
  }
  cout << res << endl;
}
