[[118] - Pascal's Triangle](https://leetcode.com/problems/pascals-triangle)

---

- Easy
- [Submission](https://leetcode.com/problems/pascals-triangle/submissions/1043713605)
- array, dynamic-programming

---

## Problem Statement

<p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        vector<int> temp;
        temp.push_back(1);
        res.push_back(temp);
        if (numRows == 1) {
            return res;
        }
        temp.push_back(1);
        res.push_back(temp);
        if (numRows == 2) {
            return res;
        }
        
        vector<int> newTemp;
        for (int i = 2; i < numRows; ++i) {
            newTemp.clear();
            newTemp.push_back(1);
            for (int j = 0; j + 1 < temp.size(); ++j) {
                newTemp.push_back(temp[j] + temp[j + 1]);
            }
            newTemp.push_back(1);
            res.push_back(newTemp);
            temp = newTemp;
        }
        return res;
    }
};
```

---

## Notes

- Keep a temporary array which holds the previous layer's value and use that for the next layer.
