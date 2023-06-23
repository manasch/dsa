[[22] - Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

---

- Medium
- [Submission](https://leetcode.com/problems/generate-parentheses/submissions/883029205/)
- string, dynamic-programming, backtracking

---

## Problem Statement

<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<string> st;
    vector<string> res;
    void backtrack(int open, int close, int n) {
        if (open == close && open == n && close == n) {
            string temp = "";
            for (auto it = st.begin(); it != st.end(); ++it) {
                temp += *it;
            }
            res.push_back(temp);
            return;
        }

        if (open < n) {
            st.push_back("(");
            backtrack(open + 1, close, n);
            st.pop_back();
        }

        if (close < open) {
            st.push_back(")");
            backtrack(open, close + 1, n);
            st.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        backtrack(0, 0, n);
        return res;
    }
};
```

---

## Notes

- A good introduction to backtracking. I had a vague idea on how to do it but could not implement it.
- This problem involves using a stack to keep track of what and how many opening and closing brackets have been added.
- The main takeaway from the problem is that:
    1. Add `(` only when the number of opens is less than `n`.
    2. Add `)` only when the number of closes is less than opens.
    3. Add to the result vector when the number of opens and closes are same and equal to `n`.
- Easy to implement it in recursive fashion. Usually for many backtracking problems.
- Why stack and backtracking ? Hint could be that you have to generate permutation and combinations but not all of them fit the required condition, therefore many have to be cut off from the result.
