[[34] - Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

---

- Medium
- [Submission](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1004559001/)
- array, binary-search

---

## Problem Statement

<p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result(2, -1);
        // mergeSearch(nums, result, 0, nums.size() - 1, target);
        result[0] = binarySearch(nums, 0, nums.size() - 1, target, false);
        result[1] = binarySearch(nums, 0, nums.size() - 1, target, true);
        return result;        
    }
private:
    // int mergeSearch(vector<int>& nums, vector<int>& result, int start, int end, int target) {
    //     int pivot = binarySearch(nums, start, end, target);
    //     if (pivot == -1 || start > end) {
    //         return -1;
    //     }
    //     int left = mergeSearch(nums, result, start, pivot - 1, target);
    //     int right = mergeSearch(nums, result, pivot + 1, end, target);
    //     result[0] = left == -1 ? pivot : min(left, result[0]);
    //     result[1] = right == -1 ? pivot : max(right, result[1]);
    //     return pivot;
    // }
    int binarySearch(vector<int>& nums, int start, int end, int target, bool flag) {
        int mid;
        int val = -1;
        while (start <= end) {
            mid = start + ((end - start) >> 1);
            if (nums[mid] == target) {
                val = mid;
                if (flag) {
                    start = mid + 1;
                }
                else {
                    end = mid - 1;
                }
            }
            else if (nums[mid] > target) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        return val;
    }
};
```

---

## Notes

- Initially I planned to try out a merge sort + binary search approach, didn't work.
- Otherwise it's really simple, keep a flag that determines to continue search in left or right even after target is found.
