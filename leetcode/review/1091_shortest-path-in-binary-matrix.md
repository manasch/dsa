[[1091] - Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix)

---

- Medium
- [Submission](https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1005177434/)
- array, breadth-first-search, matrix

---

## Problem Statement

<p>Given an <code>n x n</code> binary matrix <code>grid</code>, return <em>the length of the shortest <strong>clear path</strong> in the matrix</em>. If there is no clear path, return <code>-1</code>.</p>

<p>A <strong>clear path</strong> in a binary matrix is a path from the <strong>top-left</strong> cell (i.e., <code>(0, 0)</code>) to the <strong>bottom-right</strong> cell (i.e., <code>(n - 1, n - 1)</code>) such that:</p>

<ul>
	<li>All the visited cells of the path are <code>0</code>.</li>
	<li>All the adjacent cells of the path are <strong>8-directionally</strong> connected (i.e., they are different and they share an edge or a corner).</li>
</ul>

<p>The <strong>length of a clear path</strong> is the number of visited cells of this path.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example1_1.png" style="width: 500px; height: 234px;" />
<pre>
<strong>Input:</strong> grid = [[0,1],[1,0]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example2_1.png" style="height: 216px; width: 500px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,0],[1,1,0],[1,1,0]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,0,0],[1,1,0],[1,1,0]]
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>grid[i][j] is 0 or 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<vector<int>> q;
        unordered_set<int> visited;
        vector<vector<int>> directions = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0},
            {1, 1},
            {-1, -1},
            {1, -1},
            {-1, 1}
        };

        q.push({0, 0, 1});
        int length, i, j, index;
        vector<int> temp;

        while(!q.empty()) {
            temp = q.front();
            q.pop();
            i = temp[0];
            j = temp[1];
            length = temp[2];
            index = n * i + j;
            if (min(i, j) < 0 || max(i, j) >= n || grid[i][j] || visited.find(index) != visited.end()) {
                continue;
            }
            if (i == n - 1 && j == n - 1) {
                return length;
            }

            visited.insert(index);
            for (auto dxn: directions) {
                q.push({i + dxn[0], j + dxn[1], length + 1});
            }
        }
        return -1;
    }
};
```

---

## Notes

- This was a simple bfs search for the shortest path.
- Initially fumbled in doing the bfs but got it later that I had to have separate pathlengths for each path.
- This is surprisingly slow though, optimizations do exist.
