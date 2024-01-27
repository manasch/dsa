#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> nums(n);
  for (int i = 0; i < n; ++i) {
    cin >> nums[i];
  }

  int maxNum = INT_MIN;
  int minNum = INT_MAX;
  int maxIdx = -1, minIdx = -1;

  for (int i = 0; i < n; ++i) {
    if (nums[i] > maxNum) {
      maxNum = nums[i];
      maxIdx = i;
    }
    if (nums[i] <= minNum) {
      minNum = nums[i];
      minIdx = i;
    }
  }
  /* for (int i = n - 1; i >= 0; --i) { */
  /*   if (nums[i] >= maxNum) { */
  /*     maxNum = nums[i]; */
  /*     maxIdx = i; */
  /*   } */
  /* } */

  int res = (maxIdx - 0) + (n - 1 - minIdx);
  if (maxIdx > minIdx) {
    --res;
  }
  cout << res << endl;
}

