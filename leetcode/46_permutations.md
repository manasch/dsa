[[46] - Permutations](https://leetcode.com/problems/permutations)

---

- Medium
- [Submission](https://leetcode.com/problems/permutations/submissions/991625397/)
- [Submission](https://leetcode.com/problems/permutations/submissions/991629851/)
- array, backtracking

---

## Problem Statement

<p>Given an array <code>nums</code> of distinct integers, return <em>all the possible permutations</em>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    void dfs(vector<int>& nums, vector<int>& set, vector<bool>& map, vector<vector<int>>& result) {
        if (set.size() == nums.size()) {
            result.push_back(set);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (!map[i]) {
                map[i] = true;
                set.push_back(nums[i]);
                dfs(nums, set, map, result);
                map[i] = false;
                set.pop_back();
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> set;
        vector<bool> map(nums.size(), false);

        dfs(nums, set, map, result);
        return result;
    }
};
```

```cpp
class Solution {
private:
    void dfs(vector<int>& nums, vector<vector<int>>& result, int index) {
        if (index == nums.size()) {
            result.push_back(nums);
            return;
        }

        for (int i = index; i < nums.size(); ++i) {
            swap(nums[i], nums[index]);
            dfs(nums, result, index + 1);
            swap(nums[i], nums[index]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        dfs(nums, result, 0);
        return result;
    }
};
```

---

## Notes

- The first method involves keeping an extra data structure and an additional `O(n)` traversal of the array to check what all has been added and decide to add it to the set. Once this size reaches the same size as the nums size, it can be appended to the result set.
- This method has an extra space and time usage.

- The second method involves manipulating the input array by swapping the elements. This reduces the extra space and the extra time for lookup.
- The problem is reduced to smaller problems by picking which element takes the first place at each level.
