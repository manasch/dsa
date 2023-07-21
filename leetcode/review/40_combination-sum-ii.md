[[40] - Combination Sum II](https://leetcode.com/problems/combination-sum-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/combination-sum-ii/submissions/991875646/)
- array, backtracking

---

## Problem Statement

<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    vector<vector<int>> result;
    vector<int> current;
    void helper(vector<int>& candidates, int target, int total, int index) {
        // cout << index << " ";
        if (total == target) {
            result.push_back(current);
            return;
        }
        if (index == candidates.size() || total > target) {
            return;
        }

        current.push_back(candidates[index]);
        helper(candidates, target, total + candidates[index], index + 1);
        int temp = candidates[index];
        while (index < candidates.size() && candidates[index] == temp) {
            ++index;
        }
        current.pop_back();
        helper(candidates, target, total, index);
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        helper(candidates, target, 0, 0);
        return result;
    }
};
```

---

## Notes

- Similar logic to `LC#90`. Sort the candidates array, in the decision tree, at each node, decide whether to include the value or not.
- If not choosing it then skip all the dupes and make the same decision for the new value.
