[[200] - Number of Islands](https://leetcode.com/problems/number-of-islands)

---

- Medium
- [Submission](https://leetcode.com/problems/number-of-islands/submissions/999439005/)
- array, depth-first-search, breadth-first-search, union-find, matrix

---

## Problem Statement

<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    vector<bool> visited;
    int m, n;
    void checkIsland(int i, int j, vector<vector<char>>& grid) {
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return;
        }
        int index = n * i + j;
        if (grid[i][j] == '0' || this->visited[index]) {
            return;
        }
        this->visited[index] = true;

        checkIsland(i - 1, j, grid);
        checkIsland(i, j + 1, grid);
        checkIsland(i + 1, j, grid);
        checkIsland(i, j - 1, grid);
    }
    void printVisited() {
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int index = n * i + j;
                cout << i << " " << j << " " << visited[index] << endl;
            }
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        this->m = grid.size();
        this->n = grid[0].size();

        this->visited = vector<bool>(m * n, false);
        int islands = 0;
        int index;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                index = n * i + j;
                if (grid[i][j] != '0' && !this->visited[index]) {
                    ++islands;
                    checkIsland(i, j, grid);
                }
            }
        }
        return islands;
    }
};
```

---

## Notes

- Keep a global visited array, iterate through all the points and only enter one when it hasn't been visited and it is a landmass.
- That way the first time you enter a landmass, you mark all the other land places which can be visited from that landmass as visited, the next time you come across a landmass that hasn't been visited in the parent loop, that would be a new island.
