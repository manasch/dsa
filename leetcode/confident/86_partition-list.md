[[86] - Partition List](https://leetcode.com/problems/partition-list)

---

- Medium
- [Submission](https://leetcode.com/problems/partition-list/submissions/1021798475/)
- linked-list, two-pointers

---

## Problem Statement

<p>Given the <code>head</code> of a linked list and a value <code>x</code>, partition it such that all nodes <strong>less than</strong> <code>x</code> come before nodes <strong>greater than or equal</strong> to <code>x</code>.</p>

<p>You should <strong>preserve</strong> the original relative order of the nodes in each of the two partitions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,4,3,2,5,2], x = 3
<strong>Output:</strong> [1,2,2,4,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [2,1], x = 2
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 200]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>-200 &lt;= x &lt;= 200</code></li>
</ul>


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
    ListNode* partition(ListNode* head, int x) {
        if (head == nullptr) {
            return head;
        }
        ListNode *curr = head;
        ListNode *head1 = new ListNode();
        ListNode *head2 = new ListNode();

        ListNode *ptr1 = head1;
        ListNode *ptr2 = head2;

        while (curr != nullptr) {
            if (curr->val < x) {
                ptr1->next = curr;
                ptr1 = ptr1->next;
            }
            else {
                ptr2->next = curr;
                ptr2 = ptr2->next;
            }
            curr = curr->next;
        }
        ptr1->next = nullptr;
        ptr2->next = nullptr;

        ptr1->next = head2->next;
        head = head1->next;
        delete head1;
        delete head2;
        return head;
    }
};
```

---

## Notes

- Can be accomplished in `O(n)` time.
- Keep two separate heads, one for a linked list with values less than `x` and the other for values greater than.
- At the end, attach the second list to the end of the first one.
