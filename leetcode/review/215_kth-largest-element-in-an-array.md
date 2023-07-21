[[215] - Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

---

- Medium
- [Submission](https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/998276910/)
- array, divide-and-conquer, sorting, heap-priority-queue, quickselect

---

## Problem Statement

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>largest element in the array</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Can you solve it without sorting?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq(nums.begin(), nums.end());

        while (pq.size() > k) {
            pq.pop();
        }
        return pq.top();
    }
};
```

---

## Notes

- A faster method called `QuickSelect` exists.
- Create a min-heap of the existing numbers and pop until k elements remain to get the k'th largest element.
- Or, push all the elements to a heap and pop when the size exceeds k, once all elements have been pushed, pop and return the value.
