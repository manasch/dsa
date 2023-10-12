[[14] - Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

---

- Easy
- [Submission](https://leetcode.com/problems/longest-common-prefix/submissions/1073737957/)
- string, trie

---

## Problem Statement

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }
        int n = strs.size();
        sort(strs.begin(), strs.end());
        int res = 0;
        while (res < strs[0].size() && res < strs[n - 1].size() && strs[0][res] == strs[n - 1][res]) {
            ++res;
        }
        return strs[0].substr(0, res);
    }
};
```

---

## Notes

- Iterate through the sorted array of the strings for the first and last word, when they break, that's the longest common prefix.
