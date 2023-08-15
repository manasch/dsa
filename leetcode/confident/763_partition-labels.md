[[763] - Partition Labels](https://leetcode.com/problems/partition-labels)

---

- Medium
- [Submission](https://leetcode.com/problems/partition-labels/submissions/1021955461/)
- hash-table, two-pointers, string, greedy

---

## Problem Statement

<p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in at most one part.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resultant string should be <code>s</code>.</p>

<p>Return <em>a list of integers representing the size of these parts</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababcbacadefegdehijhklij&quot;
<strong>Output:</strong> [9,7,8]
<strong>Explanation:</strong>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits s into less parts.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;eccbbbbdec&quot;
<strong>Output:</strong> [10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> res;
        vector<int> freq(26, 0);
        unordered_set<char> visited;
        int index;
        int n = s.size();

        for (char chr: s) {
            index = chr - 'a';
            ++freq[index];
        }

        int l = 0, r = 0;
        char chr;
        while (r < n) {
            chr = s[r];
            index = chr - 'a';
            visited.insert(chr);
            --freq[index];
            if (freq[index] == 0) {
                visited.erase(chr);
            }
            if (visited.empty()) {
                res.push_back(r - l + 1);
                l = r + 1;
            }
            ++r;
        }
        return res;
    }
};
```

---

## Notes

- Surprised that this actually worked.
- Perform first iteration to get the frequence of all characters. Have a window and keep a set for all the characters visited in that window and decrement the count in the frequence.
- When the frequence for that character hits 0, remove it from the set as its frequence is exhausted.
- Now if the visited set is empty, that means all the characters in that window are unique that window and won't appear after. Add the window size to the result array and repeat.
