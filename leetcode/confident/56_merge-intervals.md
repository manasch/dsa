[[56] - Merge Intervals](https://leetcode.com/problems/merge-intervals)

---

- Medium
- [Submission](https://leetcode.com/problems/merge-intervals/submissions/1015380122/)
- array, sorting

---

## Problem Statement

<p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ans;

        vector<int> interval = intervals[0];
        for (int i = 1; i < n; ++i) {
            if (interval[0] <= intervals[i][1] && interval[1] >= intervals[i][0]) {
                interval[0] = min(interval[0], intervals[i][0]);
                interval[1] = max(interval[1], intervals[i][1]);
            }
            else {
                ans.push_back(interval);
                interval = intervals[i];
            }
        }
        ans.push_back(interval);

        return ans;
    }
};
```

---

## Notes

- Perform an initial sort, having a running interval, pick the 0th one and compare it with the next, if they overlap, merge them.
- If they don't overlap, then insert the merged interval to a new array, and replace the running interval with the new non-overlapping one.
