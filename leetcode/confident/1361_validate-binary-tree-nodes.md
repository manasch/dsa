[[1361] - Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes)

---

- Medium
- [Submission](https://leetcode.com/problems/validate-binary-tree-nodes/submissions/1077223670)
- [Submission](https://leetcode.com/problems/validate-binary-tree-nodes/submissions/1077232876)
- tree, depth-first-search, breadth-first-search, union-find, graph, binary-tree

---

## Problem Statement

<p>You have <code>n</code> binary tree nodes numbered from <code>0</code> to <code>n - 1</code> where node <code>i</code> has two children <code>leftChild[i]</code> and <code>rightChild[i]</code>, return <code>true</code> if and only if <strong>all</strong> the given nodes form <strong>exactly one</strong> valid binary tree.</p>

<p>If node <code>i</code> has no left child then <code>leftChild[i]</code> will equal <code>-1</code>, similarly for the right child.</p>

<p>Note that the nodes have no values and that we only use the node numbers in this problem.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex1.png" style="width: 195px; height: 287px;" />
<pre>
<strong>Input:</strong> n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex2.png" style="width: 183px; height: 272px;" />
<pre>
<strong>Input:</strong> n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex3.png" style="width: 82px; height: 174px;" />
<pre>
<strong>Input:</strong> n = 2, leftChild = [1,0], rightChild = [-1,-1]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == leftChild.length == rightChild.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>-1 &lt;= leftChild[i], rightChild[i] &lt;= n - 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        set<int> nodes;
        for (int i = 0; i < n; ++i) {
            nodes.insert(i);
        }

        // Can remove a node if it is being added as it has a parent.
        // If a node is being removed again, then it is being added again, hence can return false instantly.
        unordered_map<int, vector<int>> adj;
        for (int i = 0; i < n; ++i) {
            if (leftChild[i] != -1) {
                adj[i].push_back(leftChild[i]);
                if (nodes.find(leftChild[i]) != nodes.end()) {
                    nodes.erase(leftChild[i]);
                }
                else {
                    return false;
                }
            }
            if (rightChild[i] != -1) {
                adj[i].push_back(rightChild[i]);
                if (nodes.find(rightChild[i]) != nodes.end()) {
                    nodes.erase(rightChild[i]);
                }
                else {
                    return false;
                }
            }
        }

        if (nodes.size() != 1) {
            return false;
        }
        int root = *nodes.begin();
        nodes.clear();
        queue<int> q;
        q.push(root);
        
        auto bfs = [&] (int i) {
            while (!q.empty()) {
                int n = q.front();
                q.pop();
                if (nodes.find(n) != nodes.end()) {
                    return false;
                }
                nodes.insert(n);
                for (int x: adj[n]) {
                    q.push(x);
                }
            }
            return nodes.size() == n;
        };

        return bfs(root);
    }
};
```

```cpp
class UnionFind {
private:
    vector<int> parents;
    int n;
    int components;
public:
    UnionFind(int n) {
        this->n = n;
        parents.resize(n, 0);
        iota(parents.begin(), parents.end(), 0);
        components = n;
    }

    bool join(int u, int v) {
        int up = find(u);
        int vp = find(v);

        if (vp != v || up == vp) {
            return false;
        }

        --components;
        parents[vp] = up;
        return true;
    }

    int find(int node) {
        if (parents[node] == node) {
            return node;
        }
        return parents[node] = find(parents[node]);
    }

    int getComponents() {
        return components;
    }
};

class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        UnionFind uf(n);
        for (int i = 0; i < n; ++i) {
            int children[] = {leftChild[i], rightChild[i]};
            for (int c: children) {
                if (c == -1) {
                    continue;
                }
                if (!uf.join(i, c)) {
                    return false;
                }
            }
        }

        return uf.getComponents() == 1;
    }
};
```

---

## Notes

- First approach is just a regular bfs, create an adjacency list and find the node with no parents (this will be the root).
- Perform bfs and check if all nodes have been visited.
- While creating adjacency list, if nodes are being added again then return false instantly.

- Second approach is normal union-find.
- If the number of components is not 1, then return false.
- If while joining, the child node is not a component of its own or if both have same parents (forms a cycle), then return false.

- Took help for union find, but bfs solution on my own.
