[[542] - 01 Matrix](https://leetcode.com/problems/01-matrix)

---

- Medium
- [Submission](https://leetcode.com/problems/01-matrix/submissions/1024036946/)
- array, dynamic-programming, breadth-first-search, matrix

---

## Problem Statement

<p>Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the distance of the nearest </em><code>0</code><em> for each cell</em>.</p>

<p>The distance between two adjacent cells is <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[0,0,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[1,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There is at least one <code>0</code> in <code>mat</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        queue<pair<int, int>> q;
        int m = mat.size();
        int n = mat[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 0) {
                    q.push({i, j});
                }
                else {
                    mat[i][j] = -1;
                }
            }
        }

        pair<int, int> p;
        int i, j, r, c, size;
        int len = 0;
        vector<int> xdirs = {1, 0, -1, 0};
        vector<int> ydirs = {0, 1, 0, -1};
        while (!q.empty()) {
            int size = q.size();
            ++len;
            while (size--) {
                p = q.front();
                q.pop();
                i = p.first;
                j = p.second;
                for (int k = 0; k < 4; ++k) {
                    r = i + xdirs[k];
                    c = j + ydirs[k];

                    if (min(r, c) < 0 || r >= m || c >= n || mat[r][c] != -1) {
                        continue;
                    }

                    mat[r][c] = len;
                    q.push({r, c});
                }
            }
        }
        return mat;
    }
};
```

---

## Notes

- Was able to achieve that it had be done at once as performing a BFS for each and every `1` would no doubt lead to TLE. But the idea that a multi-source BFS could be done didn't occur to me. So that is the key here.
- Instead of performing a single source BFS, perform a Multi-source BFS.
- This would be possible by initially adding all the positions that have 0 to a queue, such that all these would be processed at layer 1, and as this is happening, update the cells that contain 1 to some other value that won't occur such that it can be used for later.
- Every time a value is updated, it is because it is `x` levels away from the nearest `0` as this was added in the queue.
- After updating a -1 to the level x, add that to the queue so as to update the -1's existing x + 1 levels away from the nearest 0's.
