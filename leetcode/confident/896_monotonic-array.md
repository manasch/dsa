[[896] - Monotonic Array](https://leetcode.com/problems/monotonic-array)

---

- Easy
- [Submission](https://leetcode.com/problems/monotonic-array/submissions/1061949696/)
- array

---

## Problem Statement

<p>An array is <strong>monotonic</strong> if it is either monotone increasing or monotone decreasing.</p>

<p>An array <code>nums</code> is monotone increasing if for all <code>i &lt;= j</code>, <code>nums[i] &lt;= nums[j]</code>. An array <code>nums</code> is monotone decreasing if for all <code>i &lt;= j</code>, <code>nums[i] &gt;= nums[j]</code>.</p>

<p>Given an integer array <code>nums</code>, return <code>true</code><em> if the given array is monotonic, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,4]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool flag1 = true;
        bool flag2 = true;
        int n = nums.size();

        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                flag1 = false;
            }
            if (nums[i] < nums[i - 1]) {
                flag2 = false;
            }

            if (!(flag1 || flag2)) {
                return false;
            }
        }
        return true;
    }
};
```

---

## Notes

- Keep 2 flags to perform the checks in one pass.
- One flag for decreasing and the other for increasing, at any iteration, if both are set to false, then return it there, else if it traverses the entire array, return true.
