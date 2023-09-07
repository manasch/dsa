[[72] - Edit Distance](https://leetcode.com/problems/edit-distance)

---

- Medium
- [Submission](https://leetcode.com/problems/edit-distance/submissions/1042802177/)
- string, dynamic-programming

---

## Problem Statement

<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i <= m; ++i) {
            dp[i][n] = m - i;
        }

        for (int j = 0; j <= n; ++j) {
            dp[m][j] = n - j;
        }

        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (word1[i] == word2[j]) {
                    dp[i][j] = dp[i + 1][j + 1];
                }
                else {
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], min(dp[i + 1][j], dp[i][j + 1]));
                }
            }
        }
        return dp[0][0];
    }
};
```

---

## Notes

- This is very similar to `LC#1143 - LCS`.
- The base cases would be, when one of the words are empty while the other isn't, the minimum operations would be the length of the non-tempy string.
- If the characters at the positions match, then it takes no operations and the pointer moves for both word1 and word2. If the characters mismatch, then we can either insert, delete or swap the characters.
- We have to try all the possible ways to see which is the least.
	- Insert: word1 doesn't move, but word2 pointer moves as the characters have been matched due to insertion.
	- Delete: word1 pointer moves whereas word2 pointer does not, hoping that remaining of word1 will match with word2.
	- Replace: Both the pointers would move making it similar to the case where both matched but at the cost of one operation.
- In this manner it is very similar to LCS.
