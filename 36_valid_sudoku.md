# [[36] - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

---

- Medium
- [Submission](https://leetcode.com/problems/valid-sudoku/submissions/876542227/)

### cpp
```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        const int n = 9;
        int idx;
        int square;
        bool rowHashTable[n][n] = {false};
        bool colHashTable[n][n] = {false};
        bool sqrHashTable[n][n] = {false};

        /*
        Representing each small square as an index in a 2d matrix
              0 1 2 3 4 5 6 7 8            
           0 [[][][][][][][][][]]
           1 [[][][][][][][][][]]
           2 [[][][][][][][][][]]
           3 [[][][][][][][][][]]
           4 [[][][][][][][][][]]
           5 [[][][][][][][][][]]
           6 [[][][][][][][][][]]
           7 [[][][][][][][][][]]
           8 [[][][][][][][][][]]
        */
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == '.') continue;

                idx = board[i][j] - '0' - 1;
                square = (i / 3) * 3 + (j / 3);
                if (rowHashTable[i][idx] || colHashTable[j][idx] || sqrHashTable[square][idx]) {
                    return false;
                }

                rowHashTable[i][idx] = true;
                colHashTable[j][idx] = true;
                sqrHashTable[square][idx] = true;
            }
        }
        return true;
    }
};
```

---

## Notes

- We don't have to check if the sudoku given is solvable or correct, but only valid, there could be a case where a value could be contradicting with respect to the row, col and square. But this is still considered valid.
- Can create 3 2-d matrices and store the occurence of each, if the number occurs again, it will check that the boolean has been set to true and return false, this is easy for row and column.
- For the individual squares, the row would be decided by the little trick `(r/3)*3 + (c/3)`. This is just done to get the indexing into a 2d-array format. `O(n^2) or O(9^2).
