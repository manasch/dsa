# [[242] - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

- Easy
- [Submission](https://leetcode.com/submissions/detail/866847879/)

### cpp
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if (s == t) return true;
        return false;
    }
};
```

---

## Notes

- Sorting both the strings and comparing them should do the trick, but sorting may take O(n) space as well, so time complexity of this would be O(nlogn)
