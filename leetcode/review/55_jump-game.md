[[55] - Jump Game](https://leetcode.com/problems/jump-game)

---

- Medium
- [Submission](https://leetcode.com/problems/jump-game/submissions/1017291294/)
- array, dynamic-programming, greedy

---

## Problem Statement

<p>You are given an integer array <code>nums</code>. You are initially positioned at the array&#39;s <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>

<p>Return <code>true</code><em> if you can reach the last index, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return true;
        }
        int l = 0, r = 0;
        bool flag = false;
        while (r < n) {
            while (r - l < nums[l]) {
                ++r;
            }
            if (r >= n - 1) {
                flag = true;
                break;
            }
            if (l >= r) {
                break;
            }
            ++l;
        }
        return flag;
    }
};
```

---

## Notes

- Initially I did a kind of dp, where I store the possibility of reaching the last index at each node and iterate backwards. This resulted in barely passing all test cases.
- Somehow I got the idea of using two pointers, both start at 0, move the right pointer till the difference is the value at index `l`.
- Now, shift `l` by one and repeat till either `r` reaches the end or `l` reaches `r`.
