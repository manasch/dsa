[[695] - Max Area of Island](https://leetcode.com/problems/max-area-of-island)

---

- Medium
- [Submission](https://leetcode.com/problems/max-area-of-island/submissions/1000010021/)
- array, depth-first-search, breadth-first-search, union-find, matrix

---

## Problem Statement

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>&#39;s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>The <strong>area</strong> of an island is the number of cells with a value <code>1</code> in the island.</p>

<p>Return <em>the maximum <strong>area</strong> of an island in </em><code>grid</code>. If there is no island, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        this->m = grid.size();
        this->n = grid[0].size();
        int maxArea = 0;
        int count = 0;
        vector<bool> visited(m * n, false);

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                count = 0;
                maxArea = max(maxArea, islandMass(grid, visited, count, i, j));
            }
        }
        return maxArea;
    }
private:
    int m, n;
    int islandMass(vector<vector<int>>& grid, vector<bool>& visited, int& count, int i, int j) {
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return 0;
        }

        int index = n * i + j;
        if (grid[i][j] == 0 || visited[index]) {
            return 0;
        }

        visited[index] = true;
        ++count;
        islandMass(grid, visited, count, i - 1, j);
        islandMass(grid, visited, count, i, j + 1);
        islandMass(grid, visited, count, i + 1, j);
        islandMass(grid, visited, count, i, j - 1);
        return count;
    }
};
```

---

## Notes

- This is similar to `LC#200`, but just that need to keep a area of the landmass and update the max value evertime a new landmass of larger area is discovered.
