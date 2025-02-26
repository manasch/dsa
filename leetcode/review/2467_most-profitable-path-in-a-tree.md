[[2467] - Most Profitable Path in a Tree](https://leetcode.com/problems/most-profitable-path-in-a-tree)

---

- Medium
- [Submission](https://leetcode.com/problems/most-profitable-path-in-a-tree/submissions/1555025323/)
- array, tree, depth-first-search, breadth-first-search, graph
- Contest: none

---

## Problem Statement

<p>There is an undirected tree with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>, rooted at node <code>0</code>. You are given a 2D integer array <code>edges</code> of length <code>n - 1</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.</p>

<p>At every node <code>i</code>, there is a gate. You are also given an array of even integers <code>amount</code>, where <code>amount[i]</code> represents:</p>

<ul>
	<li>the price needed to open the gate at node <code>i</code>, if <code>amount[i]</code> is negative, or,</li>
	<li>the cash reward obtained on opening the gate at node <code>i</code>, otherwise.</li>
</ul>

<p>The game goes on as follows:</p>

<ul>
	<li>Initially, Alice is at node <code>0</code> and Bob is at node <code>bob</code>.</li>
	<li>At every second, Alice and Bob <b>each</b> move to an adjacent node. Alice moves towards some <strong>leaf node</strong>, while Bob moves towards node <code>0</code>.</li>
	<li>For <strong>every</strong> node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
	<ul>
		<li>If the gate is <strong>already open</strong>, no price will be required, nor will there be any cash reward.</li>
		<li>If Alice and Bob reach the node <strong>simultaneously</strong>, they share the price/reward for opening the gate there. In other words, if the price to open the gate is <code>c</code>, then both Alice and Bob pay&nbsp;<code>c / 2</code> each. Similarly, if the reward at the gate is <code>c</code>, both of them receive <code>c / 2</code> each.</li>
	</ul>
	</li>
	<li>If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node <code>0</code>, he stops moving. Note that these events are <strong>independent</strong> of each other.</li>
</ul>

<p>Return<em> the <strong>maximum</strong> net income Alice can have if she travels towards the optimal leaf node.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/29/eg1.png" style="width: 275px; height: 275px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
  Alice&#39;s net income is now -2.
- Both Alice and Bob move to node 1. 
&nbsp; Since they reach here simultaneously, they open the gate together and share the reward.
&nbsp; Alice&#39;s net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice&#39;s income remains unchanged.
&nbsp; Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/29/eg2.png" style="width: 250px; height: 78px;" />
<pre>
<strong>Input:</strong> edges = [[0,1]], bob = 1, amount = [-7280,2350]
<strong>Output:</strong> -7280
<strong>Explanation:</strong> 
Alice follows the path 0-&gt;1 whereas Bob follows the path 1-&gt;0.
Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>edges</code> represents a valid tree.</li>
	<li><code>1 &lt;= bob &lt; n</code></li>
	<li><code>amount.length == n</code></li>
	<li><code>amount[i]</code> is an <strong>even</strong> integer in the range <code>[-10<sup>4</sup>, 10<sup>4</sup>]</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<int> bobVisitTime(n, -1);
        unordered_map<int, vector<int>> adj;

        for (auto &edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        auto dfs = [&] (auto self, int node, int time, int par) -> bool {
            if (node == 0) {
                bobVisitTime[node] = time;
                return true;
            }
            for (const int& neigh: adj[node]) {
                if (neigh != par) {
                    if (self(self, neigh, time + 1, node)) {
                        bobVisitTime[node] = time;
                        return true;
                    }
                }
            }
            return false;
        };

        dfs(dfs, bob, 0, -1);

        queue<pair<int, int>> q;
        vector<bool> vis(n, false);
        q.push(make_pair(0, 0));
        int level = 0;
        int res = INT_MIN;

        while (!q.empty()) {
            int p = q.size();
            while (p--) {
                auto [node, tot] = q.front();
                q.pop();

                if (vis[node]) {
                    continue;
                }
                vis[node] = true;

                int alicePart = amount[node];
                if (bobVisitTime[node] != -1) {
                    if (level > bobVisitTime[node]) {
                        alicePart = 0;
                    }
                    if (level == bobVisitTime[node]) {
                        alicePart = (amount[node] >> 1);
                    }
                }
                for (const int& neigh: adj[node]) {
                    if (!vis[neigh]) {
                        q.push(make_pair(neigh, tot + alicePart));
                    }

                    if (node != 0 && adj[node].size() == 1) {
                        res = max(res, tot + alicePart);
                    }
                }
            }
            ++level;
        }

        return res;
    }
};
```

---

## Notes

- intuition was right but could not get it to code.
- there is only one path that Bob can take since it's a tree, hence no cycles.
- can keep track of when bob visits the nodes of his path, using dfs or bfs.

- now alice has to choose which path to leaf node will give the highest profit.
- since we kept track of bob's times for each node, when alice reaches a node in the tree, can determine how much profit or expense is needed depending on whether bob has already gone past this node, on the node at the same time, or has not visited the node yet or at all. can be done using bfs and level order.
