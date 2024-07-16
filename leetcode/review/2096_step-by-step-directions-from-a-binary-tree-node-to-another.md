[[2096] - Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another)

---

- Medium
- [Submission](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/)
- string, tree, depth-first-search, binary-tree
- Contest: none

---

## Problem Statement

<p>You are given the <code>root</code> of a <strong>binary tree</strong> with <code>n</code> nodes. Each node is uniquely assigned a value from <code>1</code> to <code>n</code>. You are also given an integer <code>startValue</code> representing the value of the start node <code>s</code>, and a different integer <code>destValue</code> representing the value of the destination node <code>t</code>.</p>

<p>Find the <strong>shortest path</strong> starting from node <code>s</code> and ending at node <code>t</code>. Generate step-by-step directions of such path as a string consisting of only the <strong>uppercase</strong> letters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;U&#39;</code>. Each letter indicates a specific direction:</p>

<ul>
	<li><code>&#39;L&#39;</code> means to go from a node to its <strong>left child</strong> node.</li>
	<li><code>&#39;R&#39;</code> means to go from a node to its <strong>right child</strong> node.</li>
	<li><code>&#39;U&#39;</code> means to go from a node to its <strong>parent</strong> node.</li>
</ul>

<p>Return <em>the step-by-step directions of the <strong>shortest path</strong> from node </em><code>s</code><em> to node</em> <code>t</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/15/eg1.png" style="width: 214px; height: 163px;" />
<pre>
<strong>Input:</strong> root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
<strong>Output:</strong> &quot;UURL&quot;
<strong>Explanation:</strong> The shortest path is: 3 &rarr; 1 &rarr; 5 &rarr; 2 &rarr; 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/15/eg2.png" style="width: 74px; height: 102px;" />
<pre>
<strong>Input:</strong> root = [2,1], startValue = 2, destValue = 1
<strong>Output:</strong> &quot;L&quot;
<strong>Explanation:</strong> The shortest path is: 2 &rarr; 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= Node.val &lt;= n</code></li>
	<li>All the values in the tree are <strong>unique</strong>.</li>
	<li><code>1 &lt;= startValue, destValue &lt;= n</code></li>
	<li><code>startValue != destValue</code></li>
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
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string path1 = "";
        string path2 = "";

        findPath(root, startValue, path1);
        findPath(root, destValue, path2);

        int idx = 0;
        while (idx < path1.size() && idx < path2.size() && path1[idx] == path2[idx]) {
            ++idx;
        }

        string directions = string(path1.size() - idx, 'U') + path2.substr(idx);
        return directions;
    }

    bool findPath(TreeNode *node, int value, string& path) {
        if (node == nullptr) {
            return false;
        }
        if (node->val == value) {
            return true;
        }
        path.push_back('L');
        if (findPath(node->left, value, path)) {
            return true;
        }
        path.pop_back();

        path.push_back('R');
        if (findPath(node->right, value, path)) {
            return true;
        }
        path.pop_back();
        
        return false;
    }
};
```

---

## Notes

- I initially over-complicated the problem, maybe it could have been done that way.
- Solution is to find the LCA and then 'U' for startValue till LCA and append the remainder of the path to the string.
- Instead of finding the LCA, just start from the common prefix index.
