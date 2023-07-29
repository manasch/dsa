[[64] - Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)

---

- Medium
- [Submission](https://leetcode.com/problems/minimum-path-sum/submissions/1006804115)
- array, dynamic-programming, matrix

---

## Problem Statement

<p>Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6]]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 200</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return dfs(grid, dp, 0, 0);
    }
private:
    int m, n;
    int dfs(vector<vector<int>>& grid, vector<vector<int>>& dp, int i, int j) {
        if (i >= m || j >= n) {
            return INT_MAX;
        }
        if (i == m - 1 && j == n - 1) {
            return grid[i][j];
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        int rightPath = dfs(grid, dp, i, j + 1);
        int downPath = dfs(grid, dp, i + 1, j);
        int minPath = min(rightPath, downPath);
        
        dp[i][j] = grid[i][j] + minPath;
        return dp[i][j];
    }
};
```

---

## Notes

- Apparently the memory usage can be optimized, but otherwise just storing the min path sum till then and using the min of right or down.
