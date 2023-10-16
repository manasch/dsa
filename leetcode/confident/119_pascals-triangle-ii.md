[[119] - Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii)

---

- Easy
- [Submission](https://leetcode.com/problems/pascals-triangle-ii/submissions/1076378649/)
- array, dynamic-programming

---

## Problem Statement

<p>Given an integer <code>rowIndex</code>, return the <code>rowIndex<sup>th</sup></code> (<strong>0-indexed</strong>) row of the <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rowIndex = 3
<strong>Output:</strong> [1,3,3,1]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rowIndex = 0
<strong>Output:</strong> [1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rowIndex = 1
<strong>Output:</strong> [1,1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= rowIndex &lt;= 33</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you optimize your algorithm to use only <code>O(rowIndex)</code> extra space?</p>


---

## Solution

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) {
            return {1};
        }
        if (rowIndex == 1) {
            return {1, 1};
        }
        vector<int> prev = {1, 1};
        vector<int> curr;
        for (int i = 2; i <= rowIndex; ++i) {
            curr.clear();
            curr.push_back(1);
            for (int j = 1; j < prev.size(); ++j) {
                curr.push_back(prev[j] + prev[j - 1]);
            }
            curr.push_back(1);
            prev = curr;
        }
        return curr;
    }
};
```

---

## Notes

- Similar to pascals triangle i, just keep track of the previous row to generate the current row. Break from the loop when the iterator reaches the required row index.
