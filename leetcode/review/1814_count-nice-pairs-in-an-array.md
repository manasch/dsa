[[1814] - Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array)

---

- Medium
- [Submission](https://leetcode.com/problems/count-nice-pairs-in-an-array/submissions/1103460283/)
- array, hash-table, math, counting

---

## Problem Statement

<p>You are given an array <code>nums</code> that consists of non-negative integers. Let us define <code>rev(x)</code> as the reverse of the non-negative integer <code>x</code>. For example, <code>rev(123) = 321</code>, and <code>rev(120) = 21</code>. A pair of indices <code>(i, j)</code> is <strong>nice</strong> if it satisfies all of the following conditions:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; nums.length</code></li>
	<li><code>nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])</code></li>
</ul>

<p>Return <em>the number of nice pairs of indices</em>. Since that number can be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [42,11,1,97]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [13,10,35,24,76]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        long long count = 0;
        const int mod = 1e9 + 7;
        
        auto revNum = [&] (int num) -> int {
            int rev = 0;
            while (num > 0) {
                rev = rev * 10 + (num % 10);
                num /= 10;
            }
            return rev;
        };

        unordered_map<int, long> diff;
        for (int num: nums) {
            ++diff[num - revNum(num)];
        }

        for (auto& [k, v]: diff) {
            if (v > 1) {
                count = (count + (((v) * ((v - 1))) / 2)) % mod;
            }
        }
        return count;
    }
};
```

---

## Notes

- I had to see the hint, it was basically `num[i] - rev(num[i]) == num[j] - rev(num[j])`.
- Find out the frequency all the `num - rev(num)` and just add `n * (n - 1) / 2` and add it up.
