[[1405] - Longest Happy String](https://leetcode.com/problems/longest-happy-string)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-happy-string/submissions/1424514948/)
- string, greedy, heap-priority-queue
- Contest: none

---

## Problem Statement

<p>A string <code>s</code> is called <strong>happy</strong> if it satisfies the following conditions:</p>

<ul>
	<li><code>s</code> only contains the letters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
	<li><code>s</code> does not contain any of <code>&quot;aaa&quot;</code>, <code>&quot;bbb&quot;</code>, or <code>&quot;ccc&quot;</code> as a substring.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>a</code> occurrences of the letter <code>&#39;a&#39;</code>.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>b</code> occurrences of the letter <code>&#39;b&#39;</code>.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>c</code> occurrences of the letter <code>&#39;c&#39;</code>.</li>
</ul>

<p>Given three integers <code>a</code>, <code>b</code>, and <code>c</code>, return <em>the <strong>longest possible happy </strong>string</em>. If there are multiple longest happy strings, return <em>any of them</em>. If there is no such string, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 1, b = 1, c = 7
<strong>Output:</strong> &quot;ccaccbcc&quot;
<strong>Explanation:</strong> &quot;ccbccacc&quot; would also be a correct answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 7, b = 1, c = 0
<strong>Output:</strong> &quot;aabaa&quot;
<strong>Explanation:</strong> It is the only correct answer in this case.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= a, b, c &lt;= 100</code></li>
	<li><code>a + b + c &gt; 0</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int, char>> pq;
        if (a > 0) pq.push({a, 'a'});
        if (b > 0) pq.push({b, 'b'});
        if (c > 0) pq.push({c, 'c'});

        string s = "";
        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop();
            int c = p.first;
            char ch = p.second;

            if (s.size() >= 2 && s[s.size() - 1] == ch && s[s.size() - 2] == ch) {
                if (pq.empty()) {
                    break;
                }

                auto temp = pq.top();
                pq.pop();
                s += temp.second;
                if (temp.first > 1) {
                    pq.push({temp.first - 1, temp.second});
                }
            }
            else {
                --c;
                s += ch;
            }

            if (c > 0) {
                pq.push({c, ch});
            }
        }
        return s;
    }
};
```

---

## Notes

- It is always optimum to take the largest occuring one first, and when the streak of same characters reached 3, we don't considre it.
- Can use a max-heap to keep track of the characters left to use.
- If the streak hits 3, need to check the 2nd one in the heap and perform the same operations.
