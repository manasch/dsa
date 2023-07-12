[[51] - N-Queens](https://leetcode.com/problems/n-queens)

---

- Hard
- [Submission](https://leetcode.com/problems/n-queens/submissions/992911942/)
- array, backtracking

---

## Problem Statement

<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>all distinct solutions to the <strong>n-queens puzzle</strong></em>. You may return the answer in <strong>any order</strong>.</p>

<p>Each solution contains a distinct board configuration of the n-queens&#39; placement, where <code>&#39;Q&#39;</code> and <code>&#39;.&#39;</code> both indicate a queen and an empty space, respectively.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [[&quot;.Q..&quot;,&quot;...Q&quot;,&quot;Q...&quot;,&quot;..Q.&quot;],[&quot;..Q.&quot;,&quot;Q...&quot;,&quot;...Q&quot;,&quot;.Q..&quot;]]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[&quot;Q&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    bool isValid(vector<string>& board, int n, int i, int j) {
        for (int x = 0; x < n; ++x) {
            if (x != i && board[x][j] == 'Q') {
                return false;
            }
        }

        for (int y = 0; y < n; ++y) {
            if (y != j && board[i][y] == 'Q') {
                return false;
            }
        }

        for (int x = i, y = j; x >= 0 && x < n && y >= 0 && y < n; ++x, ++y) {
            if (x != i && y != j && board[x][y] == 'Q') {
                return false;
            }
        }

        for (int x = i, y = j; x >= 0 && x < n && y >= 0 && y < n; --x, ++y) {
            if (x != i && y != j && board[x][y] == 'Q') {
                return false;
            }
        }

        for (int x = i, y = j; x >= 0 && x < n && y >= 0 && y < n; ++x, --y) {
            if (x != i && y != j && board[x][y] == 'Q') {
                return false;
            }
        }

        for (int x = i, y = j; x >= 0 && x < n && y >= 0 && y < n; --x, --y) {
            if (x != i && y != j && board[x][y] == 'Q') {
                return false;
            }
        }
        return true;
    }
    void printBoard(vector<string>& board) {
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board.size(); ++j) {
            }
        }
    }
    void dfs(vector<vector<string>>& result, vector<string>& board, int n, int i, int j, int c) {
        if (c == n) {
            result.push_back(board);
            return;
        }
        for (int index = j; index < n; ++index) {
            board[i][index] = 'Q';
            // printBoard(board);
            bool res = isValid(board, n, i, index);
            if (res) {
                dfs(result, board, n, i + 1, 0, c + 1);
            }
            board[i][index] = '.';
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> result;
        dfs(result, board, n, 0, 0, 0);
        return result;
    }
};
```

---

## Notes

- Start from the first row, place a queen in the first col, everytime a queen is placed move to the next row and start placing the queen from the first col.
- Everytime a queen is placed check if it's not attacking any other queen and move ahead.
- Backtrack everytime it's placed in an invalid position and move to the next col.
