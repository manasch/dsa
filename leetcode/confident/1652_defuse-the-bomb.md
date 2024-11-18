[[1652] - Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb)

---

- Easy
- [Submission](https://leetcode.com/problems/defuse-the-bomb/submissions/1456028008/)
- array, sliding-window
- Contest: none

---

## Problem Statement

<p>You have a bomb to defuse, and your time is running out! Your informer will provide you with a <strong>circular</strong> array <code>code</code>&nbsp;of length of <code>n</code>&nbsp;and a key <code>k</code>.</p>

<p>To decrypt the code, you must replace every number. All the numbers are replaced <strong>simultaneously</strong>.</p>

<ul>
	<li>If <code>k &gt; 0</code>, replace the <code>i<sup>th</sup></code> number with the sum of the <strong>next</strong> <code>k</code> numbers.</li>
	<li>If <code>k &lt; 0</code>, replace the <code>i<sup>th</sup></code> number with the sum of the <strong>previous</strong> <code>k</code> numbers.</li>
	<li>If <code>k == 0</code>, replace the <code>i<sup>th</sup></code> number with <code>0</code>.</li>
</ul>

<p>As <code>code</code> is circular, the next element of <code>code[n-1]</code> is <code>code[0]</code>, and the previous element of <code>code[0]</code> is <code>code[n-1]</code>.</p>

<p>Given the <strong>circular</strong> array <code>code</code> and an integer key <code>k</code>, return <em>the decrypted code to defuse the bomb</em>!</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> code = [5,7,1,4], k = 3
<strong>Output:</strong> [12,10,16,13]
<strong>Explanation:</strong> Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> code = [1,2,3,4], k = 0
<strong>Output:</strong> [0,0,0,0]
<strong>Explanation:</strong> When k is zero, the numbers are replaced by 0. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> code = [2,4,9,3], k = -2
<strong>Output:</strong> [12,5,6,13]
<strong>Explanation:</strong> The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the <strong>previous</strong> numbers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == code.length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= code[i] &lt;= 100</code></li>
	<li><code>-(n - 1) &lt;= k &lt;= n - 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> prefix, res;

        if (k == 0) {
            return vector<int>(n, 0);
        }
        else if (k < 0) {
            reverse(code.begin(), code.end());
        }

        int runningSum = 0;
        for (int i = 0; i < n; ++i) {
            prefix.push_back(code[i] + runningSum);
            runningSum += code[i];
        }

        for (int i = 0; i < n; ++i) {
            int end = (i + abs(k));
            if (end < n) {
                res.push_back(prefix[abs(end)] - prefix[i]);
            }
            else {
                res.push_back((prefix[n - 1] - prefix[i]) + prefix[end % n]);
            }
        }

        if (k < 0) {
            reverse(res.begin(), res.end());
        }

        return res;
    }
};
```

---

## Notes

- The problem is the same for `k` being `-ve`, just have to work on the reverse of the `code` array.
- Create a prefix sum array, with this, if the next `k` elements are beyond the array, just take the sum of elements till the end of the array and wherever the `k`th element ends from the start.
- Otherwise, just take the normal sum from the difference of the elements of the prefix sum array.

- Another solution is to use a sliding window to keep track of the sum of the fixed window size, adjusting for the start and end using modulo.
