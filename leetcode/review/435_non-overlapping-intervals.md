[[435] - Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals)

---

- Medium
- [Submission](https://leetcode.com/problems/non-overlapping-intervals/submissions/1015528439/)
- [Submission](https://leetcode.com/problems/non-overlapping-intervals/submissions/1015542123/)
- array, dynamic-programming, greedy, sorting

---

## Problem Statement

<p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 1) {
            return 0;
        }
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        vector<bool> dp(n, false);

        int count = 0;
        for (int i = n - 2; i >= 0; --i) {
            for (int j = i + 1; j < n; ++j) {
                if (dp[j] == false && (intervals[i][0] < intervals[j][1] && intervals[i][1] > intervals[j][0])) {
                    dp[i] = true;
                    ++count;
                    break;
                }
            }
        }
        return count;
    }
};
```

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if (n == 1) {
            return 0;
        }

        sort(intervals.begin(), intervals.end());
        int count = 0;
        int end = intervals[0][1];

        for (int i = 1; i < n; ++i) {
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
            }
            else {
                ++count;
                end = min(end, intervals[i][1]);
            }
        }
        return count;
    }
};
```

---

## Notes

- Honestly don't know how this worked, I thought I'll sort and then keep track of what all I've removed so that I don't visit it again, Iterate backwards and remove the ones that overlap and break.
- Next time I iterate, I see this has been removed and ignore it, and it worked.

- The linear solution involves keeping track of the end as you traverse the vector, check for an overlap, if they do, then update the count and update the end with the minimum of itself and the one it traversed through.
