[[207] - Course Schedule](https://leetcode.com/problems/course-schedule)

---

- Medium
- [Submission](https://leetcode.com/problems/course-schedule/submissions/1002500782/)
- depth-first-search, breadth-first-search, graph, topological-sort

---

## Problem Statement

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li>All the pairs prerequisites[i] are <strong>unique</strong>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, unordered_set<int>> courseMap;
        for (auto x: prerequisites) {
            courseMap[x[0]].insert(x[1]);
        }

        unordered_set<int> visited;
        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(courseMap, visited, i)) {
                return false;
            }
        }
        return true;
    }
private:
    bool dfs(unordered_map<int, unordered_set<int>>& courseMap, unordered_set<int>& visited, int course) {
        if (courseMap[course].empty()) {
            return true;
        }
        // If there exists a cycle, it is impossible to finish all the courses.
        if (visited.find(course) != visited.end()) { 
            return false;
        }
        visited.insert(course);
        bool res = true;
        for (auto x: courseMap[course]) {
            if (!dfs(courseMap, visited, x)) {
                return false;
            }
        }
        courseMap[course].clear();
        visited.erase(course);
        return true;
    }
};
```

### Kahn's Algorithm
```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses);
        vector<vector<int>> adj(numCourses);
        for (auto prerequisite : prerequisites) {
            adj[prerequisite[1]].push_back(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }

        queue<int> q;
        // Push all the nodes with indegree zero in the queue.
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        int nodesVisited = 0;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            nodesVisited++;

            for (auto& neighbor : adj[node]) {
                // Delete the edge "node -> neighbor".
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        return nodesVisited == numCourses;
    }
};
```

---

## Notes

- Kahn's algorithm could be used to decide if all the course can be completed or not, this involves creating a graph (represented as an adjacency matrix / list) and deleting all nodes that have an indegree of 0. This means that no other course is required to take the current course.
- This method implemented is the opposite, create edges from the course that is depended on the other course. Perform a `DFS` until a course with no outdegree exists, this indicates that the course can be completed and is not dependent on any other course, when it comes back from the call without fail, the list holding can be cleared.
