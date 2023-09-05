[[329] - Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix)

---

- Hard
- [Submission](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/1040978341/)
- array, dynamic-programming, depth-first-search, breadth-first-search, graph, topological-sort, memoization, matrix

---

## Problem Statement

<p>Given an <code>m x n</code> integers <code>matrix</code>, return <em>the length of the longest increasing path in </em><code>matrix</code>.</p>

<p>From each cell, you can either move in four directions: left, right, up, or down. You <strong>may not</strong> move <strong>diagonally</strong> or move <strong>outside the boundary</strong> (i.e., wrap-around is not allowed).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[9,9,4],[6,6,8],[2,1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing path is <code>[1, 2, 6, 9]</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> matrix = [[3,4,5],[3,2,6],[2,2,1]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest increasing path is <code>[3, 4, 5, 6]</code>. Moving diagonally is not allowed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    int m, n;
    vector<int> dxn = {0, 1, 0, -1, 0};
    int dfs(int i, int j, int prev, vector<vector<int>>& matrix, vector<vector<int>>& dp) {
        if (min(i, j) < 0 || i >= m || j >= n) {
            return 0;
        }
        if (matrix[i][j] <= prev) {
            return 0;
        }
        // if (dp.find({i, j}) != dp.end()) {
        //     return dp[{i, j}];
        // }
        if (dp[i][j] != 0) {
            return dp[i][j];
        }
        int maxPath = 1;
        for (int k = 0; k < 4; ++k) {
            maxPath = max(maxPath, 1 + dfs(i + dxn[k], j + dxn[k + 1], matrix[i][j], matrix, dp));
        }
        // return dp[{i, j}] = maxPath;
        return dp[i][j] = maxPath;
    }
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();

        // map<pair<int, int>, int> dp;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int maxPath = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                maxPath = max(maxPath, dfs(i, j, -1, matrix, dp));
            }
        }
        return maxPath;
    }
};
```

---

## Notes

- This was a regular dfs with memoization, at each i, j keep track of the max path it has seen till then so that it can be reused later.
- Not really a hard problem but more on the medium side.
