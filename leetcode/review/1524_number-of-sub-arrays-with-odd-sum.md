[[1524] - Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum)

---

- Medium
- [Submission](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/submissions/1555243442/)
- array, math, dynamic-programming, prefix-sum
- Contest: none

---

## Problem Statement

<p>Given an array of integers <code>arr</code>, return <em>the number of subarrays with an <strong>odd</strong> sum</em>.</p>

<p>Since the answer can be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,4,6]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6,7]
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int cur = 0;
        int oddSum = 0;
        int evenSum = 0;
        int res = 0;
        int mod = 1e9 + 7;

        for (const int& num: arr) {
            cur += num;
            if ((cur & 1)) {
                ++oddSum;
                res = (res + 1 + evenSum) % mod;
            }
            else {
                ++evenSum;
                res = (res + oddSum) % mod;
            }
        }
        return res;
    }
};
```

---

## Notes

- uses a prefix logic. can keep track of the total number of odd sums and even sums come by so far.
- also keep track of the total sum so far, if that value is odd, can add that to the result along with the total number of evenSums, as odd - even is odd.
- similarly, if the current sum is even, add the number of oddSums so far.
