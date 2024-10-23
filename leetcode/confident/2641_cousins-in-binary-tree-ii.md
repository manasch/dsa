[[2641] - Cousins in Binary Tree II](https://leetcode.com/problems/cousins-in-binary-tree-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/cousins-in-binary-tree-ii/submissions/1431385172/)
- [Submission](https://leetcode.com/problems/cousins-in-binary-tree-ii/submissions/1431391512/)
- hash-table, tree, depth-first-search, breadth-first-search, binary-tree
- Contest: none

---

## Problem Statement

<p>Given the <code>root</code> of a binary tree, replace the value of each node in the tree with the <strong>sum of all its cousins&#39; values</strong>.</p>

<p>Two nodes of a binary tree are <strong>cousins</strong> if they have the same depth with different parents.</p>

<p>Return <em>the </em><code>root</code><em> of the modified tree</em>.</p>

<p><strong>Note</strong> that the depth of a node is the number of edges in the path from the root node to it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/example11.png" style="width: 571px; height: 151px;" />
<pre>
<strong>Input:</strong> root = [5,4,9,1,10,null,7]
<strong>Output:</strong> [0,0,0,7,7,null,11]
<strong>Explanation:</strong> The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/diagram33.png" style="width: 481px; height: 91px;" />
<pre>
<strong>Input:</strong> root = [3,1,2]
<strong>Output:</strong> [0,0,0]
<strong>Explanation:</strong> The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
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
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (!root) {
            return nullptr;
        }

        queue<long long> sums;
        queue<TreeNode *> q;
        q.push(root);

        while (!q.empty()) {
            int t = q.size();
            long long s = 0;
            while (t--) {
                auto p = q.front();
                q.pop();

                s += p->val;
                if (p->right) q.push(p->right);
                if (p->left) q.push(p->left);
            }
            sums.push(s);
        }
        sums.pop();
        q.push(root);

        while (!q.empty()) {
            int t = q.size();
            long long s = sums.front();
            while (t--) {
                auto p = q.front();
                q.pop();

                int cs = 0;
                if (p->right) {
                    cs += p->right->val;
                    q.push(p->right);
                }
                if (p->left) {
                    cs += p->left->val;
                    q.push(p->left);
                }

                if (p->right) p->right->val = s - cs;
                if (p->left) p->left->val = s - cs;
            }
            sums.pop();
        }
        root->val = 0;
        return root;
    }
};
```

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
    TreeNode* replaceValueInTree(TreeNode* root) {
        int rowSum = root->val;
        queue<TreeNode *> q;
        q.push(root);

        while (!q.empty()) {
            int t = q.size();
            int nextSum = 0;
            while (t--) {
                auto p = q.front();
                q.pop();
                p->val = rowSum - p->val;

                int siblingSum = (p->right ? p->right->val : 0) + (p->left ? p->left->val : 0);

                if (p->left) {
                    nextSum += p->left->val;
                    p->left->val = siblingSum;
                    q.push(p->left);
                }
                if (p->right) {
                    nextSum += p->right->val;
                    p->right->val = siblingSum;
                    q.push(p->right);
                }
            }
            rowSum = nextSum;
        }   
        return root;
    }
};
```

---

## Notes

- The first solution is what came to me intuitively, for each node, we need its rowsum, so I perform one pass of bfs to store the row sum and in the next pass, I set that node's value with the difference of the rowsum and the sibling sum.

- The second solution is more clever, we don't need all the row sums, just that particular rowsum, so when traversing, if we have the rowsum already and the current node is set to the sibling sum, we can just set that node's value as the difference of the row sum and that sibling sum.
- This can be achieved by initially having a variable that stores the root's value, and subsequently at each level, calculate the children's sibling sum and set it as that, such that in the next level, you can directly subtract the rowsum with that node's value.
