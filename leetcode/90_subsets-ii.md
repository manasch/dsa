[[90] - Subsets II](https://leetcode.com/problems/subsets-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/subsets-ii/submissions/991854635/)
- array, backtracking, bit-manipulation

---

## Problem Statement

<p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span><em> (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    void helper(vector<int>& nums, vector<vector<int>>& result, vector<int>& current, int index) {
        if (index == nums.size()) {
            result.push_back(current);
            return;
        }

        current.push_back(nums[index]);
        helper(nums, result, current, index + 1);

        int temp = nums[index];
        while (index < nums.size() && nums[index] == temp) {
            ++index;
        }
        current.pop_back();
        helper(nums, result, current, index);
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> current;
        helper(nums, result, current, 0);
        return result;
    }
};
```

---

## Notes

- This is an extension of `LC#78` - subsets. It involves a similar decision of inclusion or exclusion.
- But since the list can have duplicates, sort the list such that the dupes are placed together.
- If including the element, proceed normally, but when not including the element, skip all the dupes and include the next element.
