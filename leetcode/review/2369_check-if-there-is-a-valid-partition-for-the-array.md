[[2369] - Check if There is a Valid Partition For The Array](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array)

---

- Medium
- [Submission](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/submissions/1019878622/)
- array, dynamic-programming

---

## Problem Statement

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. You have to partition the array into one or more <strong>contiguous</strong> subarrays.</p>

<p>We call a partition of the array <strong>valid</strong> if each of the obtained subarrays satisfies <strong>one</strong> of the following conditions:</p>

<ol>
	<li>The subarray consists of <strong>exactly</strong> <code>2</code> equal elements. For example, the subarray <code>[2,2]</code> is good.</li>
	<li>The subarray consists of <strong>exactly</strong> <code>3</code> equal elements. For example, the subarray <code>[4,4,4]</code> is good.</li>
	<li>The subarray consists of <strong>exactly</strong> <code>3</code> consecutive increasing elements, that is, the difference between adjacent elements is <code>1</code>. For example, the subarray <code>[3,4,5]</code> is good, but the subarray <code>[1,3,5]</code> is not.</li>
</ol>

<p>Return <code>true</code><em> if the array has <strong>at least</strong> one valid partition</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,4,4,5,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no valid partition for this array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    bool dfs(vector<int>& nums, unordered_map<int, bool>& dp, int idx) {
        if (dp.find(idx) != dp.end()) {
            return dp[idx];
        }
        bool ans = false;
        if (idx + 1 < nums.size() && nums[idx] == nums[idx + 1]) {
            ans |= dfs(nums, dp, idx + 2);
        }
        if (idx + 2 < nums.size() && nums[idx] == nums[idx + 1] && nums[idx] == nums[idx + 2]) {
            ans |= dfs(nums, dp, idx + 3);
        }
        if (idx + 2 < nums.size() && nums[idx] == nums[idx + 1] - 1 && nums[idx] == nums[idx + 2] - 2) {
            ans |= dfs(nums, dp, idx + 3);
        }
        dp.insert({idx, ans});
        return ans;
    }
public:
    bool validPartition(vector<int>& nums) {
        unordered_map<int, bool> dp;
        dp[nums.size()] = true;
        return dfs(nums, dp, 0);
    }
};
```

---

## Notes

- Not the most efficient solution, but it worked. Essentially just check if starting from an index, check the three conditions they mentioned.
- Also not sure if the dp actually helped because the submission was very slow compared to other submissions. Ok nevermind, it does seem to help, on the first dfs it caches the future possible partitions.
- The Top-Down approach but iterating reverse results in a similar result.
