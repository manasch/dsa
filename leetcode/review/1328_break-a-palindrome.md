[[1328] - Break a Palindrome](https://leetcode.com/problems/break-a-palindrome)

---

- Medium
- [Submission](https://leetcode.com/problems/break-a-palindrome/submissions/1100882480/)
- string, greedy

---

## Problem Statement

<p>Given a palindromic string of lowercase English letters <code>palindrome</code>, replace <strong>exactly one</strong> character with any lowercase English letter so that the resulting string is <strong>not</strong> a palindrome and that it is the <strong>lexicographically smallest</strong> one possible.</p>

<p>Return <em>the resulting string. If there is no way to replace a character to make it not a palindrome, return an <strong>empty string</strong>.</em></p>

<p>A string <code>a</code> is lexicographically smaller than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, <code>a</code> has a character strictly smaller than the corresponding character in <code>b</code>. For example, <code>&quot;abcc&quot;</code> is lexicographically smaller than <code>&quot;abcd&quot;</code> because the first position they differ is at the fourth character, and <code>&#39;c&#39;</code> is smaller than <code>&#39;d&#39;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> palindrome = &quot;abccba&quot;
<strong>Output:</strong> &quot;aaccba&quot;
<strong>Explanation:</strong> There are many ways to make &quot;abccba&quot; not a palindrome, such as &quot;<u>z</u>bccba&quot;, &quot;a<u>a</u>ccba&quot;, and &quot;ab<u>a</u>cba&quot;.
Of all the ways, &quot;aaccba&quot; is the lexicographically smallest.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> palindrome = &quot;a&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no way to replace a single character to make &quot;a&quot; not a palindrome, so return an empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= palindrome.length &lt;= 1000</code></li>
	<li><code>palindrome</code> consists of only lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.size();
        if (n <= 1) {
            return "";
        }
        int start = 0, end = n - 1;
        while (start < end) {
            if (palindrome[start] != 'a') {
                palindrome[start] = 'a';
                return palindrome;
            }
            ++start;
            --end;
        }
        palindrome[n - 1] = 'b';
        return palindrome;
    }
};
```

---

## Notes

- Basically, need to check for the first character that can be changed to 'a'.
- If none can be changed to 'a', then this is the edge case of all 'a's in which case just change the last character to a 'b'.
