[[700155] - Mirror Tree](https://practice.geeksforgeeks.org/problems/mirror-tree/1)

---

- Easy
- Tree, Data Structures
- Paytm, VMWare, Morgan Stanley, Accolite, Amazon, Microsoft, Samsung, Snapdeal, Ola Cabs, Walmart, Goldman Sachs, Adobe, Google, SAP Labs, Myntra, Belzabar, eBay, PropTiger

---

## Problem Statement

<p><span style="font-size:14px">Given a Binary Tree, convert it into its mirror.<br />
<img alt="MirrorTree1" class="aligncenter size-full wp-image-663" src="https://contribute.geeksforgeeks.org/wp-content/uploads/mirrortrees.jpg" style="height:338px; width:591px" title="MirrorTree1" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></p>

<p><span style="font-size:14px"><strong>Example 1:</strong></span></p>

<pre>
<span style="font-size:14px"><strong>Input:
</strong>      1
&nbsp;   /  \
&nbsp;  2    3
<strong>Output: </strong>3 1 2<strong>
Explanation: </strong>The tree is
&nbsp;&nbsp; 1&nbsp;&nbsp;  (mirror)  1
 /&nbsp;&nbsp;\&nbsp;&nbsp;  =&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /&nbsp; \
2&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;  2
The inorder of mirror is 3 1 2</span>
</pre>

<p><span style="font-size:14px"><strong>Example 2:</strong></span></p>

<pre>
<span style="font-size:14px"><strong>Input:
</strong>      10
&nbsp;    /  \
&nbsp;   20   30
&nbsp;  /  \
&nbsp; 40  60
<strong>Output: </strong>30 10 60 20 40<strong>
Explanation: </strong>The tree is
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10
&nbsp;&nbsp;  /&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;(mirror) /&nbsp;&nbsp;&nbsp; \
&nbsp;  20&nbsp;&nbsp;&nbsp; 30&nbsp;&nbsp;&nbsp; =&gt; &nbsp; 30&nbsp;&nbsp;&nbsp; 20
&nbsp; /&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    /&nbsp;&nbsp;&nbsp;\
&nbsp;40&nbsp; 60&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 60&nbsp;&nbsp;&nbsp;40
The inroder traversal of mirror is
30 10 60 20 40.</span></pre>

<p><span style="font-size:14px"><strong>Your Task:</strong><br />
Just complete the <strong>function mirror()&nbsp;</strong>that takes <strong>node </strong>as <strong>paramter&nbsp; </strong>and convert it into its mirror. The printing is done by the driver code only.</span></p>

<p><span style="font-size:14px"><strong>Expected Time Complexity:&nbsp;</strong>O(N).<br />
<strong>Expected Auxiliary Space:&nbsp;</strong>O(Height of the Tree).</span></p>

<p><span style="font-size:14px"><strong>Constraints:</strong><br />
1 &le; Number of nodes &le; 10<sup>5</sup><br />
1 &le; Data of a node &le; 10<sup>5</sup></span></p>


---

## Solution

```cpp
// function Template for C++

/* A binary tree node has data, pointer to left child
   and a pointer to right child /
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
}; */
class Solution {
  public:
    // Function to convert a binary tree into its mirror tree.
    void mirror(Node* node) {
        // code here
        if (node == nullptr) return;
        
        mirror(node->left);
        mirror(node->right);
        
        swap(node->left, node->right);
    }
};
```

---

## Notes

- Simple recursion and replace at the end.
