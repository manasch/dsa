[[1726] - Tuple with Same Product](https://leetcode.com/problems/tuple-with-same-product)

---

- Medium
- [Submission](https://leetcode.com/problems/tuple-with-same-product/submissions/1533495920/)
- array, hash-table, counting
- Contest: none

---

## Problem Statement

<p>Given an array <code>nums</code> of <strong>distinct</strong> positive integers, return <em>the number of tuples </em><code>(a, b, c, d)</code><em> such that </em><code>a * b = c * d</code><em> where </em><code>a</code><em>, </em><code>b</code><em>, </em><code>c</code><em>, and </em><code>d</code><em> are elements of </em><code>nums</code><em>, and </em><code>a != b != c != d</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,4,6]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,4,5,10]
<strong>Output:</strong> 16
<strong>Explanation:</strong> There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>All elements in <code>nums</code> are <strong>distinct</strong>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> prodMaps;

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                ++prodMaps[nums[i] * nums[j]];
            }
        }

        int res = 0;
        for (auto [key, val]: prodMaps) {
            int num = ((val) * (val - 1)) >> 1;
            res += 8 * num;
        }
        return res;
    }
};
```

---

## Notes

- find number of pairs that have the same product.
- for 2 pairs that are picked, there can be 8 permutations.
- a handshake of one pair to every other pair can be picked as the two pairs participating in the permutation, hence `n(n - 1) / 2` for each product where count of paris is greater than 1.
- find the some of all such product count pairs.
