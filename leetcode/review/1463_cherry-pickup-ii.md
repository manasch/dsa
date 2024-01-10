[[1463] - Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii)

---

- Hard
- [Submission](https://leetcode.com/problems/cherry-pickup-ii/submissions/1142359714/)
- array, dynamic-programming, matrix

---

## Problem Statement

<p>You are given a <code>rows x cols</code> matrix <code>grid</code> representing a field of cherries where <code>grid[i][j]</code> represents the number of cherries that you can collect from the <code>(i, j)</code> cell.</p>

<p>You have two robots that can collect cherries for you:</p>

<ul>
	<li><strong>Robot #1</strong> is located at the <strong>top-left corner</strong> <code>(0, 0)</code>, and</li>
	<li><strong>Robot #2</strong> is located at the <strong>top-right corner</strong> <code>(0, cols - 1)</code>.</li>
</ul>

<p>Return <em>the maximum number of cherries collection using both robots by following the rules below</em>:</p>

<ul>
	<li>From a cell <code>(i, j)</code>, robots can move to cell <code>(i + 1, j - 1)</code>, <code>(i + 1, j)</code>, or <code>(i + 1, j + 1)</code>.</li>
	<li>When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.</li>
	<li>When both robots stay in the same cell, only one takes the cherries.</li>
	<li>Both robots cannot move outside of the grid at any moment.</li>
	<li>Both robots should reach the bottom row in <code>grid</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/29/sample_1_1802.png" style="width: 374px; height: 501px;" />
<pre>
<strong>Input:</strong> grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
<strong>Output:</strong> 24
<strong>Explanation:</strong> Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/23/sample_2_1802.png" style="width: 500px; height: 452px;" />
<pre>
<strong>Input:</strong> grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
<strong>Output:</strong> 28
<strong>Explanation:</strong> Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>rows == grid.length</code></li>
	<li><code>cols == grid[i].length</code></li>
	<li><code>2 &lt;= rows, cols &lt;= 70</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> dxn = {-1, 0, 1};
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(m, -1)));

        auto dfs = [&] (auto self, int i, int j1, int j2) -> int {
            if (min(j1, j2) < 0 || max(j1, j2) >= m) {
                return -1e8;
            }
            if (i == n - 1) {
                if (j1 == j2) {
                    return grid[i][j1];
                }
                return grid[i][j1] + grid[i][j2];
            }
            if (dp[i][j1][j2] != -1) {
                return dp[i][j1][j2];
            }
            int temp = INT_MIN;
            for (int dj1 = 0; dj1 < 3; ++dj1) {
                for (int dj2 = 0; dj2 < 3; ++dj2) {
                    temp = max(temp, self(self, i + 1, j1 + dxn[dj1], j2 + dxn[dj2]));
                }
            }
            if (j1 == j2) {
                return dp[i][j1][j2] = temp + grid[i][j1];
            }
            return dp[i][j1][j2] = temp + grid[i][j1] + grid[i][j2];
        };

        return dfs(dfs, 0, 0, m - 1);
    }
};
```

---

## Notes

- This would basically be 3-d dp, but the dimensions are just determined by the number of changing states.
- This is just a normal 2-d dp but have to maintain two robots at once.
