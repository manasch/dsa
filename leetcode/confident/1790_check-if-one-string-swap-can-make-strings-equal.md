[[1790] - Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal)

---

- Easy
- [Submission](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/submissions/1532058500)
- [Submission](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/submissions/1532069769/)
- hash-table, string, counting
- Contest: none

---

## Problem Statement

<p>You are given two strings <code>s1</code> and <code>s2</code> of equal length. A <strong>string swap</strong> is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.</p>

<p>Return <code>true</code> <em>if it is possible to make both strings equal by performing <strong>at most one string swap </strong>on <strong>exactly one</strong> of the strings. </em>Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;bank&quot;, s2 = &quot;kanb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> For example, swap the first character with the last character of s2 to make &quot;bank&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;attack&quot;, s2 = &quot;defend&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make them equal with one string swap.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;kelb&quot;, s2 = &quot;kelb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The two strings are already equal, so no string swap operation is required.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li><code>s1</code> and <code>s2</code> consist of only lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int n = s1.size();
        vector<int> f1(26, 0), f2(26, 0);
        int diff = 0;
        for (int i = 0; i < n; ++i) {
            if (s1[i] != s2[i]) {
                ++diff;
            }
            ++f1[s1[i] - 'a'];
            ++f2[s2[i] - 'a'];
        }

        for (int i = 0; i < 26; ++i) {
            if (f1[i] != f2[i]) {
                return false;
            }
        }
        return diff <= 2;
    }
};
```

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int n = s1.size();
        int idx1 = 0, idx2 = 0;
        int diff = 0;
        for (int i = 0; i < n; ++i) {
            if (s1[i] != s2[i]) {
                ++diff;
                if (diff > 2) {
                    return false;
                }
                else if (diff == 1) {
                    idx1 = i;
                }
                else {
                    idx2 = i;
                }
            }
        }

        return (s1[idx1] == s2[idx2] && s1[idx2] == s2[idx1]);
    }
};
```

---

## Notes

- keep a frequency count of each character occurence.
- if the count doesn't match, false.
- if it does and the number of times the characters mismatch when checking linearly is greater than 2, false.

- smarter approach is, return false early if the count is greater than 2, if not, just keep track of the indices of the 2 characters that are swapped, the characters at the opposite position should be the same.
- the only valid case is when there's only meant to be one swap, or two characters at the wrong place and the character at the wrong place matches the other character.
