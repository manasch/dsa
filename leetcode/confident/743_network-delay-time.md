[[743] - Network Delay Time](https://leetcode.com/problems/network-delay-time)

---

- Medium
- [Submission](https://leetcode.com/problems/network-delay-time/submissions/1027518081/)
- depth-first-search, breadth-first-search, graph, heap-priority-queue, shortest-path

---

## Problem Statement

<p>You are given a network of <code>n</code> nodes, labeled from <code>1</code> to <code>n</code>. You are also given <code>times</code>, a list of travel times as directed edges <code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>, where <code>u<sub>i</sub></code> is the source node, <code>v<sub>i</sub></code> is the target node, and <code>w<sub>i</sub></code> is the time it takes for a signal to travel from source to target.</p>

<p>We will send a signal from a given node <code>k</code>. Return <em>the <strong>minimum</strong> time it takes for all the</em> <code>n</code> <em>nodes to receive the signal</em>. If it is impossible for all the <code>n</code> nodes to receive the signal, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="width: 217px; height: 239px;" />
<pre>
<strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= times.length &lt;= 6000</code></li>
	<li><code>times[i].length == 3</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 100</code></li>
	<li>All the pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are <strong>unique</strong>. (i.e., no multiple edges.)</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<int>> adj(n + 1, vector<int>(n + 1, -1));
        for (auto edge: times) {
            adj[edge[0]][edge[1]] = edge[2];
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        unordered_set<int> visited;

        // for (int i = 1; i <= n; ++i) {
        //     for (int j = 1; j <= n; ++j) {
        //         cout << adj[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        int res = 0;
        pq.push({0, k});
        pair<int, int> p;
        while (!pq.empty()) {
            p = pq.top();
            pq.pop();
            if (visited.find(p.second) == visited.end()) {
                res = max(res, p.first);
                visited.insert(p.second);
                for (int k = 1; k <= n; ++k) {
                    if (adj[p.second][k] != -1 && visited.find(k) == visited.end()) {
                        pq.push({p.first + adj[p.second][k], k});
                    }
                }
            }
        }
        if (visited.size() != n) {
            return -1;
        }
        return res;
    }
};
```

---

## Notes

- This would be a simple BFS while updating the max time it takes to reach any particular node.
