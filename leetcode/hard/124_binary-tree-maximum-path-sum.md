[[124] - Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)

---

- Hard
- [Submission](https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/987703851/)
- dynamic-programming, tree, depth-first-search, binary-tree

---

## Problem Statement

<p>A <strong>path</strong> in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence <strong>at most once</strong>. Note that the path does not need to pass through the root.</p>

<p>The <strong>path sum</strong> of a path is the sum of the node&#39;s values in the path.</p>

<p>Given the <code>root</code> of a binary tree, return <em>the maximum <strong>path sum</strong> of any <strong>non-empty</strong> path</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The optimal path is 2 -&gt; 1 -&gt; 3 with a path sum of 2 + 1 + 3 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" />
<pre>
<strong>Input:</strong> root = [-10,9,20,null,null,15,7]
<strong>Output:</strong> 42
<strong>Explanation:</strong> The optimal path is 15 -&gt; 20 -&gt; 7 with a path sum of 15 + 20 + 7 = 42.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
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
private:
    int result = INT_MIN;
    int helper(TreeNode* node) {
        if (!node) {
            return 0;
        }

        int leftMax = helper(node->left);
        int rightMax = helper(node->right);
        leftMax = max(leftMax, 0);
        rightMax = max(rightMax, 0);

        result = max(result, node->val + leftMax + rightMax);
        return max(node->val + leftMax, node->val + rightMax);
    }
public:
    int maxPathSum(TreeNode* root) {
        return max(result, helper(root));
    }
};
```

---

## Notes

- The problem is actually pretty easy, at each node we decide between splitting at that point or not splitting.
- In the case of splitting, it is required to compute the path sum including itself + it's left and right max's.
- If not splitting then it can only choose one path, hence it returns either itself with the max of left or right.
