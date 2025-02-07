[[802] - Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states)

---

- Medium
- [Submission](https://leetcode.com/problems/find-eventual-safe-states/submissions/1518982478/)
- [Submission](https://leetcode.com/problems/find-eventual-safe-states/submissions/1518993603/)
- depth-first-search, breadth-first-search, graph, topological-sort
- Contest: none

---

## Problem Statement

<p>There is a directed graph of <code>n</code> nodes with each node labeled from <code>0</code> to <code>n - 1</code>. The graph is represented by a <strong>0-indexed</strong> 2D integer array <code>graph</code> where <code>graph[i]</code> is an integer array of nodes adjacent to node <code>i</code>, meaning there is an edge from node <code>i</code> to each node in <code>graph[i]</code>.</p>

<p>A node is a <strong>terminal node</strong> if there are no outgoing edges. A node is a <strong>safe node</strong> if every possible path starting from that node leads to a <strong>terminal node</strong> (or another safe node).</p>

<p>Return <em>an array containing all the <strong>safe nodes</strong> of the graph</em>. The answer should be sorted in <strong>ascending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="Illustration of graph" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" style="height: 171px; width: 600px;" />
<pre>
<strong>Input:</strong> graph = [[1,2],[2,3],[5],[0],[5],[],[]]
<strong>Output:</strong> [2,4,5,6]
<strong>Explanation:</strong> The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
<strong>Output:</strong> [4]
<strong>Explanation:</strong>
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= graph[i].length &lt;= n</code></li>
	<li><code>0 &lt;= graph[i][j] &lt;= n - 1</code></li>
	<li><code>graph[i]</code> is sorted in a strictly increasing order.</li>
	<li>The graph may contain self-loops.</li>
	<li>The number of edges in the graph will be in the range <code>[1, 4 * 10<sup>4</sup>]</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> dp(n, -1), res;

        unordered_set<int> terminal, vis;
        for (int i = 0; i < n; ++i) {
            if (graph[i].empty()) {
                terminal.insert(i);
            }
        }

        auto dfs = [&] (auto self, int i) {
            if (terminal.find(i) != terminal.end()) {
                return dp[i] = 1;
            }
            if (vis.find(i) != vis.end()) {
                return dp[i] = 0;
            }
            if (dp[i] != -1) {
                return dp[i];
            }
            int flag = 1;
            vis.insert(i);
            for (int neigh: graph[i]) {
                flag &= self(self, neigh);
            }
            vis.erase(i);
            return dp[i] = flag;
        };

        for (int i = 0; i < n; ++i) {
            vis.clear();
            if (dfs(dfs, i)) {
                res.push_back(i);
            }
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> indegree(n);
        vector<vector<int>> adj(n);

        for (int i = 0; i < n; ++i) {
            for (int neigh: graph[i]) {
                adj[neigh].push_back(i);
                ++indegree[i];
            }
        }

        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        vector<bool> safe(n, false);
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            safe[node] = true;
            for (int neigh: adj[node]) {
                --indegree[neigh];
                if (indegree[neigh] == 0) {
                    q.push(neigh);
                }
            }
        }

        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (safe[i]) {
                res.push_back(i);
            }
        }
        return res;
    }
};
```

---

## Notes

- the easiest way to solve this is to use the basic topological sort, starting from indegree of 0 and eliminating the edges, this will also automatically prevent any cycles (which is what we need to avoid in this) and only handle the valid paths.

- can also use a dfs from every node and keep track of if any node in that path has been visited prior.
