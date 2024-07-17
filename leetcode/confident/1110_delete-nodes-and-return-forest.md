[[1110] - Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest)

---

- Medium
- [Submission](https://leetcode.com/problems/delete-nodes-and-return-forest/submissions/1323682000/)
- array, hash-table, tree, depth-first-search, binary-tree
- Contest: none

---

## Problem Statement

<p>Given the <code>root</code> of a binary tree, each node in the tree has a distinct value.</p>

<p>After deleting all nodes with a value in <code>to_delete</code>, we are left with a forest (a disjoint union of trees).</p>

<p>Return the roots of the trees in the remaining forest. You may return the result in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png" style="width: 237px; height: 150px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7], to_delete = [3,5]
<strong>Output:</strong> [[1,2,null,4],[6],[7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,4,null,3], to_delete = [3]
<strong>Output:</strong> [[1,2,4]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree is at most <code>1000</code>.</li>
	<li>Each node has a distinct value between <code>1</code> and <code>1000</code>.</li>
	<li><code>to_delete.length &lt;= 1000</code></li>
	<li><code>to_delete</code> contains distinct values between <code>1</code> and <code>1000</code>.</li>
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
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode *> forest;
        unordered_set<int> to_del(to_delete.begin(), to_delete.end());

        auto dfs = [&] (auto self, TreeNode *node) -> TreeNode* {
            if (node == nullptr) {
                return nullptr;
            }
            node->left = self(self, node->left);
            node->right = self(self, node->right);

            if (to_del.find(node->val) != to_del.end()) {
                if (node->left) {
                    forest.push_back(node->left);
                }
                if (node->right) {
                    forest.push_back(node->right);
                }
                return nullptr;
            }
            return node;
        };

        if (to_del.find(root->val) == to_del.end()) {
            forest.push_back(root);
        }
        dfs(dfs, root);
        return forest;
    }
};
```

---

## Notes

- Observations
	- If performing dfs traversal, have to add the roots of the forest from bottom-up
	- Add all the nodes to be deleted to a set for faster retrieval
- Perform a post-order traversal, if the current node is to be deleted, add it's left and right childs to the vector, if present, and return a nullptr back up to the parent.
