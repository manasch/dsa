[[417] - Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow)

---

- Medium
- [Submission](https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1000385086/)
- array, depth-first-search, breadth-first-search, matrix

---

## Problem Statement

<p>There is an <code>m x n</code> rectangular island that borders both the <strong>Pacific Ocean</strong> and <strong>Atlantic Ocean</strong>. The <strong>Pacific Ocean</strong> touches the island&#39;s left and top edges, and the <strong>Atlantic Ocean</strong> touches the island&#39;s right and bottom edges.</p>

<p>The island is partitioned into a grid of square cells. You are given an <code>m x n</code> integer matrix <code>heights</code> where <code>heights[r][c]</code> represents the <strong>height above sea level</strong> of the cell at coordinate <code>(r, c)</code>.</p>

<p>The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell&#39;s height is <strong>less than or equal to</strong> the current cell&#39;s height. Water can flow from any cell adjacent to an ocean into the ocean.</p>

<p>Return <em>a <strong>2D list</strong> of grid coordinates </em><code>result</code><em> where </em><code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code><em> denotes that rain water can flow from cell </em><code>(r<sub>i</sub>, c<sub>i</sub>)</code><em> to <strong>both</strong> the Pacific and Atlantic oceans</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" style="width: 400px; height: 400px;" />
<pre>
<strong>Input:</strong> heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
<strong>Output:</strong> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
<strong>Explanation:</strong> The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -&gt; Pacific Ocean 
&nbsp;      [0,4] -&gt; Atlantic Ocean
[1,3]: [1,3] -&gt; [0,3] -&gt; Pacific Ocean 
&nbsp;      [1,3] -&gt; [1,4] -&gt; Atlantic Ocean
[1,4]: [1,4] -&gt; [1,3] -&gt; [0,3] -&gt; Pacific Ocean 
&nbsp;      [1,4] -&gt; Atlantic Ocean
[2,2]: [2,2] -&gt; [1,2] -&gt; [0,2] -&gt; Pacific Ocean 
&nbsp;      [2,2] -&gt; [2,3] -&gt; [2,4] -&gt; Atlantic Ocean
[3,0]: [3,0] -&gt; Pacific Ocean 
&nbsp;      [3,0] -&gt; [4,0] -&gt; Atlantic Ocean
[3,1]: [3,1] -&gt; [3,0] -&gt; Pacific Ocean 
&nbsp;      [3,1] -&gt; [4,1] -&gt; Atlantic Ocean
[4,0]: [4,0] -&gt; Pacific Ocean 
       [4,0] -&gt; Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [[1]]
<strong>Output:</strong> [[0,0]]
<strong>Explanation:</strong> The water can flow from the only cell to the Pacific and Atlantic oceans.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == heights.length</code></li>
	<li><code>n == heights[r].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heights[r][c] &lt;= 10<sup>5</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size();
        n = heights[0].size();
        unordered_set<int> pacificSet;
        unordered_set<int> atlanticSet;

        for (int j = 0; j < n; ++j) {
            findSet(heights, pacificSet, 0, j, -1);
            findSet(heights, atlanticSet, m - 1, j, -1);
        }
        for (int i = 0; i < m; ++i) {
            findSet(heights, pacificSet, i, 0, -1);
            findSet(heights, atlanticSet, i, n - 1, -1);
        }

        vector<vector<int>> result;
        int index;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                index = n * i + j;
                if (pacificSet.find(index) != pacificSet.end() && atlanticSet.find(index) != atlanticSet.end()) {
                    result.push_back({i, j});
                }
            }
        }
        return result;
    }
private:
    int m, n;
    void findSet(vector<vector<int>>& heights, unordered_set<int>& oceanSet, int i, int j, int prevHeight) {
        if (i < 0 || j < 0 || i >= m ||  j >= n) {
            return;
        }
        int index = n * i + j;
        if (oceanSet.find(index) != oceanSet.end()) {
            return;
        }
        if (prevHeight > heights[i][j]) {
            return;
        }

        oceanSet.insert(index);
        findSet(heights, oceanSet, i, j + 1, heights[i][j]);
        findSet(heights, oceanSet, i, j - 1, heights[i][j]);
        findSet(heights, oceanSet, i + 1, j, heights[i][j]);
        findSet(heights, oceanSet, i - 1, j, heights[i][j]);
    }
};
```

---

## Notes

- Trying the brute force approach TLE's on the last test case. [Submission](https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1000353973/).
- Optimizing the problem by storing what can be reached from where during the DFS traversal also supposedly fails.
- The method that worked was starting from the nodes that can visit the pacific, find out all the set that can reach pacific and similarly for the atlantic.
- Finally, find the common coordinates from the two sets.
