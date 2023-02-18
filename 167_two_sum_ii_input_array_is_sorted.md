# [[167] - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

---

- Medium
- [Submission](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/900422394/)

### cpp
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0;
        int end = numbers.size() - 1;

        while (true) {
            if (numbers[start] + numbers[end] > target) --end;
            else if (numbers[start] + numbers[end] < target) ++start;
            else break;
        }

        vector<int> ans {start + 1, end + 1};
        return ans;
    }
};
```

---

## Notes

- Keep two pointers, one at the start and one at the end, if the sum of the numbers indicated by the pointers is greater than the target value, then decrement the right pointer, if the sum is smaller then increament the left pointer.
- This works because the array is sorted. When the sum is equal to target, return the indices + 1.
