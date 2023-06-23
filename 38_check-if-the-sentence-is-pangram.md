# [[38] - Count and Say](https://leetcode.com/problems/count-and-say/)

---

- Medium
- [Submission](https://leetcode.com/submissions/detail/825055729/)

### cpp
```cpp
class Solution {
public:
    string countAndSay(int n) {
        string ans = "1";
        
        if (n == 1) return ans;
        
        int c = 0;
        string temp;
        while (--n) {
            c = 0;
            temp = "";
            for (int i = 1; i < ans.size(); ++i) {
                if (ans[i] == ans[i - 1]) {
                    ++c;
                } else {
                    ++c;
                    temp += to_string(c);
                    temp += ans[i - 1];
                    c = 0;
                }
            }
            ++c;
            temp += to_string(c);
            temp += ans[ans.size() - 1];
            
            ans = temp;
        }

        return ans;
    }
};
```

---

## Notes

- Got this on first try, but it looks to be a problem that doesn't really teach you anything.
- The solution just involves running a loop `n` number of times and parsing the string.
- Start from index 1, keep a counter for each number, check if the number at current index is same as previous, if yes increament count, else just append to a temp string, reset count, and change the main string as the temp. This process will repeat `n` times.
