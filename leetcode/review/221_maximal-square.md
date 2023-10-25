[[221] - Maximal Square](https://leetcode.com/problems/maximal-square)

---

- Medium
- [Submission](https://leetcode.com/problems/maximal-square/submissions/1083739232)
- array, dynamic-programming, matrix

---

## Problem Statement

<p>Given an <code>m x n</code> binary <code>matrix</code> filled with <code>0</code>&#39;s and <code>1</code>&#39;s, <em>find the largest square containing only</em> <code>1</code>&#39;s <em>and return its area</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;" />
<pre>
<strong>Input:</strong> matrix = [[&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],[&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;],[&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;],[&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;" />
<pre>
<strong>Input:</strong> matrix = [[&quot;0&quot;,&quot;1&quot;],[&quot;1&quot;,&quot;0&quot;]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[&quot;0&quot;]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>matrix[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> dp(m, vector<int>(n, -1));
        int res = 0;

        auto dfs = [&] (auto self, int i, int j) {
            if (i >= m || j >= n) {
                return 0;
            }
            if (dp[i][j] != -1) {
                return dp[i][j];
            }
            int right = self(self, i, j + 1);
            int downRight = self(self, i + 1, j + 1);
            int down = self(self, i + 1, j);
            
            dp[i][j] = 0;
            if (matrix[i][j] == '1') {
                dp[i][j] = 1 + min(right, min(downRight, down));
            }
            res = max(res, dp[i][j]);
            return dp[i][j];
        };

        dfs(dfs, 0, 0);
        return pow(res, 2);
    }
};
```

---

## Notes

- Assume each place to be the top-left of a square, find out the max square that can be formed from that cell to its right, bottom right and bottom.
- Cache this data in the traversal and perform normal recursive dp.
