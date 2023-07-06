[[424] - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-repeating-character-replacement/submissions/975462662/)
- hash-table, string, sliding-window

---

## Problem Statement

<p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.</p>

<p>Return <em>the length of the longest substring containing the same letter you can get after performing the above operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ABAB&quot;, k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two &#39;A&#39;s with two &#39;B&#39;s or vice versa.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;AABABBA&quot;, k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the one &#39;A&#39; in the middle with &#39;B&#39; and form &quot;AABBBBA&quot;.
The substring &quot;BBBB&quot; has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only uppercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0; int r = 0;
        int res = 0;
        int maxFreq = 0;
        vector<int> charCount(26);

        while (r < s.size()) {
            ++charCount[s[r] - 'A'];
            maxFreq = max(charCount[s[r] - 'A'], maxFreq);

            if ((r - l + 1 - maxFreq) > k) {
                --charCount[s[l] - 'A'];
                ++l;
            }
            res = max(res, r - l + 1);
            ++r;
        }

        return res;
    }
};
```

---

## Notes

- This was a little tricky to understand, but one key thing to learn is that, any hashmap, hashset that is used during a sliding window will only store information about whatever is in the window as of now, anything that leaves the window also gets deleted from the window. This has been the case in all the problems I've tackled so far.
- The trick to this problem lies in figuring out the character that occurs the maximum number of times in the current window.
- After figuring this out, we are required to find the number of characters that need to be replaced such that all the characters in the window are same, this can be done by subtracting the window size from the max and checking if this value is less than the `k` that is provided, if it can't then increament the left pointer.
