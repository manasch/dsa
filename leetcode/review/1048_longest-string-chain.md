[[1048] - Longest String Chain](https://leetcode.com/problems/longest-string-chain)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-string-chain/submissions/1057151571/)
- array, hash-table, two-pointers, string, dynamic-programming

---

## Problem Statement

<p>You are given an array of <code>words</code> where each word consists of lowercase English letters.</p>

<p><code>word<sub>A</sub></code> is a <strong>predecessor</strong> of <code>word<sub>B</sub></code> if and only if we can insert <strong>exactly one</strong> letter anywhere in <code>word<sub>A</sub></code> <strong>without changing the order of the other characters</strong> to make it equal to <code>word<sub>B</sub></code>.</p>

<ul>
	<li>For example, <code>&quot;abc&quot;</code> is a <strong>predecessor</strong> of <code>&quot;ab<u>a</u>c&quot;</code>, while <code>&quot;cba&quot;</code> is not a <strong>predecessor</strong> of <code>&quot;bcad&quot;</code>.</li>
</ul>

<p>A <strong>word chain</strong><em> </em>is a sequence of words <code>[word<sub>1</sub>, word<sub>2</sub>, ..., word<sub>k</sub>]</code> with <code>k &gt;= 1</code>, where <code>word<sub>1</sub></code> is a <strong>predecessor</strong> of <code>word<sub>2</sub></code>, <code>word<sub>2</sub></code> is a <strong>predecessor</strong> of <code>word<sub>3</sub></code>, and so on. A single word is trivially a <strong>word chain</strong> with <code>k == 1</code>.</p>

<p>Return <em>the <strong>length</strong> of the <strong>longest possible word chain</strong> with words chosen from the given list of </em><code>words</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]
<strong>Output:</strong> 4
<strong>Explanation</strong>: One of the longest word chains is [&quot;a&quot;,&quot;<u>b</u>a&quot;,&quot;b<u>d</u>a&quot;,&quot;bd<u>c</u>a&quot;].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;xbc&quot;,&quot;pcxbcf&quot;,&quot;xb&quot;,&quot;cxbc&quot;,&quot;pcxbc&quot;]
<strong>Output:</strong> 5
<strong>Explanation:</strong> All the words can be put in a word chain [&quot;xb&quot;, &quot;xb<u>c</u>&quot;, &quot;<u>c</u>xbc&quot;, &quot;<u>p</u>cxbc&quot;, &quot;pcxbc<u>f</u>&quot;].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abcd&quot;,&quot;dbqca&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The trivial word chain [&quot;abcd&quot;] is one of the longest word chains.
[&quot;abcd&quot;,&quot;dbqca&quot;] is not a valid word chain because the ordering of the letters is changed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code> only consists of lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        unordered_set<string> wordSet(words.begin(), words.end());
        unordered_map<string, int> dp;

        int res = 1;
        auto dfs = [&] (auto self, string word) {
            if (wordSet.find(word) == wordSet.end()) {
                return 0;
            }
            if (dp.find(word) != dp.end()) {
                return dp[word];
            }
            int temp = 1;
            int n = word.size();
            string nextWord;
            for (int i = 0; i < n; ++i) {
                nextWord = word.substr(0, i) + word.substr(i + 1);
                temp = max(temp, 1 + self(self, nextWord));
            }
            res = max(res, temp);
            return dp[word] = temp;
        };

        for (auto word: words) {
            dfs(dfs, word);
        }
        return res;
    }
};
```

---

## Notes

- This problem seems hard, but it's not that bad.
- The main concept from this is that the strings can be added to a set for constant time lookups.
- The dp is used to keep track of the string length till now in the top-down dfs.
- Each time, a character is removed and checked to see if it is in the set or the dp. Depending on which the return changes.

- Initially, I thought at each pos, add all characters and then decide, but this is clearly better.
