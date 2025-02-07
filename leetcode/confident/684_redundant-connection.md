[[684] - Redundant Connection](https://leetcode.com/problems/redundant-connection)

---

- Medium
- [Submission](https://leetcode.com/problems/redundant-connection/submissions/1524218301/)
- depth-first-search, breadth-first-search, union-find, graph
- Contest: none

---

## Problem Statement

<p>In this problem, a tree is an <strong>undirected graph</strong> that is connected and has no cycles.</p>

<p>You are given a graph that started as a tree with <code>n</code> nodes labeled from <code>1</code> to <code>n</code>, with one additional edge added. The added edge has two <strong>different</strong> vertices chosen from <code>1</code> to <code>n</code>, and was not an edge that already existed. The graph is represented as an array <code>edges</code> of length <code>n</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the graph.</p>

<p>Return <em>an edge that can be removed so that the resulting graph is a tree of </em><code>n</code><em> nodes</em>. If there are multiple answers, return the answer that occurs last in the input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> [2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
<strong>Output:</strong> [1,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub> &lt; b<sub>i</sub> &lt;= edges.length</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
	<li>The given graph is connected.</li>
</ul>


---

## Solution

```cpp
class UnionFind {
public:
    int n;
    vector<int> parent;
    vector<int> rank;

    UnionFind(int n) : n(n), parent(vector<int>(n + 1)), rank(vector<int>(n + 1, 1)) {
        iota(parent.begin(), parent.end(), 0);
    }

    bool _union(int a, int b) {
        int ap = _parent(a);
        int bp = _parent(b);

        if (ap == bp) {
            return false;
        }
        if (rank[ap] >= rank[bp]) {
            parent[bp] = ap;
            ++rank[ap];
        }
        else {
            parent[ap] = bp;
        }
        return true;
    }

    int _parent(int a) {
        if (parent[a] == a) {
            return a;
        }
        return parent[a] = _parent(parent[a]);
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        UnionFind uf(n);

        for (auto edge: edges) {
            if (!uf._union(edge[0], edge[1])) {
                return {edge[0], edge[1]};
            }
        }
        return {};
    }
};
```

---

## Notes

- basic union find, return the edge when you detect that it is part of a cycle, that will naturally be the last node in the list.

- other method could involve finding the edges that form the cycle from dfs / bfs, and finding the the last edge that occurs in the list.
