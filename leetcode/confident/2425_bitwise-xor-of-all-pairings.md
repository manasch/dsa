[[2425] - Bitwise XOR of All Pairings](https://leetcode.com/problems/bitwise-xor-of-all-pairings)

---

- Medium
- [Submission](https://leetcode.com/problems/bitwise-xor-of-all-pairings/submissions/1510171972/)
- [Submission](https://leetcode.com/problems/bitwise-xor-of-all-pairings/submissions/1510182333/)
- array, bit-manipulation, brainteaser
- Contest: none

---

## Problem Statement

<p>You are given two <strong>0-indexed</strong> arrays, <code>nums1</code> and <code>nums2</code>, consisting of non-negative integers. There exists another array, <code>nums3</code>, which contains the bitwise XOR of <strong>all pairings</strong> of integers between <code>nums1</code> and <code>nums2</code> (every integer in <code>nums1</code> is paired with every integer in <code>nums2</code> <strong>exactly once</strong>).</p>

<p>Return<em> the <strong>bitwise XOR</strong> of all integers in </em><code>nums3</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,1,3], nums2 = [10,2,5,0]
<strong>Output:</strong> 13
<strong>Explanation:</strong>
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        auto xorthem = [] (vector<int>& arr) -> int {
            int r = arr[0];
            for (int i = 1; i < arr.size(); ++i) {
                r ^= arr[i];
            }
            return r;
        };

        if (n1 == 0 && n2 == 0) {
            return 0;
        }
        else if ((n1 == 0 || n1 % 2 == 0) && (n2 != 0 && n2 % 2)) {
            return xorthem(nums1);
        }
        else if ((n2 == 0 || n2 % 2 == 0) && (n1 != 0 && n1 % 2)) {
            return xorthem(nums2);
        }
        else if (n1 != 0 && n2 != 0 && n1 % 2 && n2 % 2) {
            return xorthem(nums1) ^ xorthem(nums2);
        }
        return 0;
    }
};
```

```cpp
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        auto xorthem = [] (vector<int>& arr) -> int {
            int r = 0;
            for (int i = 0; i < arr.size(); ++i) {
                r ^= arr[i];
            }
            return r;
        };

        int res = 0;
        if (n1 % 2) {
            res ^= xorthem(nums2);
        }
        if (n2 % 2) {
            res ^= xorthem(nums1);
        }
        return res;
    }
};
```

---

## Notes

- A bitwise of all pairings will result in multiple occurences of the same values being xor'd.
- xor of the same number is 0, hence, the final xor depends on the size of the array.
- If both the arrays are even, the result is 0.
- If one of the arrays is even, and the other is odd, the result is the xor of the even array.
- If both the arrays are odd, then the result is the xor of both the arrays.

- The simpler solution is that, only consider xor'ring the result, if the array size is odd.
