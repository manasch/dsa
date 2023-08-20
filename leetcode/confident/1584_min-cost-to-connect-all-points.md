[[1584] - Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points)

---

- Medium
- [Submission](https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/1026661189/)
- array, union-find, graph, minimum-spanning-tree

---

## Problem Statement

<p>You are given an array <code>points</code> representing integer coordinates of some points on a 2D-plane, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.</p>

<p>The cost of connecting two points <code>[x<sub>i</sub>, y<sub>i</sub>]</code> and <code>[x<sub>j</sub>, y<sub>j</sub>]</code> is the <strong>manhattan distance</strong> between them: <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>, where <code>|val|</code> denotes the absolute value of <code>val</code>.</p>

<p>Return <em>the minimum cost to make all points connected.</em> All points are connected if there is <strong>exactly one</strong> simple path between any two points.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="width: 214px; height: 268px;" />
<pre>
<strong>Input:</strong> points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>Output:</strong> 20
<strong>Explanation:</strong> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="width: 214px; height: 268px;" />
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[3,12],[-2,5],[-4,1]]
<strong>Output:</strong> 18
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>All pairs <code>(x<sub>i</sub>, y<sub>i</sub>)</code> are distinct.</li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    int manhattan_distance(vector<int>& p1, vector<int>& p2) {
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]);
    }

    int mst(vector<vector<int>>& adj, int n) {
        int res = 0;
        int connections = n - 1;
        unordered_set<int> visited;
        priority_queue<pair<int, int>> pq;
        visited.insert(0);

        for (int i = 1; i < n; ++i) {
            pq.push({-1 * adj[0][i], i});
        }

        pair<int, int> p;
        int idx, dist;
        while (connections--) {
            while (visited.find(pq.top().second) != visited.end()) {
                pq.pop();
            }
            p = pq.top();
            dist = -1 * p.first;
            idx = p.second;
            cout << idx << " " << dist << endl;
            visited.insert(idx);
            for (int j = 0; j < n; ++j) {
                if (idx != j && visited.find(j) == visited.end()) {
                    pq.push({-1 * adj[idx][j], j});
                }
            }
            res += dist;
        }
        return res;
    }
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<int>> adj(n, vector<int>(n, -1));

        int dist;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                dist = manhattan_distance(points[i], points[j]);
                adj[i][j] = adj[j][i] = dist;
            }
        }

        int res = mst(adj, n);
        return res;
    }
};
```

---

## Notes

- This is basically finding the MST from a fully connected graph.
- The issue I had was that the min-heap should be popped till it sees that a node has not been visited. Rest all works out fine with regular Prim's algo as that was implemented here.
