[[920] - Meeting Rooms](https://www.lintcode.com/problem/920)

---

- Easy
- sort
- facebook, uber

---

## Problem Statement

### Description

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine if a person could attend all meetings.

> (0,8),(8,10) is not conflict at 8

### Example

**Example1**

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
```

**Example2**

```
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
```

---

## Solution

```cpp
/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    bool canAttendMeetings(vector<Interval> &intervals) {
        // Write your code here
        int n = intervals.size();
        if (n == 1 || n == 0) {
            return true;
        }
        sort(intervals.begin(), intervals.end(), [](const Interval& i1, const Interval& i2) {
            return i1.start < i2.start;
        });

        Interval interval = intervals[0];
        for (int i = 1; i < n; ++i) {
            if (intervals[i].start < interval.end && intervals[i].end > interval.start) {
                return false;
            }
            else {
                interval = intervals[i];
            }
        }
        return true;
    }
};
```

---

## Notes

- Sort the given array based on the start index, keep a travelling interval, if it overlaps with any, instantly return false.
- If it doesn't overlap with the next one, update the interval to this and continue.
