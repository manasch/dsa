# [[125] - Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

---

- Easy
- [Submission](https://leetcode.com/problems/valid-palindrome/submissions/887289621/)

### cpp
```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;

        while (i < j) {
            while (!isalnum(s[i]) && i < j) i++;
            while (!isalnum(s[j]) && i < j) j--;

            if (tolower(s[i]) != tolower(s[j])) return false;
            ++i; --j;
        }

        return true;
    }
};
```

---

## Notes

- Take two pointers, keep one at the start, one at the end, if at any point, the characters aren't equal, exit, otherwise it is a palindrome
