[[1269] - Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps)

---

- Hard
- [Submission](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/submissions/1075656949/)
- dynamic-programming

---

## Problem Statement

<p>You have a pointer at index <code>0</code> in an array of size <code>arrLen</code>. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).</p>

<p>Given two integers <code>steps</code> and <code>arrLen</code>, return the number of ways such that your pointer is still at index <code>0</code> after <strong>exactly</strong> <code>steps</code> steps. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> steps = 3, arrLen = 2
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> steps = 2, arrLen = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> steps = 4, arrLen = 2
<strong>Output:</strong> 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= steps &lt;= 500</code></li>
	<li><code>1 &lt;= arrLen &lt;= 10<sup>6</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int numWays(int steps, int arrLen) {
        const int mod = 1e9 + 7;

        vector<vector<int>> dp(steps + 1, vector<int>(min(steps, arrLen) + 1, -1));

        auto dfs = [&] (auto self, int step, int idx) {
            if (step < 0 || idx < 0 || idx >= arrLen) {
                return 0;
            }
            if (dp[step][idx] != -1) {
                return dp[step][idx];
            }
            if (step == 0) {
                return (idx == 0) ? 1 : 0;
            }
            
            long long count = self(self, step - 1, idx) % mod;
            count += self(self, step - 1, idx - 1) % mod;
            count += self(self, step - 1, idx + 1) % mod;

            dp[step][idx] = count % mod;
            return dp[step][idx];
        };

        return dfs(dfs, steps, 0);
    }
};
```

---

## Notes

- This is a regular 2d DP problem where the steps and the idx are the variables.
- The count is incremented when we reach 0 and the steps are 0, otherwise we can still go left or right or stay.
- Memoise the tree for faster time.
