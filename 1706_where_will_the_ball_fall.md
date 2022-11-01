# [[1706] - Where Will the Ball Fall](https://leetcode.com/problems/where-will-the-ball-fall/)

---

- Medium
- [Submission](https://leetcode.com/submissions/detail/834469860/)

### cpp
```cpp
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int trows = grid.size();
        int tcols = grid[0].size();
        int ccol, ncol;
        vector<int> ans(tcols, -1);
        
        for (int col = 0; col < tcols; ++col) {
            ccol = col;
            for (int row = 0; row < trows; ++row) {
                ncol = ccol + grid[row][ccol];
                if (ncol < 0 || ncol > tcols - 1 || grid[row][ccol] != grid[row][ncol]) {
                    ans[col] = -1;
                    break;
                }
                ans[col] = ncol;
                ccol = ncol;
            }
        }
        return ans;
    }
};
```

---

## Notes

- Basically need to check for conditions where the ball gets stuck to the walls or within the grid at the tip of a V shape.
- Depending on where the ball is going, need to check if it can go to the next column (left if left, right if right), this is possible when the slope in the current col is same as the slope of it's right adjacent if the ball is going right and vice versa.
- Next col can be calculated using `current col + current cell's slope value`.
