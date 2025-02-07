[[2948] - Make Lexicographically Smallest Array by Swapping Elements](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements)

---

- Medium
- [Submission](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/submissions/1519986082/)
- array, union-find, sorting
- Contest: none

---

## Problem Statement

<p>You are given a <strong>0-indexed</strong> array of <strong>positive</strong> integers <code>nums</code> and a <strong>positive</strong> integer <code>limit</code>.</p>

<p>In one operation, you can choose any two indices <code>i</code> and <code>j</code> and swap <code>nums[i]</code> and <code>nums[j]</code> <strong>if</strong> <code>|nums[i] - nums[j]| &lt;= limit</code>.</p>

<p>Return <em>the <strong>lexicographically smallest array</strong> that can be obtained by performing the operation any number of times</em>.</p>

<p>An array <code>a</code> is lexicographically smaller than an array <code>b</code> if in the first position where <code>a</code> and <code>b</code> differ, array <code>a</code> has an element that is less than the corresponding element in <code>b</code>. For example, the array <code>[2,10,3]</code> is lexicographically smaller than the array <code>[10,2,3]</code> because they differ at index <code>0</code> and <code>2 &lt; 10</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,3,9,8], limit = 2
<strong>Output:</strong> [1,3,5,8,9]
<strong>Explanation:</strong> Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,6,18,2,1], limit = 3
<strong>Output:</strong> [1,6,7,18,1,2]
<strong>Explanation:</strong> Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,28,19,10], limit = 3
<strong>Output:</strong> [1,7,28,19,10]
<strong>Explanation:</strong> [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<queue<int>> vq;
        unordered_map<int, int> groupMap;

        vector<int> sortedNums(nums);
        sort(sortedNums.begin(), sortedNums.end());

        queue<int> curr;
        int idx = 0;
        for (int i: sortedNums) {
            if (!curr.empty() && abs(curr.back() - i) > limit) {
                vq.push_back(curr);
                curr = queue<int>();
                ++idx;
            }
            curr.push(i);
            groupMap[i] = idx;
        }
        vq.push_back(curr);

        vector<int> res;
        for (int i: nums) {
            res.push_back(vq[groupMap[i]].front());
            vq[groupMap[i]].pop();
        }
        return res;
    }
};
```

---

## Notes


- if a subsequence has elements whose difference satisfy the limit, it can always be arranged in the ascending order.
- task is to find such components and arrange these components in ascending order.
- one way can be is to use union find to find the components and arrange them in ascending order of the specific groups.
- it is not necessary for the elements to be contiguous.

- a queue is used to determine whether the element in the sorted array goes to the right or left, determining a new component.
- if it is part of the same component, can push it to the right, else, that component is done, and we pop all the elements of the queue and sort them in indices that component belongs with the help of a map from the original array.
