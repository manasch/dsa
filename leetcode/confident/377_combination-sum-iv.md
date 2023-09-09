[[377] - Combination Sum IV](https://leetcode.com/problems/combination-sum-iv)

---

- Medium
- [Submission](https://leetcode.com/problems/combination-sum-iv/submissions/1044405803)
- array, dynamic-programming

---

## Problem Statement

<p>Given an array of <strong>distinct</strong> integers <code>nums</code> and a target integer <code>target</code>, return <em>the number of possible combinations that add up to</em>&nbsp;<code>target</code>.</p>

<p>The test cases are generated so that the answer can fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], target = 4
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9], target = 3
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All the elements of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?</p>


---

## Solution

```cpp
class Solution {
private:
    int dfs(vector<int>& nums, unordered_map<int, int>& dp, int current, int target) {
        if (current > target) {
            return 0;
        }
        if (dp.find(current) != dp.end()) {
            return dp[current];
        }
        if (current == target) {
            return 1;
        }
        int count = 0;
        for (int i = 0; i < nums.size(); ++i) {
            count += dfs(nums, dp, current + nums[i], target);
        }
        return dp[current] = count;
    }
public:
    int combinationSum4(vector<int>& nums, int target) {
        unordered_map<int, int> dp;
        return dfs(nums, dp, 0, target);
    }
};
```

---

## Notes

- This is basically similar to coin change, but this time different combinations are possible, so don't have to keep track of the current index.
- Can be done faster bottom-up perhaps.
