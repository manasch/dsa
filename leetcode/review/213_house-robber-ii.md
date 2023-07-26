[[213] - House Robber II](https://leetcode.com/problems/house-robber-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/house-robber-ii/submissions/1004768509/)
- array, dynamic-programming

---

## Problem Statement

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int s = nums.size();
        if (s == 1) {
            return nums[0];
        }
        int r1 = 0;
        int r2 = 0;

        for (int i = 0; i < s - 1; ++i) {
            int t = max(nums[i] + r1, r2);
            r1 = r2;
            r2 = t;
        }
        int m1 = r2;

        r1 = 0;
        r2 = 0;
        for (int i = 1; i < s; ++i) {
            int t = max(nums[i] + r1, r2);
            r1 = r2;
            r2 = t;
        }
        return max(r2, m1);
    }
};
```

---

## Notes

- Somewhat beginning to understand this kind of dp.
- Take the max of prev or current + prev of prev
