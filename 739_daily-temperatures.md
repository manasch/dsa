[[739] - Daily Temperatures](https://leetcode.com/problems/daily-temperatures)

---

- Medium
- [Submission](https://leetcode.com/problems/daily-temperatures/submissions/883047943/)
- array, stack, monotonic-stack

---

## Problem Statement

<p>Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        int current;
        vector<int> answer(n, 0);
        stack<pair<int, int>> st;

        for (int i = 0; i < n; ++i) {
            current = temperatures[i];
            while (!st.empty() && current > st.top().second) {
                answer[st.top().first] = i - st.top().first;
                st.pop();
            }
            st.push(make_pair(i, current));
        }

        return answer;
    }
};
```

---

## Notes

- A simple usage of stack, the trick here is to maintain a stack with its index position and temperature. This stack will always be monotonically decreasing.
- This is because as we iterate through to the temperatures array, we check if the current temperature is greater than the top of the stack, if it is find the difference between the indexes and update the answer array and pop it from the stack. This results in a monotonically decreasing stack. Repeat this until the current temperature is not greater than the top of the stack.
