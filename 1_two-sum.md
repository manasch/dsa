# [[1] - Two Sum](https://leetcode.com/problems/two-sum/)

---

- Easy
- [Submission](https://leetcode.com/problems/two-sum/submissions/866874456/)

### cpp
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        int diff;
        unordered_map<int, int> hashmap;
        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            diff = target - nums[i];
            if (hashmap[diff] != 0) {
                ans.push_back(hashmap[diff] - 1);
                ans.push_back(i);
            }
            else {
                hashmap[nums[i]] = i + 1;
            }
        }

        return ans;
    }
};
```

---

## Notes

- Iterate through the original list, and store it's occurence in a hashmap, the trick is checking if `target - nums[i]` exists in the hashmap rather than iterating through the same list again and again. `O(nlogn)`.