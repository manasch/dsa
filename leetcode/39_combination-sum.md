[[39] - Combination Sum](https://leetcode.com/problems/combination-sum)

---

- Medium
- [Submission](https://leetcode.com/problems/combination-sum/submissions/991585825/)
- array, backtracking

---

## Problem Statement

<p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the <span data-keyword="frequency-array">frequency</span> of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    vector<vector<int>> result;
    vector<int> set;
    void helper(vector<int>& candidates, int target, int index, int combsum) {
        if (combsum == target) {
            result.push_back(set);
            return;
        }
        if (index >= candidates.size() || combsum > target) {
            return;
        }
        set.push_back(candidates[index]);
        helper(candidates, target, index, combsum + candidates[index]);
        set.pop_back();
        helper(candidates, target, index + 1, combsum);
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        helper(candidates, target, 0, 0);
        return result;
    }
};
```

---

## Notes

- In the decision tree, at each node we decide to include it or not, but to avoid duplicates, once we have decided to not include it, it will never be included in any of the other trees.
- A Bruteforce approach with backtracking helps solve this problem relatively easily.
- Pretty sure other ways to solve this exist, will try to do it in that way after learning more.
