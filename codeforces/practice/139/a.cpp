#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> days(7);
  for (int i = 0; i < days.size(); ++i) {
    cin >> days[i];
  }

  int day = 0;
  while (n - days[day % 7] > 0) {
    n -= days[day % 7];
    ++day;
  }
  int ans = (day % 7) + 1;
  cout << ans << endl;
}

