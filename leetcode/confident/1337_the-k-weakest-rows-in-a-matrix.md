[[1337] - The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix)

---

- Easy
- [Submission](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/1052312192)
- array, binary-search, sorting, heap-priority-queue, matrix

---

## Problem Statement

<p>You are given an <code>m x n</code> binary matrix <code>mat</code> of <code>1</code>&#39;s (representing soldiers) and <code>0</code>&#39;s (representing civilians). The soldiers are positioned <strong>in front</strong> of the civilians. That is, all the <code>1</code>&#39;s will appear to the <strong>left</strong> of all the <code>0</code>&#39;s in each row.</p>

<p>A row <code>i</code> is <strong>weaker</strong> than a row <code>j</code> if one of the following is true:</p>

<ul>
	<li>The number of soldiers in row <code>i</code> is less than the number of soldiers in row <code>j</code>.</li>
	<li>Both rows have the same number of soldiers and <code>i &lt; j</code>.</li>
</ul>

<p>Return <em>the indices of the </em><code>k</code><em> <strong>weakest</strong> rows in the matrix ordered from weakest to strongest</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
<strong>Output:</strong> [2,0,3]
<strong>Explanation:</strong> 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
<strong>Output:</strong> [0,2]
<strong>Explanation:</strong> 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>2 &lt;= n, m &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= m</code></li>
	<li><code>matrix[i][j]</code> is either 0 or 1.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        priority_queue<pair<int, int>> pq;

        int strength;
        for (int i = 0; i < m; ++i) {
            strength = 0;
            for (int j = 0; j < n && mat[i][j] != 0; ++j) {
                ++strength;
            }
            pq.push({strength, i});
            if (pq.size() > k) {
                pq.pop();
            }

        }

        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

---

## Notes

- A simple problem, just create a heap and keep popping when the size is above k, the result would be the result of the order of whatever is popped. Will be utilizing a Max-Heap of size K.
