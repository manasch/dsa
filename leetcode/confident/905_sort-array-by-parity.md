[[905] - Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity)

---

- Easy
- [Submission](https://leetcode.com/problems/sort-array-by-parity/submissions/1061065216/)
- array, two-pointers, sorting

---

## Problem Statement

<p>Given an integer array <code>nums</code>, move all the even integers at the beginning of the array followed by all the odd integers.</p>

<p>Return <em><strong>any array</strong> that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,2,4]
<strong>Output:</strong> [2,4,3,1]
<strong>Explanation:</strong> The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int n = nums.size();
        int l = 0, r = n - 1;

        while (l < r) {
            while (l < r && nums[l] % 2 == 0) {
                ++l;
            }
            while (l < r && nums[r] % 2 == 1) {
                --r;
            }
            swap(nums[l], nums[r]);
        }
        return nums;
    }
};
```

---

## Notes

- A simple two pointer approach like the intermediate stage of a quick sort.
