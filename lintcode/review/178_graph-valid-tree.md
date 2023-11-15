[[178] - Graph Valid Tree](https://www.lintcode.com/problem/178)

---

- Medium
- union-find, breadth-first-searchbfs
- [no companies listed]

---

## Problem Statement

### Description

Given `n` nodes labeled from `0` to `n - 1` and a list of `undirected` edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

> You can assume that no duplicate edges will appear in edges. Since all edges are `undirected`, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.

### Example

**Example 1:**

```
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
```

**Example 2:**

```
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
```

---

## Solution

```cpp
class Solution {
public:
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    bool validTree(int n, vector<vector<int>> &edges) {
        // write your code here
        unordered_set<int> visited;
        vector<vector<int>> adjMatrix(n, vector<int>());

        for (auto& edge: edges) {
            adjMatrix[edge[0]].push_back(edge[1]);
            adjMatrix[edge[1]].push_back(edge[0]);
        }

        if (!dfs(adjMatrix, visited, 0, -1)) {
            return false;
        }
        return (visited.size() == n);
    }
private:
    bool dfs(vector<vector<int>>& adjMatrix, unordered_set<int>& visited, int vertex, int prev) {
        if (visited.find(vertex) != visited.end()) {
            return false;
        }

        visited.insert(vertex);
        for (int v: adjMatrix[vertex]) {
            if (v != prev) {
                if (!dfs(adjMatrix, visited, v, vertex)) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

---

## Notes

- DFS could be done from the start and at each dfs call send the current node to the next call as the previous node so that it can compare it and realize that the caller was it's parent and not something that it has already visited.
- In the end if the number of visited nodes is equal to the total number of nodes, return true.
