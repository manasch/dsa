#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;

  unordered_map<char, int> freq;
  int l = 0;
  int r = 0;
  int n = s.size();
  while (r < n) {
    ++freq[s[r]];
    if (r - l + 1 == 4) {
      for (auto [k, v]: freq) {
      }
      if (freq.size() == 4) {
        break;
      }
      --freq[s[l]];
      if (freq[s[l]] == 0) {
        freq.erase(s[l]);
      }
      ++l;
    }
    ++r;
  }
  cout << r + 1 << endl;
  return 0;
}

