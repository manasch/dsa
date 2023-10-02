[[557] - Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii)

---

- Easy
- [Submission](https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/1064068052)
- two-pointers, string

---

## Problem Statement

<p>Given a string <code>s</code>, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "Let's take LeetCode contest"
<strong>Output:</strong> "s'teL ekat edoCteeL tsetnoc"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "God Ding"
<strong>Output:</strong> "doG gniD"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> contains printable <strong>ASCII</strong> characters.</li>
	<li><code>s</code> does not contain any leading or trailing spaces.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
	<li>All the words in <code>s</code> are separated by a single space.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    string reverseWords(string s) {
        string res = "";
        string word = "";
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ' ') {
                res.insert(res.end(), word.rbegin(), word.rend());
                res += " ";
                word = "";
            }
            else {
                word.push_back(s[i]);
            }
        }
        res.insert(res.end(), word.rbegin(), word.rend());
        return res;
    }
};
```

---

## Notes

- Word break at space or the end.
- True essence would be to not use any helper functions and use double pointers to reverse a word by swapping chars.
