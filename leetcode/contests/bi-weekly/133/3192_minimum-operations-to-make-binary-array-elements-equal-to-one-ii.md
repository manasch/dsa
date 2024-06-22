[[3192] - Minimum Operations to Make Binary Array Elements Equal to One II](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/submissions/1296796892/)
- 
- Contest: [biweekly-contest-133](https://leetcode.com/contest/biweekly-contest-133/)

---

## Problem Statement

<p>You are given a <span data-keyword="binary-array">binary array</span> <code>nums</code>.</p>

<p>You can do the following operation on the array <strong>any</strong> number of times (possibly zero):</p>

<ul>
	<li>Choose <strong>any</strong> index <code>i</code> from the array and <strong>flip</strong> <strong>all</strong> the elements from index <code>i</code> to the end of the array.</li>
</ul>

<p><strong>Flipping</strong> an element means changing its value from 0 to 1, and from 1 to 0.</p>

<p>Return the <strong>minimum</strong> number of operations required to make all elements in <code>nums</code> equal to 1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,1,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong><br />
We can do the following operations:</p>

<ul>
	<li>Choose the index <code>i = 1</code><span class="example-io">. The resulting array will be <code>nums = [0,<u><strong>0</strong></u>,<u><strong>0</strong></u>,<u><strong>1</strong></u>,<u><strong>0</strong></u>]</code>.</span></li>
	<li>Choose the index <code>i = 0</code><span class="example-io">. The resulting array will be <code>nums = [<u><strong>1</strong></u>,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<u><strong>0</strong></u>,<u><strong>1</strong></u>]</code>.</span></li>
	<li>Choose the index <code>i = 4</code><span class="example-io">. The resulting array will be <code>nums = [1,1,1,0,<u><strong>0</strong></u>]</code>.</span></li>
	<li>Choose the index <code>i = 3</code><span class="example-io">. The resulting array will be <code>nums = [1,1,1,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>.</span></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,0,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong><br />
We can do the following operation:</p>

<ul>
	<li>Choose the index <code>i = 1</code><span class="example-io">. The resulting array will be <code>nums = [1,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>.</span></li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int flips = 0;
        int cur = 0;
        
        for (int num: nums) {
            cur = (flips % 2 == 0 ? num : (num == 1 ? 0 : 1));
            if (cur == 0) {
                ++flips;
            }
        }
        return flips;
    }
};
```

---

## Notes

- This was surprisingly more simpler than problem 2.
- For each element have to check it's current value after applying the flips. Even flips result in the same number, odd flips result in the flipped number.
- After getting the current number, if the value is 0, we increment the flip, otherwise move on.
