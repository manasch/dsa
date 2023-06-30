[[287] - Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)

---

- Medium
- [Submission](https://leetcode.com/problems/find-the-duplicate-number/submissions/979288055/)
- array, two-pointers, binary-search, bit-manipulation

---

## Problem Statement

<p>Given an array of integers <code>nums</code> containing&nbsp;<code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.</p>

<p>There is only <strong>one repeated number</strong> in <code>nums</code>, return <em>this&nbsp;repeated&nbsp;number</em>.</p>

<p>You must solve the problem <strong>without</strong> modifying the array <code>nums</code>&nbsp;and uses only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li>All the integers in <code>nums</code> appear only <strong>once</strong> except for <strong>precisely one integer</strong> which appears <strong>two or more</strong> times.</li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b></p>

<ul>
	<li>How can we prove that at least one duplicate number must exist in <code>nums</code>?</li>
	<li>Can you solve the problem in linear runtime complexity?</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = nums[0];
        int slow = nums[0];

        do {
            fast = nums[nums[fast]];
            slow = nums[slow];
        } while (fast != slow);

        slow = nums[0];
        while (slow != fast) {
            fast = nums[fast];
            slow = nums[slow];
        }

        return slow;
    }
};
```

---

## Notes

- I knew about this from before, there are many ways to obtain this but at the cost of it not being `O(1)` memory.
- It's the famous tortoise v hare problem where the array is treated as a linked list with a cycle as the duplicate numbers would result in a cycle.
- After reducing it to a linked list with a cycle, the goal is to find the entrance to the cycle. The hare moves twice as fast as the tortise. Hence it would have entered the cycle earlier and meet the tortise again at some point in the cycle.
- The entrance can then be found by letting the hare and tortise move at the same place, but this time the hare starts from the intersection point and the tortise starts from the beginning.

- Another approach is the binary search where a range is searched, this range is decided by the fact the number to be found can't be greater than the size of the array. Hence the lower limit is 1 and the higher limit is the size of the array.
- In a regular array of size n filled with numbers [1, n] inclusive, the number of numbers that are less than or equal to a certain number is the number itself. But with dupes that becomes itself and greater. The smallest number to have the number of numbers itself and greater is the number we are trying to find.
- The binary search kicks in to reduce the search space.
