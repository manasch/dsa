[[1980] - Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string)

---

- Medium
- [Submission](https://leetcode.com/problems/find-unique-binary-string/submissions/1100137851)
- [Submission](https://leetcode.com/problems/find-unique-binary-string/submissions/1100136051)
- array, string, backtracking

---

## Problem Statement

<p>Given an array of strings <code>nums</code> containing <code>n</code> <strong>unique</strong> binary strings each of length <code>n</code>, return <em>a binary string of length </em><code>n</code><em> that <strong>does not appear</strong> in </em><code>nums</code><em>. If there are multiple answers, you may return <strong>any</strong> of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;01&quot;,&quot;10&quot;]
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> &quot;11&quot; does not appear in nums. &quot;00&quot; would also be correct.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;00&quot;,&quot;01&quot;]
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> &quot;11&quot; does not appear in nums. &quot;10&quot; would also be correct.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;111&quot;,&quot;011&quot;,&quot;001&quot;]
<strong>Output:</strong> &quot;101&quot;
<strong>Explanation:</strong> &quot;101&quot; does not appear in nums. &quot;000&quot;, &quot;010&quot;, &quot;100&quot;, and &quot;110&quot; would also be correct.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 16</code></li>
	<li><code>nums[i].length == n</code></li>
	<li><code>nums[i] </code>is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li>All the strings of <code>nums</code> are <strong>unique</strong>.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string res = "";

        int n = nums.size();
        int idx = 0;

        for (string num: nums) {
            res += num[idx] == '0' ? '1' : '0';
            ++idx;
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<string> bins(nums.begin(), nums.end());
        int n = nums.size();

        auto dfs = [&] (auto self, string curr) -> string {
            if (curr.size() == n) {
                if (bins.find(curr) == bins.end()) {
                    return curr;
                }
                return "";
            }
            string currZero = self(self, curr + "0");
            if (currZero.size() > 0) {
                return currZero;
            }
            return self(self, curr + "1");
        };

        return dfs(dfs, "");
    }
};
```

---

## Notes

- The first method I remembered from some video where you can always generate a new decimal value if you take some other number apart from what's there at that position.

- Second is just bruteforce backtracking.
