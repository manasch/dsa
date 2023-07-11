[[79] - Word Search](https://leetcode.com/problems/word-search)

---

- Medium
- [Submission](https://leetcode.com/problems/word-search/submissions/991931759/)
- array, backtracking, matrix

---

## Problem Statement

<p>Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> <em>if</em> <code>word</code> <em>exists in the grid</em>.</p>

<p>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;ABCCED&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;SEE&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;ABCB&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 6</code></li>
	<li><code>1 &lt;= word.length &lt;= 15</code></li>
	<li><code>board</code> and <code>word</code> consists of only lowercase and uppercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you use search pruning to make your solution faster with a larger <code>board</code>?</p>


---

## Solution

```cpp
class Solution {
private:
    string build;
    int m, n;
    bool helper(vector<vector<char>>& board, string word, vector<bool>& visited, int i, int j, int index) {
        // cout << i << " " << j << " " << index << endl;
        if (i < 0 || j < 0 || i == m || j == n) {
            return false;
        }
        int visit = i * n + j;
        if (visited[visit]) {
            return false;
        }
        if (board[i][j] != word[index]) {
            return false;
        }
        if (index == word.size() - 1) {
            cout << "matched" << endl;
            return true;
        }
        visited[visit] = true;
        bool r = helper(board, word, visited, i, j + 1, index + 1);
        bool d = helper(board, word, visited, i + 1, j, index + 1);
        bool l = helper(board, word, visited, i, j - 1, index + 1);
        bool u = helper(board, word, visited, i - 1, j, index + 1);
        visited[visit] = false;
        return (r || d || l || u);
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        vector<bool> visited(m * n, false);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                // cout << "Entered" << endl;
                if (helper(board, word, visited, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

---

## Notes

- Iterate through each element of the matrix, begin matching by choosing the directions, keep a visited array to check if the character has already been visited.
- Backtrack if the word has not been found and continue the other direction.
