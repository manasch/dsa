[[700410] - Bipartite Graph](https://practice.geeksforgeeks.org/problems/bipartite-graph/1)

---

- Medium
- DFS, Graph, BFS, Data Structures, Algorithms
- Flipkart, Microsoft, Samsung

---

## Problem Statement

<p><span style="font-size: 14px;">Given an adjacency list&nbsp;of a graph<strong> adj&nbsp; </strong>of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.</span><br />&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 14px;"><strong>Input: 
</strong><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700410/Web/Other/cdb283af-c52d-46df-8646-5017b45b5a13_1685086658.png" alt="" />
<strong>Output: </strong>1
<strong>Explanation: </strong>The given graph can be colored 
in two colors so, it is a bipartite graph.
</span></pre>
<p><span style="font-size: 14px;"><strong>Example&nbsp;2:</strong></span></p>
<pre><span style="font-size: 14px;"><strong>Input:
</strong><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700410/Web/Other/471d9abf-5d47-48ea-aa35-2dace9f5a2da_1685086659.png" alt="" />
<strong>Output: </strong>0
<strong>Explanation: </strong>The given graph cannot be colored 
in two colors such that color of adjacent 
vertices differs. 
</span></pre>
<p>&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Your Task:</strong><br />You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>isBipartite()&nbsp;</strong>which takes V denoting no. of vertices and adj denoting adjacency list of the graph and returns a boolean value true if the graph is bipartite otherwise returns false.</span><br />&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Expected Time Complexity:&nbsp;</strong>O(V + E)<br /><strong>Expected Space Complexity:&nbsp;</strong>O(V)<br /><br /><strong>Constraints:</strong><br />1 &le; V, E &le; 10<sup>5</sup></span></p>

---

## Solution

```cpp
class Solution {
public:
	bool isBipartite(int V, vector<int>adj[]){
	    queue<int> q;
	    vector<int> colors(V, -1);
	    unordered_set<int> vis;
	    
	    auto bfs = [&] (int src) {
    	    q.push(src);
    	    colors[src] = 1;
    	    while (!q.empty()) {
    	        int size = q.size();
    	        while (size--) {
    	            int node = q.front();
    	            q.pop();
    	            if (vis.count(node)) {
    	                continue;
    	            }
    	            vis.insert(node);
    	            for (int neigh: adj[node]) {
    	                if (colors[node] == colors[neigh]) {
    	                    return false;
    	                }
    	                else if (colors[neigh] == -1) {
    	                    colors[neigh] = colors[node] == 1 ? 0 : 1;
    	                }
    	                q.push(neigh);
    	            }
    	        }
    	    }
    	    return true;
	    };
	    
	    bool res;
	    for (int i = 0; i < V; ++i) {
	        if (!vis.count(i)) {
	            res = bfs(i);
	            if (!res) {
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

- The graph can be *disconnected*.
- Perform a bfs from each unvisited node. Have a vector that keeps track of the colors of the nodes.
- Start out the bfs with the colors of the source being 1. For each of its neighbours, mark the color the opposite of the current node's color it if it is not colored.
- If it is colored, check if they are of the same colors, if so, return false.
