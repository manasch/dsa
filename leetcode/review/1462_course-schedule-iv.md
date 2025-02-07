[[1462] - Course Schedule IV](https://leetcode.com/problems/course-schedule-iv)

---

- Medium
- [Submission](https://leetcode.com/problems/course-schedule-iv/submissions/1522035714/)
- [Submission](https://leetcode.com/problems/course-schedule-iv/submissions/1522045566/)
- depth-first-search, breadth-first-search, graph, topological-sort
- Contest: none

---

## Problem Statement

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>a<sub>i</sub></code> first if you want to take course <code>b<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code> indicates that you have to take course <code>0</code> before you can take course <code>1</code>.</li>
</ul>

<p>Prerequisites can also be <strong>indirect</strong>. If course <code>a</code> is a prerequisite of course <code>b</code>, and course <code>b</code> is a prerequisite of course <code>c</code>, then course <code>a</code> is a prerequisite of course <code>c</code>.</p>

<p>You are also given an array <code>queries</code> where <code>queries[j] = [u<sub>j</sub>, v<sub>j</sub>]</code>. For the <code>j<sup>th</sup></code> query, you should answer whether course <code>u<sub>j</sub></code> is a prerequisite of course <code>v<sub>j</sub></code> or not.</p>

<p>Return <i>a boolean array </i><code>answer</code><i>, where </i><code>answer[j]</code><i> is the answer to the </i><code>j<sup>th</sup></code><i> query.</i></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg" style="width: 222px; height: 62px;" />
<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
<strong>Output:</strong> [false,true]
<strong>Explanation:</strong> The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
<strong>Output:</strong> [false,false]
<strong>Explanation:</strong> There are no prerequisites, and each course is independent.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>Input:</strong> numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
<strong>Output:</strong> [true,true]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= numCourses &lt;= 100</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= (numCourses * (numCourses - 1) / 2)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= numCourses - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are <strong>unique</strong>.</li>
	<li>The prerequisites graph has no cycles.</li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= numCourses - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<int>> adj(numCourses, vector<int>());
        for (auto &pre: prerequisites) {
            adj[pre[1]].push_back(pre[0]);
        }

        unordered_map<int, unordered_set<int>> indirect;

        auto dfs = [&] (auto self, int c) -> unordered_set<int> {
            if (indirect.find(c) == indirect.end()) {
                indirect[c] = unordered_set<int>();
                for (int &prereq: adj[c]) {
                    unordered_set<int> temp = self(self, prereq);
                    indirect[c].insert(temp.begin(), temp.end());
                }
                indirect[c].insert(c);
            }
            return indirect[c];
        };

        for (int i = 0; i < numCourses; ++i) {
            dfs(dfs, i);
        }

        vector<bool> res;
        for (auto &q: queries) {
            res.push_back(indirect[q[1]].find(q[0]) != indirect[q[1]].end());
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<bool>> isPre(numCourses, vector<bool>(numCourses, false));
        for (auto pre: prerequisites) {
            isPre[pre[0]][pre[1]] = true;
        }

        for (int i = 0; i < numCourses; ++i) {
            for (int j = 0; j < numCourses; ++j) {
                for (int k = 0; k < numCourses; ++k) {
                    isPre[j][k] = isPre[j][k] || (isPre[j][i] & isPre[i][k]);
                }
            }
        }

        vector<bool> res;
        for (auto q: queries) {
            res.push_back(isPre[q[0]][q[1]]);
        }
        return res;
    }
};
```

---

## Notes

- first method involves performing dfs and keeping track of the paths that have been visited from any particular node.
- on the way, if that is the case, instead of going that path again, just append those nodes, to the visit set of the current dfs start node, and move ahead.
- for each query, check if the node exists in the visit set.

- can also make a small tweak to the floyd-warshall's algorithm, which is much simpler. (via, to, from -> k, i, j -> order in the cubic solution for loops).
