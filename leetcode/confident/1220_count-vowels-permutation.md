[[1220] - Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation)

---

- Hard
- [Submission](https://leetcode.com/problems/count-vowels-permutation/submissions/1085843305/)
- [Submission](https://leetcode.com/problems/count-vowels-permutation/submissions/1085848382/)
- dynamic-programming

---

## Problem Statement

<p>Given an integer <code>n</code>, your task is to count how many strings of length <code>n</code> can be formed under the following rules:</p>

<ul>
	<li>Each character is a lower case vowel&nbsp;(<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, <code>&#39;u&#39;</code>)</li>
	<li>Each vowel&nbsp;<code>&#39;a&#39;</code> may only be followed by an <code>&#39;e&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;e&#39;</code> may only be followed by an <code>&#39;a&#39;</code>&nbsp;or an <code>&#39;i&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;i&#39;</code> <strong>may not</strong> be followed by another <code>&#39;i&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;o&#39;</code> may only be followed by an <code>&#39;i&#39;</code> or a&nbsp;<code>&#39;u&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;u&#39;</code> may only be followed by an <code>&#39;a&#39;.</code></li>
</ul>

<p>Since the answer&nbsp;may be too large,&nbsp;return it modulo <code>10^9 + 7.</code></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> All possible strings are: &quot;a&quot;, &quot;e&quot;, &quot;i&quot; , &quot;o&quot; and &quot;u&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> All possible strings are: &quot;ae&quot;, &quot;ea&quot;, &quot;ei&quot;, &quot;ia&quot;, &quot;ie&quot;, &quot;io&quot;, &quot;iu&quot;, &quot;oi&quot;, &quot;ou&quot; and &quot;ua&quot;.
</pre>

<p><strong class="example">Example 3:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 68</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10^4</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int countVowelPermutation(int n) {
        const int mod = 1e9 + 7;
        unordered_map<char, string> vowels = {
            {'a', "e"},
            {'e', "ai"},
            {'i', "aeou"},
            {'o', "iu"},
            {'u', "a"}
        };

        auto hash_pair = [] (pair<char, int> p) {
            return hash<char>()(p.first) ^ hash<int>()(p.second);
        };
        unordered_map<pair<char, int>, int, decltype(hash_pair)> dp;

        auto dfs = [&] (auto self, char c, int idx) {
            if (idx == n - 1) {
                return 1;
            }
            if (dp.find({c, idx}) != dp.end()) {
                return dp[{c, idx}];
            }
            int count = 0;
            for (auto nextChar: vowels[c]) {
                count = (count + self(self, nextChar, idx + 1)) % mod;
            }
            return dp[{c, idx}] = count;
        };

        int res = 0;
        for (auto& [k, _]: vowels) {
            res = (res + dfs(dfs, k, 0)) % mod;
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    int countVowelPermutation(int n) {
        const int mod = 1e9 + 7;

        long long a = 1, e = 1, i = 1, o = 1, u = 1;

        for (int k = 1; k < n; ++k) {
            long long a_next = e;
            long long e_next = (a + i) % mod;
            long long i_next = (a + e + o + u) % mod;
            long long o_next = (i + u) % mod;
            long long u_next = a;

            a = a_next;
            e = e_next;
            i = i_next;
            o = o_next;
            u = u_next;
        }

        return (a + e + i + o + u) % mod;
    }
};
```

---

## Notes

- Was able to do this on my own \o/.
- Basically, the repeated subproblem would be for a particular level and the character at that level.
- Apart from that, it's a normal top-down dfs problem. Most likely a better solution exists.


- Ofcourse, the actual optimized solution is so simple, well this is a bottom-up kind of approach maybe?
- Just simultaniously calculate starting from each vowel, and add the next vowel value to it.
