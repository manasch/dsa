[[1014] - Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair)

---

- Medium
- [Submission](https://leetcode.com/problems/best-sightseeing-pair/submissions/1489531646/)
- array, dynamic-programming
- Contest: none

---

## Problem Statement

<p>You are given an integer array <code>values</code> where values[i] represents the value of the <code>i<sup>th</sup></code> sightseeing spot. Two sightseeing spots <code>i</code> and <code>j</code> have a <strong>distance</strong> <code>j - i</code> between them.</p>

<p>The score of a pair (<code>i &lt; j</code>) of sightseeing spots is <code>values[i] + values[j] + i - j</code>: the sum of the values of the sightseeing spots, minus the distance between them.</p>

<p>Return <em>the maximum score of a pair of sightseeing spots</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> values = [8,1,5,2,6]
<strong>Output:</strong> 11
<strong>Explanation:</strong> i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> values = [1,2]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= values.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= values[i] &lt;= 1000</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int n = values.size();
        stack<int> st;
        int maxVal = INT_MIN;

        for (int i = n - 1; i > 0; --i) {
            maxVal = max(maxVal, values[i] - i);
            st.push(maxVal);
        }

        int res = 0;
        for (int i = 0; i < n - 1; ++i) {
            int current = values[i] + i + st.top();
            st.pop();
            res = max(res, current);
        }
        return res;
    }
};

/*

8 1 5 2 6
8 2 7 5 10
8 0 3 -1 2
*/
```

---

## Notes

- While there is a better approach, this is what first struck to me.
- Essentially, convert the problem from `values[i] + values[j] + i - j` to `(values[i] + i) + (values[j] - j)`.

- This makes it into a simpler problem, where you have to find the max sum of the first part and second part.
- The second part can be stored is a maxStack (not required if you do it as you iterate right to left).
- Another iteration will give you the current value + top of the max stack as the largest value for the second part.


- The more optimized approach would be to calculate the second part on the go and keep the max value of the first part as this would ensure all possible values are covered.
