[[5] - Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-palindromic-substring/submissions/1004796148/)
- string, dynamic-programming

---

## Problem Statement

<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int x = 0;
        int y = 0;
        int len = 0;

        int l, r;
        for (int i = 0; i < s.size(); ++i) {
            l = i; r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > len) {
                    len = r - l + 1;
                    x = l;
                    y = r;
                }
                --l; ++r;
            }

            l = i; r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > len) {
                    len = r - l + 1;
                    x = l;
                    y = r;
                }
                --l; ++r;
            }
        }
        return s.substr(x, y - x + 1);
    }
};
```

---

## Notes

- Cracked my head for a little bit but to no avail.
- Implemented the bruteforce approach but that was timing out. `O(n^3)`.
- A faster way would be to think of each character in the string as the centre of a palindrom and expand outwards to see if a bigger palindrome can be formed.
- Though this is not an actual dp solution.
