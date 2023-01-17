# [[20] - Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

---

- Easy
- [Submission](https://leetcode.com/problems/valid-parentheses/submissions/879958752/)

### cpp
```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        char t;
        for (char x: s) {
            switch(x) {
                case ')':
                    if (st.empty()) return false;
                    t = st.top();
                    st.pop();
                    if (t != '(') return false;
                    break;
                case '}':
                    if (st.empty()) return false;
                    t = st.top();
                    st.pop();
                    if (t != '{') return false;
                    break;
                case ']':
                    if (st.empty()) return false;
                    t = st.top();
                    st.pop();
                    if (t != '[') return false;
                    break;
                default:
                    st.push(x);
                    break;
            }
        }
        if (!st.empty())
            return false;
        return true;
    }
};
```

---

## Notes

- Use a stack to keep track of all the paranthesis that have occured, ensure that at the end the stack should be empty, also ensure that you can't pop an empty stack (This would occur if the first character in the string is a closing paranthesis).
