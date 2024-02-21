[[3040] - Maximum Number of Operations With the Same Score II](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/submissions/1177976536/)
- [Submission](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/submissions/1177976536/)
- array, dynamic-programming, memoization
- Contest: [biweekly-contest-124](https://leetcode.com/contest/biweekly-contest-124)

---

## Problem Statement

<p>Given an array of integers called <code>nums</code>, you can perform <strong>any</strong> of the following operation while <code>nums</code> contains <strong>at least</strong> <code>2</code> elements:</p>

<ul>
	<li>Choose the first two elements of <code>nums</code> and delete them.</li>
	<li>Choose the last two elements of <code>nums</code> and delete them.</li>
	<li>Choose the first and the last elements of <code>nums</code> and delete them.</li>
</ul>

<p>The<strong> score</strong> of the operation is the sum of the deleted elements.</p>

<p>Your task is to find the <strong>maximum</strong> number of operations that can be performed, such that <strong>all operations have the same score</strong>.</p>

<p>Return <em>the <strong>maximum</strong> number of operations possible that satisfy the condition mentioned above</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
- Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
- Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
We are unable to perform any more operations as nums is empty.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,6,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
- Delete the last two elements, with score 1 + 4 = 5, nums = [6].
It can be proven that we can perform at most 2 operations.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---

## Solution

### Contest Submission

```cpp
class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int beg = 0;
        int end = nums.size() - 1;
        int res = 0;
        map<pair<int, pair<int, int>>, int> dp;
        
        auto dfs = [&] (auto self, int start, int fin, int prev, int streak) -> int {
            if (fin - start + 1 < 2) {
                return 0;
            }
            if (dp.find({prev, {start, fin}}) != dp.end()) {
                return dp[{prev, {start, fin}}];
            }
            int temp = 0;
            if (nums[start] + nums[start + 1] == prev) {
                temp = max(1 + self(self, start + 2, fin, prev, streak + 1), temp);
            }
            if (nums[fin] + nums[fin - 1] == prev) {
                temp = max(1 + self(self, start, fin - 2, prev, streak + 1), temp);
            }
            if (nums[start] + nums[fin] == prev) {
                temp = max(1 + self(self, start + 1, fin - 1, prev, streak + 1), temp);
            }
            return dp[{prev, {start, fin}}] = temp;
        };
        
        return max(1 + dfs(dfs, beg + 2, end, nums[beg] + nums[beg + 1], 1), max(
                1 + dfs(dfs, beg, end - 2, nums[end] + nums[end - 1], 1),
                1 + dfs(dfs, beg + 1, end - 1, nums[beg] + nums[end], 1)
            )
        );
    }
};
```

### Later Submissions

```cpp
class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, -1));

        auto dfs = [&] (auto self, int start, int end, int score) -> int {
            if (start >= end) {
                return 0;
            }
            if (dp[start][end] != -1) {
                return dp[start][end];
            }

            int temp = 0;
            if (nums[start] + nums[end] == score) {
                temp = max(temp, 1 + self(self, start + 1, end - 1, score));
            }
            if (nums[start] + nums[start + 1] == score) {
                temp = max(temp, 1 + self(self, start + 2, end, score));
            }
            if (nums[end] + nums[end - 1] == score) {
                temp = max(temp, 1 + self(self, start, end - 2, score));
            }
            return dp[start][end] = temp;
        };

        return max(1 + dfs(dfs, 2, n - 1, nums[0] + nums[1]), max(
            1 + dfs(dfs, 1, n - 2, nums[0] + nums[n - 1]),
            1 + dfs(dfs, 0, n - 3, nums[n - 1] + nums[n - 2])
        ));
    }
};
```

---

## Notes

- Was able to figure out it was DP and also the recurring subproblem.
- The subarray start and end is the recurring subproblem.

- Initial approach used a 3D dp, it worked but was pretty slow, the later submission consists of the 2D dp solution.
- Basically keep on reducing the array size based on the 3 conditions
	- Remove first two.
	- Remove last two.
	- Remove first and last.
- This can only be satistifed if the sum of the removed elements is the same as the starting sum.
- The subarray will be to common subproblem which can be cached.
