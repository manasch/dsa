[[130] - Surrounded Regions](https://leetcode.com/problems/surrounded-regions)

---

- Medium
- [Submission](https://leetcode.com/problems/surrounded-regions/submissions/1000863328/)
- array, depth-first-search, breadth-first-search, union-find, matrix

---

## Problem Statement

<p>Given an <code>m x n</code> matrix <code>board</code> containing <code>&#39;X&#39;</code> and <code>&#39;O&#39;</code>, <em>capture all regions that are 4-directionally&nbsp;surrounded by</em> <code>&#39;X&#39;</code>.</p>

<p>A region is <strong>captured</strong> by flipping all <code>&#39;O&#39;</code>s into <code>&#39;X&#39;</code>s in that surrounded region.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 550px; height: 237px;" />
<pre>
<strong>Input:</strong> board = [[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;O&quot;,&quot;O&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;X&quot;,&quot;O&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;O&quot;,&quot;X&quot;,&quot;X&quot;]]
<strong>Output:</strong> [[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;O&quot;,&quot;X&quot;,&quot;X&quot;]]
<strong>Explanation:</strong> Notice that an &#39;O&#39; should not be flipped if:
- It is on the border, or
- It is adjacent to an &#39;O&#39; that should not be flipped.
The bottom &#39;O&#39; is on the border, so it is not flipped.
The other three &#39;O&#39; form a surrounded region, so they are flipped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = [[&quot;X&quot;]]
<strong>Output:</strong> [[&quot;X&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is <code>&#39;X&#39;</code> or <code>&#39;O&#39;</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        m = board.size();
        n = board[0].size();
        unordered_set<int> noFlip;

        for (int i = 0; i < m; ++i) {
            dfs(board, noFlip, i, 0);
            dfs(board, noFlip, i, n - 1);
        }

        for (int j = 0; j < n; ++j) {
            dfs(board, noFlip, 0, j);
            dfs(board, noFlip, m - 1, j);
        }

        int index;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                index = n * i + j;
                if (board[i][j] == 'O' && noFlip.find(index) == noFlip.end()) {
                    board[i][j] = 'X';
                }
            }
        }
    }
private:
    int m, n;
    void dfs(vector<vector<char>>& board, unordered_set<int>& noFlip, int i, int j) {
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return;
        }
        if (board[i][j] == 'X') {
            return;
        }
        int index = n * i + j;
        if (noFlip.find(index) != noFlip.end()) {
            return;
        }

        noFlip.insert(index);
        dfs(board, noFlip, i - 1, j);
        dfs(board, noFlip, i, j + 1);
        dfs(board, noFlip, i + 1, j);
        dfs(board, noFlip, i, j - 1);
    }
};
```

---

## Notes

- Following up on `LC#417`. The '0' not to flip are the ones that are connected to the cells that are at the border and are '0'.
- Create a set of all the cells that are connected to the cell on the border and it is a '0'. Iterate and flip the ones which are not in the set.
