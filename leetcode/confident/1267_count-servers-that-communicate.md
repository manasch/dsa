[[1267] - Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate)

---

- Medium
- [Submission](https://leetcode.com/problems/count-servers-that-communicate/submissions/1517890480/)
- array, depth-first-search, breadth-first-search, union-find, matrix, counting
- Contest: none

---

## Problem Statement

<p>You are given a map of a server center, represented as a <code>m * n</code> integer matrix&nbsp;<code>grid</code>, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.<br />
<br />
Return the number of servers&nbsp;that communicate with any other server.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-6.jpg" style="width: 202px; height: 203px;" /></p>

<pre>
<strong>Input:</strong> grid = [[1,0],[0,1]]
<strong>Output:</strong> 0
<b>Explanation:</b>&nbsp;No servers can communicate with others.</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/13/untitled-diagram-4.jpg" style="width: 203px; height: 203px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[1,0],[1,1]]
<strong>Output:</strong> 3
<b>Explanation:</b>&nbsp;All three servers can communicate with at least one other server.
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-1-3.jpg" style="width: 443px; height: 443px;" /></p>

<pre>
<strong>Input:</strong> grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
<strong>Output:</strong> 4
<b>Explanation:</b>&nbsp;The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can&#39;t communicate with any other server.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 250</code></li>
	<li><code>1 &lt;= n &lt;= 250</code></li>
	<li><code>grid[i][j] == 0 or 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<int> countRows(m, 0), countCols(n, 0);

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    ++countRows[i];
                    ++countCols[j];
                }
            }
        }

        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] && (countRows[i] > 1 || countCols[j] > 1)) {
                    ++res;
                }
            }
        }
        return res;
    }
};
```

---

## Notes

- Keep a frequency count of the number of servers in each row and column, if the rowCount or colCount for any index is greater than 1, then increment the result, as this will always ensure that in either the row or col, that server will be able to communicate and hence connected to the network.
