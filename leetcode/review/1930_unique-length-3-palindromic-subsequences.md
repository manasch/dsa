[[1930] - Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

---

- Medium
- [Submission](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/submissions/1098447213/)
- hash-table, string, prefix-sum

---

## Problem Statement

<p>Given a string <code>s</code>, return <em>the number of <strong>unique palindromes of length three</strong> that are a <strong>subsequence</strong> of </em><code>s</code>.</p>

<p>Note that even if there are multiple ways to obtain the same subsequence, it is still only counted <strong>once</strong>.</p>

<p>A <strong>palindrome</strong> is a string that reads the same forwards and backwards.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabca&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 3 palindromic subsequences of length 3 are:
- &quot;aba&quot; (subsequence of &quot;<u>a</u>a<u>b</u>c<u>a</u>&quot;)
- &quot;aaa&quot; (subsequence of &quot;<u>aa</u>bc<u>a</u>&quot;)
- &quot;aca&quot; (subsequence of &quot;<u>a</u>ab<u>ca</u>&quot;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;adc&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no palindromic subsequences of length 3 in &quot;adc&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbcbaba&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4 palindromic subsequences of length 3 are:
- &quot;bbb&quot; (subsequence of &quot;<u>bb</u>c<u>b</u>aba&quot;)
- &quot;bcb&quot; (subsequence of &quot;<u>b</u>b<u>cb</u>aba&quot;)
- &quot;bab&quot; (subsequence of &quot;<u>b</u>bcb<u>ab</u>a&quot;)
- &quot;aba&quot; (subsequence of &quot;bbcb<u>aba</u>&quot;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<char> letters;
        vector<int> first(26, -1);
        vector<int> last(26, -1);
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            letters.insert(c);
            if (first[c - 'a'] == -1) {
                first[c - 'a'] = i;
            }
            last[c - 'a'] = i;
        }

        int res = 0;
        unordered_set<char> middle;
        for (auto& letter: letters) {
            int i = first[letter - 'a'];
            int j = last[letter - 'a'];

            middle.clear();
            for (int k = i + 1; k < j; ++k) {
                middle.insert(s[k]);
            }
            res += middle.size();
        }
        return res;
    }
};
```

---

## Notes

- Since it's a palindrome of just length 3, the first and the last character have to be the same.
- Keeping this in mind, one can find the first and last occurance of all the characters in the string and all the unique characters that come in between these two positions add up to the result.
