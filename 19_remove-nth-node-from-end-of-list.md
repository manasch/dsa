[[19] - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

---

- Medium
- [Submission](https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/977714445/)
- linked-list, two-pointers

---

## Problem Statement

<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do this in one pass?</p>


---

## Solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == NULL) {
            return NULL;
        }

        ListNode* left = head;
        ListNode* right = head;

        while (n--) {
            right = right->next;
        }

        if (right == NULL) {
            return head->next;
        }

        while (right->next != NULL) {
            right = right->next;
            left = left->next;
        }

        left->next = left->next->next;
        return head;
    }
};
```

---

## Notes

- This can be easily solved in one traversal, finding the total length of the linked list, and then traversing L - N to remove the node.
- This can also be achieved in one pass, as required by the follow up question. It can be done so by utilizing two pointers. The first pointer will start normally, while the second pointer will start after the first pointer has moved N steps, that way when the first pointer reaches the last node, the second pointer would be N away from the end, pointing to the node to be deleted, which can be done in multiple ways.
