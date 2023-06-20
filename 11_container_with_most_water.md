# [[11] - Container With Most Water](https://leetcode.com/problems/container-with-most-water)

---

- Medium
- [Submission](https://leetcode.com/problems/container-with-most-water/submissions/902209584/)

### cpp
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int area = 0;

        while (l < r) {
            area = max(area, (r - l) * min(height[l], height[r]));
            if (height[l] > height[r])
                --r;
            else
                ++l;
        }
        return area;
    }
};
```

---

## Notes

- We want the greatest area possible, therefore we check the largest width possible, and then decreament the pointer depending on which of the heights is the smaller one.
