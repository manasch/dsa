[[91] - Decode Ways](https://leetcode.com/problems/decode-ways)

---

- Medium
- [Submission](https://leetcode.com/problems/decode-ways/submissions/1005300309/)
- string, dynamic-programming

---

## Problem Statement

<p>A message containing letters from <code>A-Z</code> can be <strong>encoded</strong> into numbers using the following mapping:</p>

<pre>
&#39;A&#39; -&gt; &quot;1&quot;
&#39;B&#39; -&gt; &quot;2&quot;
...
&#39;Z&#39; -&gt; &quot;26&quot;
</pre>

<p>To <strong>decode</strong> an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, <code>&quot;11106&quot;</code> can be mapped into:</p>

<ul>
	<li><code>&quot;AAJF&quot;</code> with the grouping <code>(1 1 10 6)</code></li>
	<li><code>&quot;KJF&quot;</code> with the grouping <code>(11 10 6)</code></li>
</ul>

<p>Note that the grouping <code>(1 11 06)</code> is invalid because <code>&quot;06&quot;</code> cannot be mapped into <code>&#39;F&#39;</code> since <code>&quot;6&quot;</code> is different from <code>&quot;06&quot;</code>.</p>

<p>Given a string <code>s</code> containing only digits, return <em>the <strong>number</strong> of ways to <strong>decode</strong> it</em>.</p>

<p>The test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;12&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> &quot;12&quot; could be decoded as &quot;AB&quot; (1 2) or &quot;L&quot; (12).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;226&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> &quot;226&quot; could be decoded as &quot;BZ&quot; (2 26), &quot;VF&quot; (22 6), or &quot;BBF&quot; (2 2 6).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;06&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;06&quot; cannot be mapped to &quot;F&quot; because of the leading zero (&quot;6&quot; is different from &quot;06&quot;).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> contains only digits and may contain leading zero(s).</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int numDecodings(string s) {
        unordered_map<int, int> dp;
        dp[s.size()] = 1;
        return dfs(s, 0, dp);
    }
private:
    int dfs(string& s, int idx, unordered_map<int, int>& dp) {
        if (s[idx] == '0') {
            return 0;
        }
        if (dp.find(idx) != dp.end()) {
            return dp[idx];
        }

        int res = dfs(s, idx + 1, dp);
        if (idx + 1 < s.size() && (s[idx] == '1' || (s[idx] == '2' && s[idx + 1] - '0' <= 6))) {
            res += dfs(s, idx + 2, dp);
        }
        dp[idx] = res;
        return res;
    }
};
```

---

## Notes

- Slowly somewhat understanding it, break the problem into subproblems, I was able to draw the decision tree, but not generalize it into subproblems, it's rather simple but easy to miss.
- if `111065` is the string then the subproblem would be  `11065` or `1065`. But it can be noticed that the subproblem for `11065` would be `1065` and `065`.
- Hence, by storing the number of possible ways in a data structure `dp`, it can be reused later.
