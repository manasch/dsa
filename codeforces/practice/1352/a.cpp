#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve() {
  int n;
  cin >> n;
  
  vector<int> nums;
  int power = 1;
  while (n > 0) {
    if (n % 10 > 0) {
      nums.push_back((n % 10) * power);
    }
    n /= 10;
    power *= 10;
  }
  cout << nums.size() << endl;
  for (int num: nums) {
    cout << num << " ";
  }
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}

