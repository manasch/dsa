[[10] - Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)

---

- Hard
- [Submission]( https://leetcode.com/problems/regular-expression-matching/submissions/1050276902/)
- string, dynamic-programming, recursion

---

## Problem Statement

<p>Given an input string <code>s</code>&nbsp;and a pattern <code>p</code>, implement regular expression matching with support for <code>&#39;.&#39;</code> and <code>&#39;*&#39;</code> where:</p>

<ul>
	<li><code>&#39;.&#39;</code> Matches any single character.</li>
	<li><code>&#39;*&#39;</code> Matches zero or more of the preceding element.</li>
</ul>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &#39;*&#39; means zero or more of the preceding element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;, p = &quot;.*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 20</code></li>
	<li><code>1 &lt;= p.length&nbsp;&lt;= 20</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>&#39;.&#39;</code>, and&nbsp;<code>&#39;*&#39;</code>.</li>
	<li>It is guaranteed for each appearance of the character <code>&#39;*&#39;</code>, there will be a previous valid character to match.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();
        map<pair<int, int>, bool> dp;
        auto dfs = [&] (auto self, int i, int j) {
            if (dp.find({i, j}) != dp.end()) {
                return dp[{i, j}];
            }
            if (i >= m && j >= n) {
                return true;
            }
            if (j >= n) {
                return false;
            }

            bool match = (i < m) && (s[i] == p[j] || p[j] == '.');
            if (j + 1 < n && p[j + 1] == '*') {
                bool dontInclude = self(self, i, j + 2);
                bool include = match && self(self, i + 1, j);
                return dp[{i,j}] = (dontInclude || include);
            }
            if (match) {
                return dp[{i, j}] = self(self, i + 1, j + 1);
            }
            return dp[{i, j}] = false;
        };

        return dfs(dfs, 0, 0);
    }
};
```

---

## Notes

- This was actually pretty doable, I believe I could have gotten this on my own with a little more thought, but basically this just regular string matching with regex for complexity.
- I was able to determine the values in the dp correctly being i and j that is the position in s and p respectively.
- But essentially, If the lookahead of a character is a `*`, it is either considered or not considered, and the total match is counted with the dfs.
- Otherwise, if it is a dot, it matches anything and hence can increment both i and j.
