[[49] - Group Anagrams](https://leetcode.com/problems/group-anagrams)

---

- Medium
- [Submission](https://leetcode.com/problems/group-anagrams/submissions/866880192/)
- array, hash-table, string, sorting

---

## Problem Statement

<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> ans;
        string original;

        for (auto x: strs) {
            original = x;
            sort(x.begin(), x.end());
            hashmap[x].push_back(original);
        }

        for (auto [_, x]: hashmap) {
            ans.push_back(x);
        }
        
        return ans;
    }
};
```

---

## Notes

- Create a hashmap of the sorted string mapped to a vector of strings, this way after sorting, just append the string to the vector of strings whose sorted string matches the key. This is `O(m.nlogn)`, pretty slow.
- This can be made faster by exploiting the fact that only lowercase alphabets will be used, and hence just count the occurence of what all occurs how many times and use that as the key in the hashmap. `O(m.n.26) = O(m.n)` Uses extra space 26 everytime. Create a string of what all occurs how many times, represent it in binary and keep that as the key in the hashmap.
