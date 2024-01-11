[[494] - Target Sum](https://leetcode.com/problems/target-sum)

---

- Medium
- [Submission](https://leetcode.com/problems/target-sum/submissions/1036723963/)
- [Submission](https://leetcode.com/problems/target-sum/submissions/1143265427/)
- array, dynamic-programming, backtracking

---

## Problem Statement

<p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>You want to build an <strong>expression</strong> out of nums by adding one of the symbols <code>&#39;+&#39;</code> and <code>&#39;-&#39;</code> before each integer in nums and then concatenate all the integers.</p>

<ul>
	<li>For example, if <code>nums = [2, 1]</code>, you can add a <code>&#39;+&#39;</code> before <code>2</code> and a <code>&#39;-&#39;</code> before <code>1</code> and concatenate them to build the expression <code>&quot;+2-1&quot;</code>.</li>
</ul>

<p>Return the number of different <strong>expressions</strong> that you can build, which evaluates to <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], target = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 1000</code></li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    int dfs(vector<int>& nums, int target, int current, int idx, map<pair<int, int>, int>& dp) {
        if (idx >= nums.size()) {
            if (current == target) {
                return 1;
            }
            else {
                return 0;
            }
        }
        if (dp.find({idx, current}) != dp.end()) {
            return dp[{idx, current}];
        }
        dp[{idx, current}] = dfs(nums, target, current + nums[idx], idx + 1, dp) + dfs(nums, target, current - nums[idx], idx + 1, dp);
        return dp[{idx, current}];
    }
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        map<pair<int, int>, int> dp;
        return dfs(nums, target, 0, 0, dp);
    }
};
```

```cpp
struct Hash {
    template <class T1, class T2>
    size_t operator() (const pair<T1, T2>& p) const {
        return hash<T1>()(p.first) ^ (hash<T2>()(p.second) << 16);
    }
};

class Solution {
private:
    int dfs(vector<int>& nums, int target, int idx, unordered_map<pair<int, int>, int, Hash>& dp) {
        if (idx == 0) {
            if (target == 0 && nums[idx] == 0) {
                return 2;
            }
            if (target == 0 || target == nums[idx]) {
                return 1;
            }
            return 0;
        }
        if (dp.find({idx, target}) != dp.end()) {
            return dp[{idx, target}];
        }
        int notTake = dfs(nums, target, idx - 1, dp);
        int take = 0;
        if (target >= nums[idx]) {
            take = dfs(nums, target - nums[idx], idx - 1, dp);
        }
        return dp[{idx, target}] = take + notTake;
    }
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        if ((totalSum - target) % 2 || (totalSum - target) < 0) {
            return 0;
        }
        int n = nums.size();
        int newTarget = (totalSum - target) / 2;
        unordered_map<pair<int, int>, int, Hash> dp;
        return dfs(nums, newTarget, n - 1, dp);
    }
};
```

---

## Notes

- Normal bruteforce worked which is the regular backtracking solution.
- Caching it decreased the time, but not by much. Can write it in bottom-up DP.

- Covert this problem from figuring out which takes + and which takes - to finding out two subsets S1 and S2 such that S1 - S2 = target.
- From the given array, the total sum can be figured out. This total sum is just the sum of the two subsets S1 and S2.
- Hence, `total = S1 + S2`, `S1 - S2 = target`, just have to find a subset sum of `S2 = (total - target) / 2` from the array.
- There are some exceptions where the `total - target` should be positive and an even number.
- This just reduces to finding a subset sum in an array.
