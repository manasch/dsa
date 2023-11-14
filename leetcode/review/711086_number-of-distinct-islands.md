[[711086] - Number of Distinct Islands](https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1)

---

- Medium
- DFS, Graph, BFS, Data Structures, Algorithms
- 

---

## Problem Statement

<p><span style="font-size:14px">Given a boolean 2D matrix <strong>grid&nbsp;</strong>of size <strong>n</strong> * <strong>m</strong>. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).</span></p>

<p><strong><span style="font-size:14px">Example 1:</span></strong></p>

<pre>
<span style="font-size:14px"><strong>Input:</strong></span>
<span style="font-size:14px">grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}</span>
<span style="font-size:14px"><strong>Output:</strong></span>
<span style="font-size:14px">1</span>
<span style="font-size:14px"><strong>Explanation:</strong></span>
<span style="font-size:14px">grid[][] = {{<span style="color:#ff0000">1</span>, <span style="color:#ff0000">1</span>, 0, 0, 0}, 
&nbsp;           {<span style="color:#ff0000">1</span>, <span style="color:#ff0000">1</span>, 0, 0, 0}, 
&nbsp;           {0, 0, 0, <span style="color:#ff0000">1</span>, <span style="color:#ff0000">1</span>}, 
&nbsp;           {0, 0, 0, <span style="color:#ff0000">1</span>, <span style="color:#ff0000">1</span>}}
Same colored islands are equal.
We have 2 equal islands, so we 
have only 1 distinct island.</span>

</pre>

<p><strong><span style="font-size:14px">Example 2:</span></strong></p>

<pre>
<span style="font-size:14px"><strong>Input:</strong></span>
<span style="font-size:14px">grid[][] = {{1, 1, 0, 1, 1},
&nbsp;           {1, 0, 0, 0, 0},
&nbsp;           {0, 0, 0, 0, 1},
&nbsp;           {1, 1, 0, 1, 1}}</span>
<span style="font-size:14px"><strong>Output:</strong></span>
<span style="font-size:14px">3</span>
<span style="font-size:14px"><strong>Explanation:
</strong>grid[][] = {{<span style="color:#ff0000">1</span>, <span style="color:#ff0000">1</span>, 0, <span style="color:#00ff00">1</span>, <span style="color:#00ff00">1</span>}, 
&nbsp;           {<span style="color:#ff0000">1</span>, 0, 0, 0, 0}, 
&nbsp;           {0, 0, 0, 0, <span style="color:#0000cd">1</span>}, 
&nbsp;           {<span style="color:#00ff00">1</span>, <span style="color:#00ff00">1</span>, 0, <span style="color:#0000ff">1</span>, <span style="color:#0000ff">1</span>}}</span>
<span style="font-size:14px">Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.</span>

</pre>

<p><span style="font-size:14px"><strong>Your Task:</strong></span></p>

<p><span style="font-size:14px">You don&#39;t need to read or print anything. Your task is to complete the function <strong>countDistinctIslands()&nbsp;</strong>which takes the <strong>grid</strong> as an input parameter and returns the total number of <strong>distinct</strong> islands.</span></p>

<p><span style="font-size:14px"><strong>Expected Time Complexity:&nbsp;</strong>O(n * m)<br />
<strong>Expected Space Complexity:&nbsp;</strong>O(n * m)</span></p>

<p><span style="font-size:14px"><strong>Constraints:</strong><br />
1 &le; n, m &le; 500<br />
grid[i][j] == 0 or grid[i][j] == 1</span></p>

<ul>
</ul>


---

## Solution

```cpp
// User function Template for C++

class Solution {
  public:
    int countDistinctIslands(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        
        auto dfs = [&] (auto self, int i, int j, vector<pair<int, int>>& shape, int baseRow, int baseCol) {
            if (min(i, j) < 0 || i >= n || j >= m || vis[i][j] || grid[i][j] == 0) {
                return;
            }
            vis[i][j] = true;
            
            shape.push_back({i - baseRow, j - baseCol});
            self(self, i + 1, j, shape, baseRow, baseCol);
            self(self, i - 1, j, shape, baseRow, baseCol);
            self(self, i, j + 1, shape, baseRow, baseCol);
            self(self, i, j - 1, shape, baseRow, baseCol);
        };
        
        vector<pair<int, int>> shape;
        set<vector<pair<int, int>>> distinctIslands;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (!vis[i][j] && grid[i][j] == 1) {
                    dfs(dfs, i, j, shape, i, j);
                    distinctIslands.insert(shape);
                    shape.clear();
                }
            }
        }
        return distinctIslands.size();
    }
};
```

---

## Notes

- This is basically an extension to number of islands.
- Along with the number of islands, we need to keep track of the shape of the islands, considering the starting coordinate as the base, store the difference of the other parts of the island with respect to the base in the same order of the dfs/bfs traversal.
- Store this shape in a set and return the set size at the end.
