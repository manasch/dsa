# [[48] - Rotate Image](https://leetcode.com/problems/rotate-image/)

---

- Medium
- [Submission](https://leetcode.com/submissions/detail/787025436/)

### cpp
```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix[0].size();
        int t;
        
        for(int i = 0; i < n; i++) {
            for(int j = i; j < n; j++){
                t = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = t;
            }
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n/2; j++){
                t = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = t;
            }
        }
    }
};
```

---

## Notes

- This was a simple problem involving a matrix trick. The problem requires us to rotate a 2D array of numbers clockwise.
- The trick involves first transposing the matrix and then reflecting the matrix on the vertical axis, which results in the rotated image.
