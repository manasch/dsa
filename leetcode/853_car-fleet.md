[[853] - Car Fleet](https://leetcode.com/problems/car-fleet)

---

- Medium
- [Submission](https://leetcode.com/problems/car-fleet/submissions/887263792/)
- array, stack, sorting, monotonic-stack

---

## Problem Statement

<p>There are <code>n</code> cars going to the same destination along a one-lane road. The destination is <code>target</code> miles away.</p>

<p>You are given two integer array <code>position</code> and <code>speed</code>, both of length <code>n</code>, where <code>position[i]</code> is the position of the <code>i<sup>th</sup></code> car and <code>speed[i]</code> is the speed of the <code>i<sup>th</sup></code> car (in miles per hour).</p>

<p>A car can never pass another car ahead of it, but it can catch up to it&nbsp;and drive bumper to bumper <strong>at the same speed</strong>. The faster car will <strong>slow down</strong> to match the slower car&#39;s speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).</p>

<p>A <strong>car fleet</strong> is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.</p>

<p>If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.</p>

<p>Return <em>the <strong>number of car fleets</strong> that will arrive at the destination</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 10, position = [3], speed = [3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is only one car, hence there is only one fleet.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = 100, position = [0,2,4], speed = [4,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == position.length == speed.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt; target &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= position[i] &lt; target</code></li>
	<li>All the values of <code>position</code> are <strong>unique</strong>.</li>
	<li><code>0 &lt; speed[i] &lt;= 10<sup>6</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        int res = 0;
        map<int, int> pq;
        stack<float> st;
        float t;

        for (int i = 0; i < n; ++i) {
            pq.insert(pair<int, int>(position[i], speed[i]));
        }

        for (auto it = pq.rbegin(); it != pq.rend(); ++it) {
            t = (float) (target - it->first) / (float) it->second;
            if (st.empty()) {
                st.push(t);
            }
            else {
                if (t > st.top()) {
                    ++res;
                    st.push(t);
                }
            }
        }

        return ++res;
    }
};
```

---

## Notes

- Uses two concepts, sorting it by distance and finding out time for each car.
- Traverse backwards, if an earlier car has a greater speed, then it would be slowed down by the car ahead of it, hence keep a stack of the speed of cars while traversing backwards inserting only when the speed is slower. `O(n)` space and `O(nlogn)` time.
