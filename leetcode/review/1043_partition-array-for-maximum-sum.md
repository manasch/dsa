[[1043] - Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum)

---

- Medium
- [Submission](https://leetcode.com/problems/partition-array-for-maximum-sum/submissions/1164732625/)
- array, dynamic-programming
- Contest: none

---

## Problem Statement

<p>Given an integer array <code>arr</code>, partition the array into (contiguous) subarrays of length <strong>at most</strong> <code>k</code>. After partitioning, each subarray has their values changed to become the maximum value of that subarray.</p>

<p>Return <em>the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,15,7,9,2,5,10], k = 3
<strong>Output:</strong> 84
<strong>Explanation:</strong> arr becomes [15,15,15,9,10,10,10]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
<strong>Output:</strong> 83
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1], k = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(n + 1, -1);

        auto dfs = [&] (auto self, int idx) {
            if (idx >= n) {
                return 0;
            }
            if (dp[idx] != -1) {
                return dp[idx];
            }

            int ans = 0;
            int curMax = 0;
            int end = min(n, idx + k);
            for (int i = idx; i < end; ++i) {
                curMax = max(curMax, arr[i]);
                ans = max(ans, curMax * (i - idx + 1) + self(self, i + 1));
            }
            return dp[idx] = ans;
        };

        return dfs(dfs, 0);
    }
};
```

---

## Notes

- Was able to figure out that it was DP, but unable to get the recurance relationship and instead of thinking of subarrays, went into subsequence.
- In reality, this is very simple, consider each index as the starting index of a new subarray, and go k steps to the right and keep track of the max value.
- If it is decided to end the subarray there and start anew, add the `maxval * subarray length` to the answer and keep moving right.
- Memoize this and it's done.
