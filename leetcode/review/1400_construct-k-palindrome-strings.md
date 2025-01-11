[[1400] - Construct K Palindrome Strings](https://leetcode.com/problems/construct-k-palindrome-strings)

---

- Medium
- [Submission](https://leetcode.com/problems/construct-k-palindrome-strings/submissions/1505311366/)
- hash-table, string, greedy, counting
- Contest: none

---

## Problem Statement

<p>Given a string <code>s</code> and an integer <code>k</code>, return <code>true</code> <em>if you can use all the characters in </em><code>s</code><em> to construct </em><code>k</code><em> palindrome strings or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;annabelle&quot;, k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> You can construct two palindromes using all characters in s.
Some possible constructions &quot;anna&quot; + &quot;elble&quot;, &quot;anbna&quot; + &quot;elle&quot;, &quot;anellena&quot; + &quot;b&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to construct 3 palindromes using all the characters of s.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;true&quot;, k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> The only possible solution is to put each character in a separate string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    bool canConstruct(string s, int k) {
        vector<int> count(26, 0);
        if (s.size() < k) {
            return false;
        }
        for (char c: s) {
            ++count[c - 'a'];
        }

        int oddCount = 0;
        for (int i: count) {
            oddCount += (i % 2);
        }

        if (oddCount > k) {
            return false;
        }
        return true;
    }
};
```

---

## Notes

- Basic concept of a palindrome is that, the number of characters in it should be the same in case of an even palindrome, for an odd, there's an extra character (or set of same characters).

- If the oddCount of any character exceeds the `k`, then the minimum number of palindromes that can be formed is `k` at the least, as these have to be part of atleast `k` different palindromes.

- Using this, we can determine, depending on the count of oddCount, if the palindromes can be formed or not.
