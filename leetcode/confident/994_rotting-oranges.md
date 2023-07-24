[[994] - Rotting Oranges](https://leetcode.com/problems/rotting-oranges)

---

- Medium
- [Submission](https://leetcode.com/problems/rotting-oranges/submissions/1001626334/)
- array, breadth-first-search, matrix

---

## Problem Statement

<p>You are given an <code>m x n</code> <code>grid</code> where each cell can have one of three values:</p>

<ul>
	<li><code>0</code> representing an empty cell,</li>
	<li><code>1</code> representing a fresh orange, or</li>
	<li><code>2</code> representing a rotten orange.</li>
</ul>

<p>Every minute, any fresh orange that is <strong>4-directionally adjacent</strong> to a rotten orange becomes rotten.</p>

<p>Return <em>the minimum number of minutes that must elapse until no cell has a fresh orange</em>. If <em>this is impossible, return</em> <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/16/oranges.png" style="width: 650px; height: 137px;" />
<pre>
<strong>Input:</strong> grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,2]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are already no fresh oranges at minute 0, the answer is just 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>grid[i][j]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        queue<pair<int, int>> rotten;
        int total = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 2) {
                    rotten.push(pair<int, int>(i, j));
                    ++total;
                }
                else if (grid[i][j] == 1) {
                    ++total;
                }
            }
        }

        int notRotten = total - rotten.size();

        int i, j;
        int time = 0;
        int limit;
        pair<int, int> coord;
        while (!rotten.empty() && notRotten > 0) {
            limit = rotten.size();
            while (limit--) {
                coord = rotten.front();
                rotten.pop();
                i = coord.first;
                j = coord.second;

                notRotten += (bfs(grid, rotten, i - 1, j)
                    + bfs(grid, rotten, i, j + 1)
                    + bfs(grid, rotten, i + 1, j)
                    + bfs(grid, rotten, i, j - 1)
                );
            }
            ++time;
        }
        if (notRotten > 0) {
            return -1;
        }
        return time;
    }
private:
    int m, n;
    int bfs(vector<vector<int>>& grid, queue<pair<int, int>>& rotten, int i, int j) {
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return 0;
        }
        if (grid[i][j] == 2 || grid[i][j] == 0) {
            return 0;
        }
        grid[i][j] = 2;
        rotten.push(pair<int, int>(i, j));
        return -1;
    }
};
```

---

## Notes

- This requires a BFS traversal for every infected orange. For each rotten orange, make its neighbours rotten and add it to a queue.
- At the end if there are any oranges that are not rotten, then it is not possible for all of them to become rotten (not connected 4 directionally).
- I forgot to ensure that the inner while loop has to be executed only a limited number of times and not until the queue was empty. `ref:limit--`
