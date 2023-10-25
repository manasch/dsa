[[779] - K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar)

---

- Medium
- [Submission](https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/1083529298)
- math, bit-manipulation, recursion

---

## Problem Statement

<p>We build a table of <code>n</code> rows (<strong>1-indexed</strong>). We start by writing <code>0</code> in the <code>1<sup>st</sup></code> row. Now in every subsequent row, we look at the previous row and replace each occurrence of <code>0</code> with <code>01</code>, and each occurrence of <code>1</code> with <code>10</code>.</p>

<ul>
	<li>For example, for <code>n = 3</code>, the <code>1<sup>st</sup></code> row is <code>0</code>, the <code>2<sup>nd</sup></code> row is <code>01</code>, and the <code>3<sup>rd</sup></code> row is <code>0110</code>.</li>
</ul>

<p>Given two integer <code>n</code> and <code>k</code>, return the <code>k<sup>th</sup></code> (<strong>1-indexed</strong>) symbol in the <code>n<sup>th</sup></code> row of a table of <code>n</code> rows.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> row 1: <u>0</u>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
row 1: 0
row 2: <u>0</u>1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
row 1: 0
row 2: 0<u>1</u>
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 30</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>n - 1</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int kthGrammar(int n, int k) {
        if (n == 1) {
            return 0;
        }
        int count = pow(2, n - 1);
        if (k > count / 2) {
            return 1 - kthGrammar(n - 1, k - (count / 2));
        }
        else {
            return kthGrammar(n - 1, k);
        }
    }
};
```

---

## Notes

- This is kind of similar to a binary search.
- Basically have to figure out the number of flips that are required from the start.
- A pattern can be noticed where the digits are basically reverse in the second half, and that the prev binary string is a prefix of the current binary string.
- At any level, the length of the binary string is `2^(n - 1)` for nth level.
- If the kth value lies outside half of the length, then the bit is flipped, if it lies in the first half, it remains as it is.
- This can be done recursively or iteratively, and also with a binary search like approach by starting off with a 0, and flipping when the kth position is greater than mid and keeping it the same when it mid or less.
