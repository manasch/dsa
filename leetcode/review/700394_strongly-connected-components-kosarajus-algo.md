[[700394] - Strongly Connected Components (Kosaraju's Algo)](https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

---

- Medium
- DFS, Graph, Data Structures, Algorithms
- Amazon, Microsoft, Visa

---

## Problem Statement

<p><span style="font-size: 14px;">Given a Directed Graph with<strong> V </strong>vertices <strong>(</strong>Numbered from<strong> 0 to V-1)</strong>&nbsp;and <strong>E</strong> edges</span>, <span style="font-size: 14px;">Find </span><span style="font-size: 14px;">the number of strongly connected components in the graph.</span><br />&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 14px;"><strong>Input:</strong></span>
<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700394/Web/Other/89b7c4e7-e03c-402f-b445-3e8815299af6_1685086635.png" alt="" />
<span style="font-size: 14px;"><strong>Output:</strong>
3
<strong>Explanation</strong>:
</span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700394/Web/Other/9f4ccc7f-8ad8-4f81-908a-01f27090ba5e_1685086635.png" alt="" />
<span style="font-size: 14px;">We can clearly see that there are 3 Strongly
Connected Components in the Graph</span>
</pre>
<p><span style="font-size: 14px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 14px;"><strong>Input:</strong></span>
<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700394/Web/Other/8b9b3908-a800-4ffa-acaf-26cb760eac8e_1685086635.png" alt="" />
<span style="font-size: 14px;"><strong>Output:</strong>
1
<strong>Explanation</strong>:</span>
<span style="font-size: 14px;">All of the nodes are connected to each other.
So, there's only one SCC.</span>
</pre>
<p>&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Your Task:</strong><br />You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>kosaraju()</strong> which takes the number of vertices V and adjacency list of the graph of size V as inputs and returns an integer denoting the number of strongly connected components in the given graph.</span><br />&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Expected Time Complexity:</strong>&nbsp;O(V+E).<br /><strong>Expected Auxiliary Space:</strong>&nbsp;O(V+E).</span><br />&nbsp;</p>
<p><span style="font-size: 14px;"><strong>Constraints:</strong><br />1 </span> <span style="font-size: 14px;">&le;</span> <span style="font-size: 14px;"> V </span> <span style="font-size: 14px;">&le;</span> <span style="font-size: 14px;"> 5000<br />0 </span> <span style="font-size: 14px;">&le;</span> <span style="font-size: 14px;"> E </span> <span style="font-size: 14px;">&le;</span> <span style="font-size: 14px;"> (V*(V-1))<br />0 </span> <span style="font-size: 14px;">&le;</span> <span style="font-size: 14px;"> u, v </span> <span style="font-size: 14px;">&le;</span> <span style="font-size: 14px;"> V-1<br />Sum of E over all testcases will not exceed 25*10<sup>6</sup></span></p>

---

## Solution

```cpp
class Solution
{
	public:
	//Function to find number of strongly connected components in the graph.
    int kosaraju(int V, vector<vector<int>>& adj)
    {
        //code here
        stack<int> st;
        unordered_set<int> visited;
        auto dfs = [&] (auto self, int node) {
            if (visited.find(node) != visited.end()) {
                return;
            }
            visited.insert(node);
            for (auto i: adj[node]) {
                self(self, i);
            }
            st.push(node);
        };
        
        for (int i = 0; i < V; ++i) {
            if (visited.find(i) == visited.end()) {
                dfs(dfs, i);
            }
        }
        
        vector<vector<int>> adjT(V);
        for (int i = 0; i < V; ++i) {
            for (auto node: adj[i]) {
                adjT[node].push_back(i);
            }
        }
        
        auto dfs2 = [&] (auto self, int node) {
            if (visited.find(node) != visited.end()) {
                return;
            }
            visited.insert(node);
            for (auto i: adjT[node]) {
                self(self, i);
            }
        };
        
        int components = 0;
        visited.clear();
        while (!st.empty()) {
            if (visited.find(st.top()) == visited.end()) {
                ++components;
                dfs2(dfs2, st.top());
            }
            st.pop();
        }
        return components;
    }
};
```

---

## Notes

- This algo requires 3 steps.
	1. Perform a dfs and store the items that finish first in a stack, such that the items that finish last are at the top of the stack.
	2. Reverse the edges of the graph.
	3. Perform another dfs for the top of the stack until the stack becomes empty, every time a dfs can be performed, it is a new component.

- This algo works on the basis that one SCC can move to another SCC because of a bridge, and when the edges are reversed for this bridge, you can never go to another SCC from some SCC.
