[[20] - Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

---

- Easy
- [Submission](https://leetcode.com/problems/valid-parentheses/submissions/879958752/)
- string, stack

---

## Problem Statement

<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>


---

## Solution

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
