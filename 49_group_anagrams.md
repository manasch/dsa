# [[49] - Group Anagrams](https://leetcode.com/problems/group-anagrams/)

---

- Medium
- [Submission](https://leetcode.com/problems/group-anagrams/submissions/866880192/)

### cpp
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> ans;
        string original;

        for (auto x: strs) {
            original = x;
            sort(x.begin(), x.end());
            hashmap[x].push_back(original);
        }

        for (auto [_, x]: hashmap) {
            ans.push_back(x);
        }
        
        return ans;
    }
};
```

---

## Notes

- Create a hashmap of the sorted string mapped to a vector of strings, this way after sorting, just append the string to the vector of strings whose sorted string matches the key. This is `O(m.nlogn)`, pretty slow.
- This can be made faster by exploiting the fact that only lowercase alphabets will be used, and hence just count the occurence of what all occurs how many times and use that as the key in the hashmap. `O(m.n.26) = O(m.n)` Uses extra space 26 everytime.
