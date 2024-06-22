[[3190] - Find Minimum Operations to Make All Elements Divisible by Three](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three)

---

- Easy
- [Submission](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/submissions/1296694887/)
- 
- Contest: [biweekly-contest-133](https://leetcode.com/contest/biweekly-contest-133/)

---

## Problem Statement

<p>You are given an integer array <code>nums</code>. In one operation, you can add or subtract 1 from <strong>any</strong> element of <code>nums</code>.</p>

<p>Return the <strong>minimum</strong> number of operations to make all elements of <code>nums</code> divisible by 3.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All array elements can be made divisible by 3 using 3 operations:</p>

<ul>
	<li>Subtract 1 from 1.</li>
	<li>Add 1 to 2.</li>
	<li>Subtract 1 from 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,6,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int count = 0;
        for (int num: nums) {
            count += min(num % 3, 3 - num % 3);
        }
        return count;
    }
};
```

---

## Notes

- All that needed to be checked was how far the number was from the nearest number divisible by 3. Add up all the differences to get the answer
