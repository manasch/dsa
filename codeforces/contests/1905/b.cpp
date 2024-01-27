#include<bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;

  vector<int> ind(n + 1, 0);
  int u, v;
  
  for (int i = 0; i < n - 1; ++i) {
    cin >> u >> v;
    ++ind[u];
    ++ind[v];
  }

  int count = 0;
  for (int i = 1; i <= n; ++i) {
    count += ((ind[i] == 1) ? 1 : 0);
  }

  cout << ceil((double) count / (double) 2) << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}

