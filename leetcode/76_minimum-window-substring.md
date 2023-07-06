[[76] - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)

---

- Hard
- [Submission](https://leetcode.com/problems/minimum-window-substring/submissions/977038418/)
- hash-table, string, sliding-window

---

## Problem Statement

<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ADOBECODEBANC&quot;, t = &quot;ABC&quot;
<strong>Output:</strong> &quot;BANC&quot;
<strong>Explanation:</strong> The minimum window substring &quot;BANC&quot; includes &#39;A&#39;, &#39;B&#39;, and &#39;C&#39; from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;aa&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> Both &#39;a&#39;s from t must be included in the window.
Since the largest window of s only has one &#39;a&#39;, return empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?</p>


---

## Solution

```cpp
class Solution {
private:
    // int getIndex(char c) {
    //     if (c >= 'A' && c <= 'Z') {
    //         return c - 'A';
    //     }
    //     else {
    //         return c - 'a' + 26;
    //     }
    // }
public:
    string minWindow(string s, string t) {
        int m = s.size();
        int n = t.size();
        pair<int, int> ans(-1, -1);
        int minWindowSize = INT_MAX;

        if (n > m) return "";

        unordered_map<char, int> sCount;
        unordered_map<char, int> tCount;

        for (char c: t) {
            ++tCount[c];
        }

        int l = 0; int r = 0;
        int currentMin;
        int need = 0;
        int req = tCount.size();
        while (r < m) {
            ++sCount[s[r]];
            if (tCount[s[r]] > 0 && sCount[s[r]] == tCount[s[r]]) {
                ++need;
            }

            while (need == req) {
                currentMin = r - l + 1;
                minWindowSize = min(minWindowSize, currentMin);
                if (currentMin == minWindowSize) {
                    ans.first = l;
                    ans.second = r - l + 1;
                }

                --sCount[s[l]];
                if (tCount[s[l]] > 0 && sCount[s[l]] < tCount[s[l]]) {
                    --need;
                }
                ++l;
            }
            ++r;
        }
        
        if (ans.first != -1) {
            return s.substr(ans.first, ans.second);
        }
        return "";
    }
};
```

---

## Notes

- Did this after `LC#576` and it helped, made this problem way easier.
- The window size changes here while the characters in the window are checked to see if they are enough or not.
- The right pointer keeps moving and stops only when there are enough characters and the left pointer starts moving until the number of characters are not enough.
- A typical sliding window problem which results in time complexity of `O(m + n)`.
