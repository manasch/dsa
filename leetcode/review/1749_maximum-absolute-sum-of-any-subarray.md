[[1749] - Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray)

---

- Medium
- [Submission](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/submissions/1556085448/)
- array, dynamic-programming
- Contest: none

---

## Problem Statement

<p>You are given an integer array <code>nums</code>. The <strong>absolute sum</strong> of a subarray <code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> is <code>abs(nums<sub>l</sub> + nums<sub>l+1</sub> + ... + nums<sub>r-1</sub> + nums<sub>r</sub>)</code>.</p>

<p>Return <em>the <strong>maximum</strong> absolute sum of any <strong>(possibly empty)</strong> subarray of </em><code>nums</code>.</p>

<p>Note that <code>abs(x)</code> is defined as follows:</p>

<ul>
	<li>If <code>x</code> is a negative integer, then <code>abs(x) = -x</code>.</li>
	<li>If <code>x</code> is a non-negative integer, then <code>abs(x) = x</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-3,2,3,-4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,-5,1,-4,3,-2]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int cur = 0;
        int preMax = 0;
        int preMin = 0;
        int res = 0;

        for (const int& num: nums) {
            cur += num;
            res = max(max(res, abs(cur - preMax)), abs(cur - preMin));
            preMax = max(preMax, cur);
            preMin = min(preMin, cur);
        }
        return res;
    }
};
```

---

## Notes

- this is similar to performing two kadane's algorithms at once.
- maintain the max and min prefix sums come by so far. we want to maximize the values towards both extremes (positive and negative).
- hence removing the maxprefix or minprefix from the current sum ensures that we will keep getting the max absolute subarray sum.
