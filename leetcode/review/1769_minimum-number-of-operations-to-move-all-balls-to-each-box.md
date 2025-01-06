[[1769] - Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box)

---

- Medium
- [Submission](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/submissions/1499764895/)
- [Submission](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/submissions/1499763671/)
- array, string, prefix-sum
- Contest: none

---

## Problem Statement

<p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>&#39;0&#39;</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>&#39;1&#39;</code> if it contains <strong>one</strong> ball.</p>

<p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

<p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

<p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;110&quot;
<strong>Output:</strong> [1,1,3]
<strong>Explanation:</strong> The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;001011&quot;
<strong>Output:</strong> [11,8,5,4,3,4]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == boxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>boxes[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> p1(n + 1, 0), p2(n + 1, 0);
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            p1[i] += p1[i - 1] + cnt;
            cnt += (boxes[i - 1] == '1' ? 1 : 0);
        }

        cnt = 0;
        for (int i = n - 1; i >= 0; --i) {
            p2[i] += p2[i + 1] + cnt;
            cnt += (boxes[i] == '1' ? 1 : 0);
        }
        
        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i) {
            res[i] = p1[i + 1] + p2[i];
        }
        return res;
    }
};
// 0 0 1 0 1 1
// 0 0 0 1 2 4
// 11 8 5 3 1 0
```

```cpp
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> p(n + 1, 0);
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            p[i] += p[i - 1] + cnt;
            cnt += (boxes[i - 1] == '1' ? 1 : 0);
        }

        vector<int> res(n, 0);
        cnt = 0;
        int next = 0;
        int curr = 0;
        for (int i = n - 1; i >= 0; --i) {
            curr = next + cnt;
            cnt += (boxes[i] == '1' ? 1 : 0);
            next = curr;
            res[i] = p[i + 1] + curr;
        }

        return res;
    }
};
// 0 0 1 0 1 1
// 0 0 0 0 1 2 4
// 11 8 5 3 1 0 0
```

---

## Notes

- This is a prefix sum approach, where at each index of the prefix sum, we keep track of how many times a `1` to the left of it has to move to reach the current index.
- This can be kept track of by adding the number of `1`'s come across with the previous value of the prefix sum.
- A similar thing can be applied in the reverse order and sum of both the arrays for the respective arrays can be achieved.

- A more efficient approach would be that, we don't even need to keep track of the 2nd prefix sum (we don't need the first prefix sum either, but that's different).
- Two variables are enough to keep track of the current and previous as we don't need the values beyond that.
