[[201] - Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range)

---

- Medium
- [Submission](https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/1182194701/)
- bit-manipulation
- Contest: none

---

## Problem Statement

<p>Given two integers <code>left</code> and <code>right</code> that represent the range <code>[left, right]</code>, return <em>the bitwise AND of all numbers in this range, inclusive</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 5, right = 7
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 0, right = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> left = 1, right = 2147483647
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= left &lt;= right &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int count = 0;
        while (left != right) {
            left >>= 1;
            right >>= 1;
            ++count;
        }
        return (left << count);
    }
};
```

---

## Notes

- Essentially trying to find the first digit where it defers, because everything to the left of it will be the same.
- Trying to find the common prefix, and everything after that will be replaced by 0's.
