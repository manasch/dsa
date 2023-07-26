[[684] - Redundant Connection](https://leetcode.com/problems/redundant-connection)

---

- Medium
- [Submission](https://leetcode.com/problems/redundant-connection/submissions/1003450061/)
- depth-first-search, breadth-first-search, union-find, graph

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
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parents(n + 1);
        vector<int> rank(n + 1, 1);
        iota(parents.begin(), parents.end(), 0);

        vector<int> result;
        for (auto edge: edges) {
            if (!_union(edge[0], edge[1], rank, parents)) {
                result = edge;
                break;
            }
        }
        return result;
    }
private:
    int _find(int n, vector<int>& parents) {
        int p = parents[n];

        while (p != parents[p]) {
            p = parents[p];
        }
        return p;
    }

    bool _union(int u, int v, vector<int>& rank, vector<int>& parents) {
        int p1 = _find(u, parents);
        int p2 = _find(v, parents);

        if (p1 == p2) {
            return false;
        }
        if (rank[p1] >= rank[p2]) {
            parents[p2] = p1;
            rank[p1] += rank[p2];
        }
        else {
            parents[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;
    }
};
```

---

## Notes

- Trying out union-find algorithm for the first time.
- We try to union two nodes, it is only possible to make a union when they have difference parents, if they have the same parents that means it has already been unioned before and will now form a cycle. The first edge to form a cycle will be the additional edge.
- The find method just finds the parent of the given node. The one with a lower rank gets merged into the one with the higher rank.
