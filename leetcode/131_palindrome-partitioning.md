[[131] - Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning)

---

- Medium
- [Submission](https://leetcode.com/problems/palindrome-partitioning/submissions/992659747/)
- string, dynamic-programming, backtracking

---

## Problem Statement

<p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string"><strong>palindrome</strong></span>. Return <em>all possible palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    bool isPalindrome(string s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            ++l;
            --r;
        }
        return true;
    }

    void dfs(const string s, vector<string>& current, vector<vector<string>>& result, int index) {
        if (index >= s.size()) {
            result.push_back(current);
            return;
        }
        for (int i = index; i < s.size(); ++i) {
            if (isPalindrome(s, index, i)) {
                string c = s.substr(index, i - index + 1);
                current.push_back(c);
                dfs(s, current, result, i + 1);
                current.pop_back();
            }
        }
    }
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> current;
        dfs(s, current, result, 0);
        return result;
    }
};
```

---

## Notes

- Generate every possible partition and check if the set of partitions are all palindromes.
- `O(2^n)`
