[[3151] - Special Array I](https://leetcode.com/problems/special-array-i)

---

- Easy
- [Submission](https://leetcode.com/problems/special-array-i/submissions/1527314028/)
- array
- Contest: none

---

## Problem Statement

<p>An array is considered <strong>special</strong> if every pair of its adjacent elements contains two numbers with different parity.<!-- notionvc: e6bed0fa-c67d-43a7-81b4-99fb85b99e98 --></p>

<p>You are given an array of integers <code>nums</code>. Return <code>true</code> if <code>nums</code> is a <strong>special</strong> array, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one element. So the answer is <code>true</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only two pairs: <code>(2,1)</code> and <code>(1,4)</code>, and both of them contain numbers with different parity. So the answer is <code>true</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,3,1,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums[1]</code> and <code>nums[2]</code> are both odd. So the answer is <code>false</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return true;
        }

        for (int i = 0; i < n - 1; ++i) {
            if ((nums[i] & 1) ^ (nums[i + 1] & 1) == 0) {
                return false;
            }
        }
        return true;
    }
};
```

---

## Notes

- parity refers to even or odd, just xor the lsb of adjacent elements, if that is the same, in that case return false, else true.
