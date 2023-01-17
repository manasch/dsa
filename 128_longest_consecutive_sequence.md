# [[128] - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-consecutive-sequence/submissions/879172294/)

### cpp
```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // unordered_set<int> hashSet(nums.begin(), nums.end());
        // int longest = 0;
        // int temp;

        // if (nums.size() == 0) return 0;

        // for (int x: nums) {
        //     temp = 1;
        //     while (hashSet.count(x - 1 - temp)) {
        //         ++temp;
        //     }
        //     longest = max(temp, longest);
        // }
        // return longest;
        unordered_set<int> hashSet(nums.begin(), nums.end());
        int longest = 0;
        int temp;

        for (int x: nums) {
            if (!hashSet.count(x + 1)) {
                temp = 1;
                while (hashSet.count(x - temp))
                    ++temp;
                
                longest = max(temp, longest);
            }
        }
        return longest;
    }
};
```

---

## Notes

- Generate a hashset (which is basically a set whose elements can be hashed so searching is `O(n)`).
- Iterate through every number in the nums array, for every number we just check if it is the last number in the sequence, this can be done by checking if a number after it exists. If it does, we keep going back till the number doesn't exist and stop the loop, This won't iterate n times for each number in the average case.
