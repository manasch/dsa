[[3039] - Apply Operations to Make String Empty](https://leetcode.com/problems/apply-operations-to-make-string-empty)

---

- Medium
- [Submission](https://leetcode.com/problems/apply-operations-to-make-string-empty/submissions/1177899517/)
- [Submission](https://leetcode.com/problems/apply-operations-to-make-string-empty/submissions/1178047675/)
- array, hash-table, sorting, counting
- Contest: [biweekly-contest-124](https://leetcode.com/contest/biweekly-contest-124)

---

## Problem Statement

<p>You are given a string <code>s</code>.</p>

<p>Consider performing the following operation until <code>s</code> becomes <strong>empty</strong>:</p>

<ul>
	<li>For <strong>every</strong> alphabet character from <code>&#39;a&#39;</code> to <code>&#39;z&#39;</code>, remove the <strong>first</strong> occurrence of that character in <code>s</code> (if it exists).</li>
</ul>

<p>For example, let initially <code>s = &quot;aabcbbca&quot;</code>. We do the following operations:</p>

<ul>
	<li>Remove the underlined characters <code>s = &quot;<u><strong>a</strong></u>a<strong><u>bc</u></strong>bbca&quot;</code>. The resulting string is <code>s = &quot;abbca&quot;</code>.</li>
	<li>Remove the underlined characters <code>s = &quot;<u><strong>ab</strong></u>b<u><strong>c</strong></u>a&quot;</code>. The resulting string is <code>s = &quot;ba&quot;</code>.</li>
	<li>Remove the underlined characters <code>s = &quot;<u><strong>ba</strong></u>&quot;</code>. The resulting string is <code>s = &quot;&quot;</code>.</li>
</ul>

<p>Return <em>the value of the string </em><code>s</code><em> right <strong>before</strong> applying the <strong>last</strong> operation</em>. In the example above, answer is <code>&quot;ba&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabcbbca&quot;
<strong>Output:</strong> &quot;ba&quot;
<strong>Explanation:</strong> Explained in the statement.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;
<strong>Output:</strong> &quot;abcd&quot;
<strong>Explanation:</strong> We do the following operation:
- Remove the underlined characters s = &quot;<u><strong>abcd</strong></u>&quot;. The resulting string is s = &quot;&quot;.
The string just before the last operation is &quot;abcd&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


---

## Solution

### Contest Submission

```cpp
class Solution {
public:
    string lastNonEmptyString(string s) {
        vector<int> freq(26, 0), last(26, -1);

        int idx = 0;
        for (int i = 0; i < s.size(); ++i) {
            idx = s[i] - 'a';
            ++freq[idx];
            last[idx] = i;
        }
        
        string res = "";
        int max_count = *max_element(freq.begin(), freq.end());
        
        for (int i = 0; i < 26; ++i) {
            if (max_count == freq[i]) {
                res += char('a' + i);
            }
        }
        
        sort(res.begin(), res.end(), [&](const char &ch1, const char &ch2) {
            return last[ch1 - 'a'] < last[ch2 - 'a'];
        });
        
        return res;
    }
};
```

### Later Submission

```cpp
class Solution {
public:
    string lastNonEmptyString(string s) {
        vector<int> freq(26, 0), last(26, -1);

        int idx = 0;
        for (int i = 0; i < s.size(); ++i) {
            idx = s[i] - 'a';
            ++freq[idx];
            last[idx] = i;
        }
        
        string res = "";
        int max_count = *max_element(freq.begin(), freq.end());

        for (int i = 0; i < s.size(); ++i) {
            int idx = s[i] - 'a';
            if (max_count == freq[idx] && last[idx] == i) {
                res += s[i];
            }
        }
        return res;
    }
};
```

---

## Notes

- Just store the frequency and the last occurance of the characters, and remove the characters unless they aren't of mode occurance and not the last occurance.
- Initially tried to sort the array based on last occurance, but that isn't required. `O(nlogn) -> O(n)`
