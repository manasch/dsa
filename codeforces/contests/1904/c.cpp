#include <bits/stdc++.h>
using namespace std;

void solve() {
  long long n, k;
  cin >> n >> k;
  vector<long long> arr;
  for (long long i = 0; i < n; ++i) {
    long long t;
    cin >> t;
    arr.push_back(t);
  }

  if (k >= 3) {
    cout << 0 << endl;
  }
  else {
    sort(arr.begin(), arr.end());
    long long smallest = arr[0];
    for (long long i = 0; i < n - 1; ++i) {
      smallest = min(smallest, arr[i + 1] - arr[i]);
    }

    if (k == 1) {
      cout << smallest << endl;
    }
    else {
      for (long long i = 0; i < n; ++i) {
        for (long long j = 0; j < i; ++j) {
          long long v = arr[i] - arr[j];
          long long p = lower_bound(begin(arr), end(arr), v) - begin(arr);

          // Compare with next
          if (p < n) {
            smallest = min(smallest, arr[p] - v);
          }

          // Compare with previous
          if (p > 0) {
            smallest = min(smallest, v - arr[p - 1]);
          }
        }
      }
      cout << smallest << endl;
    }
  }
}

int main() {
  long long t;
  cin >> t;
  while (t--) {
    solve();
  }
}

