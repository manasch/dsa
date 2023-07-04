[[102] - Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)

---

- Medium
- [Submission](https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/985509488/)
- tree, breadth-first-search, binary-tree

---

## Problem Statement

<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


---

## Solution

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;

        queue<TreeNode *> q;
        q.push(root);

        TreeNode *node;
        vector<int> temp;

        while (!q.empty()) {
            int len = q.size();
            while (len--) {
                node = q.front();
                q.pop();
                if (node) {
                    temp.push_back(node->val);
                    q.push(node->left);
                    q.push(node->right);
                }
            }
            if (!temp.empty())
                result.push_back(temp);
            temp.clear();
        }
        return result;
    }
};
```

---

## Notes

- This was just a simulation of BFS.
- Required to keep track of each level, can be done with the help of a count variable and when the q is empty.
