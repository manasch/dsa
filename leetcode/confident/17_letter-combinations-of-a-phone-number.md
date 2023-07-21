[[17] - Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)

---

- Medium
- [Submission](https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/992672292/)
- hash-table, string, backtracking

---

## Problem Statement

<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png" style="width: 300px; height: 243px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;,&quot;ae&quot;,&quot;af&quot;,&quot;bd&quot;,&quot;be&quot;,&quot;bf&quot;,&quot;cd&quot;,&quot;ce&quot;,&quot;cf&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;&quot;
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;2&quot;
<strong>Output:</strong> [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>[&#39;2&#39;, &#39;9&#39;]</code>.</li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    void dfs(string digits, unordered_map<char, string>& phone, int index, string text, vector<string>& result) {
        if (index == digits.size()) {
            result.push_back((string) text);
            return;
        }
        string c = phone[digits[index]];
        for (int i = 0; i < c.size(); ++i) {
            text.push_back(c[i]);
            dfs(digits, phone, index + 1, text, result);
            text.pop_back();
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> phone = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        vector<string> result;
        if (digits.size() == 0) {
            return result;
        }
        string text = "";
        dfs(digits, phone, 0, text, result);
        return result;
    }
};
```

---

## Notes

- Create a simple map of the digits to the letters like the phonepad.
- Create every possible combination of strings that could be formed with the help of backtracking, once the characters is added and used, remove it after it has been used.
