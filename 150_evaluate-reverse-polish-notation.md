# [[150] - Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation)

---

- Medium
- [Submission](https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/882388329/)

### cpp
```cpp
class Solution {
private:
    stack<int> st;
public:
    bool isOp(string x) {
        if (x == "+" | x == "-" | x == "*" | x == "/") return true;
        return false;
    }
    int evalRPN(vector<string>& tokens) {
        int op1, op2;
        for (auto x: tokens) {
            if (isOp(x)) {
                op1 = st.top();
                st.pop();
                op2 = st.top();
                st.pop();

                if (x == "+") st.push(op1 + op2);
                else if (x == "-") st.push(op2 - op1);
                else if (x == "*") st.push(op1 * op2);
                else if (x == "/") st.push(op2 / op1);
                else break;
            }
            else {
                st.push(stoi(x));
            }
        }
        return st.top();
    }
};
```

---

## Notes

- Reverse Polish Notation is just another cool name for Postfix Notation. Evaluating postfix notation is as follows.
- Traverse through the tokens, if the token is not an operator, push it to a stack, if it is an operator, then pop the top two elements of the stack, perform the operation and push it back to the stack.
- This will work as it is given that the tokens are from a valid postfix notation.
