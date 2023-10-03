[[1512] - Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs)

---

- Easy
- [Submission](https://leetcode.com/problems/number-of-good-pairs/submissions/1065569332/)
- array, hash-table, math, counting

---

## Problem Statement

<p>Given an array of integers <code>nums</code>, return <em>the number of <strong>good pairs</strong></em>.</p>

<p>A pair <code>(i, j)</code> is called <em>good</em> if <code>nums[i] == nums[j]</code> and <code>i</code> &lt; <code>j</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,1,3]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Each pair in the array are <em>good</em>.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> f;
        int res = 0;

        for (int x: nums) {
            if (f.find(x) == f.end()) {
                f.insert({x, 1});
            }
            else {
                res += f[x];
                ++f[x];
            }
        }
        return res;
    }
};
```

---

## Notes

- Brute Force would be O(n^2).
- Keep track of if the number has appeared till now, if it has, those many new pairs will be formed.
