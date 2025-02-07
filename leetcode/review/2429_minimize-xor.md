[[2429] - Minimize XOR](https://leetcode.com/problems/minimize-xor)

---

- Medium
- [Submission](https://leetcode.com/problems/minimize-xor/submissions/1509122208/)
- greedy, bit-manipulation
- Contest: none

---

## Problem Statement

<p>Given two positive integers <code>num1</code> and <code>num2</code>, find the positive integer <code>x</code> such that:</p>

<ul>
	<li><code>x</code> has the same number of set bits as <code>num2</code>, and</li>
	<li>The value <code>x XOR num1</code> is <strong>minimal</strong>.</li>
</ul>

<p>Note that <code>XOR</code> is the bitwise XOR operation.</p>

<p>Return <em>the integer </em><code>x</code>. The test cases are generated such that <code>x</code> is <strong>uniquely determined</strong>.</p>

<p>The number of <strong>set bits</strong> of an integer is the number of <code>1</code>&#39;s in its binary representation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 3, num2 = 5
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer <strong>3</strong> has the same number of set bits as num2, and the value <code>3 XOR 3 = 0</code> is minimal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 1, num2 = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer <strong>3</strong> has the same number of set bits as num2, and the value <code>3 XOR 1 = 2</code> is minimal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1, num2 &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int minimizeXor(int num1, int num2) {
        unordered_set<int> setBits;
        int count = __builtin_popcount(num2);
        int flag = 1;
        int res = 0;
        flag <<= 30;
        while (count > 0 && flag > 0) {
            while (flag > 0 && (num1 & flag) != flag) {
                flag >>= 1;
            }
            if (flag <= 0) {
                break;
            }
            setBits.insert(flag);
            res |= flag;
            --count;
            flag >>= 1;
        }
        flag = 1;
        while (count--) {
            if (setBits.find(flag) != setBits.end()) {
                flag <<= 1;
                ++count;
                continue;
            }
            res |= flag;
            flag <<= 1;
        }
        return res;
    }
};
```

---

## Notes

- Need count of set bits in `num2`, create a `res` var starting from 0, and a `flag` that has the bit set from the msb.
- Keep setting the bits in the `res` var if the same bit is set in `num1`, this will ensure, that when `num1` is xor'd with `res`, it will result in the minimum value possible, as same values xor'd result in 0.
- If the count of set bits remain after the `flag` has reached 0, start setting the bits that were not set in the first iteration of `res` from right to left till the count is exhausted.
