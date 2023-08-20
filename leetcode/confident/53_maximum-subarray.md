[[53] - Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

---

- Medium
- [Submission](https://leetcode.com/problems/maximum-subarray/submissions/1026968584/)
- array, divide-and-conquer, dynamic-programming

---

## Problem Statement

<p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>


---

## Solution

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = -1e5;
        int sum = 0;
        int r = 0, l = 0;
        int n = nums.size();

        while (r < n) {
            sum += nums[r];
            maxSum = max(maxSum, sum);
            if (sum <= 0) {
                sum = 0;
            }
            ++r;
        }
        return maxSum;
    }
};
```

---

## Notes

- So I had apparently done this problem before, but never submitted it, this soln has a little extra stuff but is very similar to what I saw from a video before.
- If at any point in time, the sum becomes negative, just reset the sum and continue, but what if the entire array is -ve, then just keep track of the largest negative number.
- I don't really require initializing maxSum to `-1e5`, but rather just have it be the first value in the array and keep updating max value.
