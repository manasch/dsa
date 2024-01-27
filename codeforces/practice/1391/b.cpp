#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n, m;
  cin >> n >> m;

  vector<vector<char>> grid(n, vector<char>(m, 'C'));

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> grid[i][j];
    }
  }

  int count = 0;
  for (int i = 0; i < n - 1; ++i) {
    if (grid[i][m - 1] == 'R') {
      ++count;
    }
  }

  for (int j = 0; j < m - 1; ++j) {
    if (grid[n - 1][j] == 'D') {
      ++count;
    }
  }
  cout << count << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}

