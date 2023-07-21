[[1365] - How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number)

---

- Easy
- [Submission](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/977974313/)
- array, hash-table, sorting, counting

---

## Problem Statement

<p>Given the array <code>nums</code>, for each <code>nums[i]</code> find out how many numbers in the array are smaller than it. That is, for each <code>nums[i]</code> you have to count the number of valid <code>j&#39;s</code>&nbsp;such that&nbsp;<code>j != i</code> <strong>and</strong> <code>nums[j] &lt; nums[i]</code>.</p>

<p>Return the answer in an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,1,2,2,3]
<strong>Output:</strong> [4,0,1,1,3]
<strong>Explanation:</strong> 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,8]
<strong>Output:</strong> [2,1,0,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7]
<strong>Output:</strong> [0,0,0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> count(101, 0);
        for (auto x: nums) {
            ++count[x];
        }

        for (int i = 1; i < 101; ++i) {
            count[i] += count[i - 1];
        }

        vector<int> result;
        for (auto x: nums) {
            if (x) {
                result.push_back(count[x - 1]);
            }
            else {
                result.push_back(0);
            }
        }
        return result;
    }
};
```

---

## Notes

- This can easily be solved in quadratic time but getting it in linear is trickier, but with the help of the constraints, notice that it only takes values till 100.
- Can utilize another array of size 100 and initialize it's value to the count of the number times it appears in the `nums` array.
- Just take the prefix sum to get the number of values less than the current index.
- During retrieval, just get the previous index's value if it's not 0 otherwise just get 0.
