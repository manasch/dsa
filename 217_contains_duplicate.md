# [[217] - Contains Duplicate](https://leetcode.com/problems/contains-duplicate//)

---

- Easy
- [Submission](https://leetcode.com/problems/contains-duplicate/submissions/866841513/)

### cpp
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        for (int x: nums) {
            if (hashmap[x] == 1) return true;
            hashmap[x]++;
        }
        return false;
    }
};
```

---

## Notes

- Run through the list and store each element seen in a hashmap, next time it is seen again, it would be in the map, return true
