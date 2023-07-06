[[3] - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/975322240/)
- hash-table, string, sliding-window

---

## Problem Statement

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0; int r = 0;
        int n = s.size();
        int ans = 0;
        unordered_set<char> charset;

        while (r < n) {
            while (charset.find(s[r]) != charset.end()) {
                charset.erase(s[l]);
                ++l;
            }
            charset.insert(s[r]);
            ans = max(ans, r - l + 1);
            ++r;
        }

        return ans;
    }
};
```

---

## Notes

- A bruteforce approach would be to check every single substring for each character and find the length. That would be `O(n^2)`. Instead can be done using two pointers and a sliding windows.
- The left pointer only updates when the right pointer sees something that is already in the set. The set is used to keep track of what all characters have been seen. The right pointer keeps updating normally until the end.
