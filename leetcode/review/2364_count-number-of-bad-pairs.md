[[2364] - Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs)

---

- Medium
- [Submission](https://leetcode.com/problems/count-number-of-bad-pairs/submissions/1536684971/)
- array, hash-table, math, counting
- Contest: none

---

## Problem Statement

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. A pair of indices <code>(i, j)</code> is a <strong>bad pair</strong> if <code>i &lt; j</code> and <code>j - i != nums[j] - nums[i]</code>.</p>

<p>Return<em> the total number of <strong>bad pairs</strong> in </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,1,3,3]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no bad pairs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        long long n = nums.size();
        vector<long long> diff(n);
        unordered_map<long long, long long> diffMap;
        for (long long i = 0; i < n; ++i) {
            diff[i] = nums[i] - i;
            ++diffMap[diff[i]];
        }

        long long res = 0;
        for (auto const& [_, v]: diffMap) {
            res += ((v - 1) * v) >> 1;
        }
        return (((n - 1) * n) >> 1) - res;
    }
};
```

```cpp
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        long long badPairs = 0;
        unordered_map<int, int> diffCount;

        for (int pos = 0; pos < nums.size(); pos++) {
            int diff = pos - nums[pos];

            // Count of previous positions with same difference
            int goodPairsCount = diffCount[diff];

            // Total possible pairs minus good pairs = bad pairs
            badPairs += pos - goodPairsCount;

            // Update count of positions with this difference
            diffCount[diff] = goodPairsCount + 1;
        }

        return badPairs;
    }
};
```

---

## Notes

- instead of finding the total number of bad pairs, if we can find the total number of good pairs and subtract it from the total number of pairs, can arrive at the same answer. was able to deduce this logic.

- thought of this, but idk why i didn't utilize it, but instead of doing `nums[j] - nums[i] == j - i`, can do `nums[i] - i == nums[j] - j`. did this in another problem before, similar approach. equation re-arranging was the key.

- with this, find the count of each diff, with that, count good pairs for each diff, and subtract the total sum from the number of total pairs

- can also just keep a running count of the good paris till `j`. at `j`, the total number of pairs that can be formed is `j` as `j` can form a pair with any index from `0` to `j - 1`. with this, the count of good pairs is determined by the count stored in the map.
