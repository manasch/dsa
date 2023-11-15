[[919] - Meeting Rooms II](https://www.lintcode.com/problem/919)

---

- Medium
- heap, greedy, sweep-line, sort
- facebook, google, uber

---

## Problem Statement

### Description

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find the minimum number of conference rooms required.)

> (0,8),(8,10) is not conflict at 8

### Example

**Example1**

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
```

**Example2**

```
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
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
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        int n = intervals.size();
        if (n == 1) {
            return 1;
        }
        vector<int> start, end;
        for (Interval i: intervals) {
            start.push_back(i.start);
            end.push_back(i.end);
        }

        sort(start.begin(), start.end());
        sort(end.begin(), end.end());
        int res = 0, count = 0;

        int s = 0, e = 0;

        while (s < n && e < n) {
            if (start[s] < end[e]) {
                ++s;
                ++count;
            }
            else {
                ++e;
                --count;
            }
            res = max(res, count);
        }
        return res;
    }
};
```

---

## Notes

- Initially planned on keeping the ends of all the meeting room end points in a set, but that won't work when multiple meetings end at the same time.
- Create two different arrays, one for start and one for end.
- Have two different pointers traversing them separately, if the start time for the start pointer is less than the end time for the end pointer, that means, the earliest meeting that's starting collides with the earliest end of the meetings, hence, increament the count value.
- Next time, if the end value is smaller or equal, that means that this meeting is completed and the number of rooms currently in use decreases by 1.
- At every stage, keep track of the max number of rooms at use, which should give the answer.
