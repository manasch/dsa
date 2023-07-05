[[105] - Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

---

- Medium
- [Submission](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/986894398/)
- array, hash-table, divide-and-conquer, tree, binary-tree

---

## Problem Statement

<p>Given two integer arrays <code>preorder</code> and <code>inorder</code> where <code>preorder</code> is the preorder traversal of a binary tree and <code>inorder</code> is the inorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code> and <code>inorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>inorder</code> also appears in <code>preorder</code>.</li>
	<li><code>preorder</code> is <strong>guaranteed</strong> to be the preorder traversal of the tree.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
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
// private:
//     unordered_map<int, int> inorderHash;

//     TreeNode* divide(int preindex, int beg, int end, vector<int>& preorder, vector<int>& inorder, int size) {

//         if (preindex >= size) {
//             return NULL;
//         }
//         int pivot = inorderHash[preorder[preindex]];

//         if (pivot < 0 || pivot >= size) {
//             return NULL;
//         }

//         if (pivot == beg && pivot == end) {
//             return new TreeNode(inorder[pivot]);
//         }

//         TreeNode* left = divide(preindex + 1, beg, pivot - 1, preorder, inorder, size);
//         TreeNode* right = divide(preindex + 1, pivot + 1, end, preorder, inorder, size);

//         return new TreeNode(inorder[pivot], left, right);
//     }

// public:
//     TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
//         int n = inorder.size();
//         for (int i = 0; i < inorder.size(); ++i) {
//             inorderHash[inorder[i]] = i;
//         }

//         TreeNode* root = divide(0, 0, n - 1, preorder, inorder, n);
//         return root;
//     }
private:
    unordered_map<int, int> h;
    TreeNode* divide(vector<int>& preorder, vector<int>& inorder, int& index, int beg, int end) {
        if (beg > end) {
            return NULL;
        }

        TreeNode *root = new TreeNode(preorder[index]);
        int pivot = h[preorder[index]];
        ++index;

        root->left = divide(preorder, inorder, index, beg, pivot - 1);
        root->right = divide(preorder, inorder, index, pivot + 1, end);

        return root;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); ++i) {
            h[inorder[i]] = i;
        }

        int index = 0;
        return divide(preorder, inorder, index, 0, inorder.size() - 1);
    }
};
```

---

## Notes

- The commented out code has my initial approach. It is very similar to the final one that is both use divide and conquer.
- The goal is to find the pivot which divides the left subtree and the right subtree, construct the tree bottom up.
- I used a hashmap to increase the speed of access of finding the pivot.
