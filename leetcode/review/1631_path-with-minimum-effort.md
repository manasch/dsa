[[1631] - Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort)

---

- Medium
- [Submission](https://leetcode.com/problems/path-with-minimum-effort/submissions/1051172317)
- array, binary-search, depth-first-search, breadth-first-search, union-find, heap-priority-queue, matrix

---

## Problem Statement

<p>You are a hiker preparing for an upcoming hike. You are given <code>heights</code>, a 2D array of size <code>rows x columns</code>, where <code>heights[row][col]</code> represents the height of cell <code>(row, col)</code>. You are situated in the top-left cell, <code>(0, 0)</code>, and you hope to travel to the bottom-right cell, <code>(rows-1, columns-1)</code> (i.e.,&nbsp;<strong>0-indexed</strong>). You can move <strong>up</strong>, <strong>down</strong>, <strong>left</strong>, or <strong>right</strong>, and you wish to find a route that requires the minimum <strong>effort</strong>.</p>



<p>A route&#39;s <strong>effort</strong> is the <strong>maximum absolute difference</strong><strong> </strong>in heights between two consecutive cells of the route.</p>



<p>Return <em>the minimum <strong>effort</strong> required to travel from the top-left cell to the bottom-right cell.</em></p>



<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>



<p><img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/ex1.png" style="width: 300px; height: 300px;" /></p>



<pre>

<strong>Input:</strong> heights = [[1,2,2],[3,8,2],[5,3,5]]

<strong>Output:</strong> 2

<strong>Explanation:</strong> The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.

This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

</pre>



<p><strong class="example">Example 2:</strong></p>



<p><img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/ex2.png" style="width: 300px; height: 300px;" /></p>



<pre>

<strong>Input:</strong> heights = [[1,2,3],[3,8,4],[5,3,5]]

<strong>Output:</strong> 1

<strong>Explanation:</strong> The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

</pre>



<p><strong class="example">Example 3:</strong></p>

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/ex3.png" style="width: 300px; height: 300px;" />

<pre>

<strong>Input:</strong> heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

<strong>Output:</strong> 0

<strong>Explanation:</strong> This route does not require any effort.

</pre>



<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>



<ul>

	<li><code>rows == heights.length</code></li>

	<li><code>columns == heights[i].length</code></li>

	<li><code>1 &lt;= rows, columns &lt;= 100</code></li>

	<li><code>1 &lt;= heights[i][j] &lt;= 10<sup>6</sup></code></li>

</ul>

---

## Solution

```cpp
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        int res = 0;

        vector<int> dxn = {0, 1, 0, -1, 0};
        set<pair<int, int>> visited;
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        pq.push({0, 0, 0});

        while (!pq.empty()) {
            auto [val, i, j] = pq.top();
            pq.pop();

            if (visited.find({i, j}) != visited.end()) {
                continue;
            }
            visited.insert({i, j});
            if (i == m - 1 && j == n - 1) {
                res = val;
                break;
            }

            for (int k = 0; k < 4; ++k) {
                int nx = i + dxn[k];
                int ny = j + dxn[k + 1];
                if (min(nx, ny) < 0 || nx >= m || ny >= n || visited.find({nx, ny}) != visited.end()) {
                    continue;
                }
                int newHeight = max(val, abs(heights[nx][ny] - heights[i][j]));
                pq.push({newHeight, nx, ny});
            }
        }
        return res;
    }
};
```

---

## Notes

- At first glance, it seemed like a dp problem, but in reality it was just a bfs with priority queue, that is it is very similar to djikstra's algorithm.
- Essentially, we try to find the smallest absolute difference path in the list of available cells to visit and visit that, the first time we reach the destination, we have found the smallest maximum absolute difference in the path it took to reach the destination.
- Essentially, for each cell, push the effort it takes to reach its neighbours to the heap, push the max of the effort and the max effort it took to get till here.
- By following a semi-greey approach, we ensure that the greater effort paths are not visited before the lower effort paths.
