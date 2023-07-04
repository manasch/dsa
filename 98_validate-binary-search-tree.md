[[98] - Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)

---

- Medium
- [Submission](https://leetcode.com/problems/validate-binary-search-tree/submissions/986106761/)
- tree, depth-first-search, binary-search-tree, binary-tree

---

## Problem Statement

<p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul>
	<li>The left <span data-keyword="subtree">subtree</span> of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" />
<pre>
<strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node&#39;s value is 5 but its right child&#39;s value is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
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
private:
    bool result = true;
    TreeNode* prev = NULL;
public:
    void checkValidBST(TreeNode *node) {
        if (!node) {
            return;
        }

        checkValidBST(node->left);
        if (prev) {
            if (node->val <= prev->val) {
                result = false;
            }
        }
        prev = node;
        checkValidBST(node->right);
    }

    bool isValidBST(TreeNode* root) {
        checkValidBST(root);
        return result;
    }
};
```

---

## Notes

- A basic fact about BST is that when traversing it in inorder the elements should be in a monotonically increasing order.
- Hence, keeping track of the previous node visited and comparing it with the current can decide if the tree is indeed a BST or not.
