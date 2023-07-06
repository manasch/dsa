[[143] - Reorder List](https://leetcode.com/problems/reorder-list)

---

- Medium
- [Submission](https://leetcode.com/problems/reorder-list/submissions/977701579/)
- linked-list, two-pointers, stack, recursion

---

## Problem Statement

<p>You are given the head of a singly linked-list. The list can be represented as:</p>

<pre>
L<sub>0</sub> &rarr; L<sub>1</sub> &rarr; &hellip; &rarr; L<sub>n - 1</sub> &rarr; L<sub>n</sub>
</pre>

<p><em>Reorder the list to be on the following form:</em></p>

<pre>
L<sub>0</sub> &rarr; L<sub>n</sub> &rarr; L<sub>1</sub> &rarr; L<sub>n - 1</sub> &rarr; L<sub>2</sub> &rarr; L<sub>n - 2</sub> &rarr; &hellip;
</pre>

<p>You may not modify the values in the list&#39;s nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
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
    void reorderList(ListNode* head) {
        ListNode* ptr1 = head;
        ListNode* ptr2 = head;

        while (ptr2->next != NULL && ptr2->next->next != NULL) {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next->next;
        }

        ListNode* secondHead = ptr1->next;
        ptr1->next = NULL;

        ptr2 = secondHead;
        ptr1 = NULL;
        ListNode* temp;

        while (ptr2 != NULL) {
            temp = ptr2->next;
            ptr2->next = ptr1;
            ptr1 = ptr2;
            ptr2 = temp;
        }

        secondHead = ptr1;

        ptr1 = head;
        ptr2 = secondHead;

        while (ptr2) {
            temp = ptr1;
            ptr1 = ptr1->next;
            temp->next = ptr2;
            temp = ptr2;
            ptr2 = ptr2->next;
            temp->next = ptr1;
        }
    }
};
```

---

## Notes

- Uses concepts of reversing a linked list and merging two linked lists.
- Use a fast pointer and a slow pointer to find the middle of the given linked list. Seperate out the second portion.
- Reverse the second portion of the list and merge it with the first part.
