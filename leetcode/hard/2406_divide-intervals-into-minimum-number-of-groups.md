[[2406] - Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups)

---

- Medium
- [Submission](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/submissions/1419988046/)
- array, two-pointers, greedy, sorting, heap-priority-queue, prefix-sum
- Contest: none

---

## Problem Statement

<p>You are given a 2D integer array <code>intervals</code> where <code>intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> represents the <strong>inclusive</strong> interval <code>[left<sub>i</sub>, right<sub>i</sub>]</code>.</p>

<p>You have to divide the intervals into one or more <strong>groups</strong> such that each interval is in <strong>exactly</strong> one group, and no two intervals that are in the same group <strong>intersect</strong> each other.</p>

<p>Return <em>the <strong>minimum</strong> number of groups you need to make</em>.</p>

<p>Two intervals <strong>intersect</strong> if there is at least one common number between them. For example, the intervals <code>[1, 5]</code> and <code>[5, 8]</code> intersect.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[5,6],[8,10],[11,13]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> None of the intervals overlap, so we can put all of them in one group.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<pair<int, int>> vec;
        for (auto i: intervals) {
            vec.push_back({i[0], 1});
            vec.push_back({i[1] + 1, -1});
        }
        sort(vec.begin(), vec.end());

        int res = 0;
        int count = 0;
        for (int i = 0; i < vec.size(); ++i) {
            count += vec[i].second;
            res = max(res, count);
        }
        return res;
    }
};
```

---

## Notes

- This problem is very similar to Meeting Rooms II, where I need to find the minimum number of groups required.
- I still couldn't solve it even though I've done the other problem before, but this solution is very nice.

- Just have to create two events for each interval, `{start, 1}` and `{end + 1, -1}`.
- This works because, you are trying to keep track of the number of times there is an overlap at each time.
- Performing a prefix sum and taking the max of all of this gives the required result as the maximum number of groups required or rooms occupied at any point in time.
