[[78] - Subsets](https://leetcode.com/problems/subsets)

---

- Medium
- [Submission](https://leetcode.com/problems/subsets/submissions/991155824/)
- [Submission](https://leetcode.com/problems/subsets/submissions/991161754/)
- array, backtracking, bit-manipulation

---

## Problem Statement

<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    vector<vector<int>> result;
    vector<int> subset;
    void dfs(vector<int>& nums, int index) {
        if (index == nums.size()) {
            result.push_back(subset);
            return;
        }
        subset.push_back(nums[index]);
        dfs(nums, index + 1);
        subset.pop_back();
        dfs(nums, index + 1);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(nums, 0);
        return result;
    }
};
```

```cpp
class Solution {
private:
    vector<vector<int>> helper(vector<int>& nums, int n) {
        if (n == 0) {
            vector<vector<int>> subset;
            vector<int> nullset;
            subset.push_back(nullset);
            return subset;
        }

        vector<vector<int>> set1 = helper(nums, n - 1);
        vector<vector<int>> set2 = set1;

        for (int i = 0; i < set2.size(); ++i) {
            set2[i].push_back(nums[n - 1]);
        }

        set1.insert(set1.end(), set2.begin(), set2.end());
        return set1;
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        return helper(nums, nums.size());
    }
};
```

---

## Notes

- Multiple ways of solving this problem, a simple approach could be iterating through each element, and deciding whether to include that element or not.
- Another method could be building the subset list from ground up.
- The second method preserves the order at which the subsets are formed, at each call it doubles the number of elements by adding the last element to all the sets already existing in the subset array.
