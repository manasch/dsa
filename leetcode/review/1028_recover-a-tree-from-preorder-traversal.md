[[1028] - Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal)

---

- Hard
- [Submission](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/submissions/1551619092/)
- string, tree, depth-first-search, binary-tree
- Contest: none

---

## Problem Statement

<p>We run a&nbsp;preorder&nbsp;depth-first search (DFS) on the <code>root</code> of a binary tree.</p>

<p>At each node in this traversal, we output <code>D</code> dashes (where <code>D</code> is the depth of this node), then we output the value of this node.&nbsp; If the depth of a node is <code>D</code>, the depth of its immediate child is <code>D + 1</code>.&nbsp; The depth of the <code>root</code> node is <code>0</code>.</p>

<p>If a node has only one child, that child is guaranteed to be <strong>the left child</strong>.</p>

<p>Given the output <code>traversal</code> of this traversal, recover the tree and return <em>its</em> <code>root</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/09/10/recover_tree_ex1.png" style="width: 423px; height: 200px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-2--3--4-5--6--7&quot;
<strong>Output:</strong> [1,2,5,3,4,6,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/09/10/recover_tree_ex2.png" style="width: 432px; height: 250px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-2--3---4-5--6---7&quot;
<strong>Output:</strong> [1,2,5,3,null,6,null,4,null,7]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/09/10/recover_tree_ex3.png" style="width: 305px; height: 250px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-401--349---90--88&quot;
<strong>Output:</strong> [1,401,null,349,88,90]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the original tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
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
    int idx;
    string traversal;
    pair<int, int> extractNum() {
        if (idx >= traversal.size()) {
            return {-1, -1};
        }
        int num = 0;
        int depth = 0;

        while (idx < traversal.size() && traversal[idx] == '-') {
            ++depth;
            ++idx;
        }

        while (idx < traversal.size() && traversal[idx] != '-') {
            num = num * 10 + (traversal[idx] - '0');
            ++idx;
        }

        return make_pair(num, depth);
    }
public:
    TreeNode* recoverFromPreorder(string traversal) {
        this->traversal = traversal;
        this->idx = 0;

        // depth, pointer to node
        stack<pair<int, TreeNode *>> st;
        auto [n, de] = extractNum();
        TreeNode *root = new TreeNode(n);

        TreeNode *node = root;
        st.push({de, node});

        while (!st.empty()) {
            auto [num, d] = extractNum();
            if (num == -1) {
                break;
            }
            while (st.top().first >= d) {
                st.pop();
            }
            TreeNode *temp = new TreeNode(num);
            TreeNode *parent = st.top().second;

            if (parent->left == nullptr) {
                parent->left = temp;
            }
            else if (parent->right == nullptr) {
                parent->right = temp;
            }
            st.push(make_pair(d, temp));
        }
        return root;
    }
};
```

---

## Notes

- got the intuition of how to do it, but it seemed painful doing it recursively.
- checked hint, recommended iterative, starting thinking in iterative version.

- build the tree as we parse the string, keep pushing the new nodes to the parent's left child first and then right.
- if the parsed node's depth is lesser than the top of the stack, we can pop as this is a preorder traversal, it is understood that no other nodes will appear as its children.
- keep popping till the same depth is reached and attach it as the right child.
