[[347] - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

---

- Medium
- [Submission](https://leetcode.com/problems/top-k-frequent-elements/submissions/871377021/)
- array, hash-table, divide-and-conquer, sorting, heap-priority-queue, bucket-sort, counting, quickselect

---

## Problem Statement

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>


---

## Solution

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> hashmap;
        for (auto x: nums) {
            hashmap[x]++;
        }

        vector<vector<int>> reverseIndex(n + 1);
        for (auto [k, i]: hashmap) {
            reverseIndex[i].push_back(k);
        }

        vector<int> ans;
        for (int i = n; i >= 0; --i) {
            if (ans.size() >= k) break;
            if (reverseIndex[i].size() != 0) {
                ans.insert(ans.end(), reverseIndex[i].begin(), reverseIndex[i].end());
            }
        }

        return ans;
    }
};
```

---

## Notes

- There are multiple ways to solve this problem, the obvious way to solve it would be to create a priority queue of the count of the elements and take the top k, but this would be `O(nlogn)`, this can be improved by taking a heap and only heapify it k times as we only need the top `k` frequent elements, hene making it `O(klogn)`.
- There's an even faster way by using bucket sort, or somewhat of a reverse index, where the index is the count and the value is a vector of elements with that count, the list length is fixed to the length of the given nums list and therefore just iterating through the back of this list and getting the `k` elements will give the answer, `O(n)` space and time.
