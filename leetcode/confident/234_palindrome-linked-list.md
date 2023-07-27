[[234] - Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list)

---

- Easy
- [Submission](https://leetcode.com/problems/palindrome-linked-list/submissions/1005130650/)
- linked-list, two-pointers, stack, recursion

---

## Problem Statement

<p>Given the <code>head</code> of a singly linked list, return <code>true</code><em> if it is a </em><span data-keyword="palindrome-sequence"><em>palindrome</em></span><em> or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?

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
    bool isPalindrome(ListNode* head) {
        if (head->next == nullptr) {
            return true;
        }
        ListNode *ptr1 = head;
        ListNode *ptr2 = head;

        while (ptr2->next != nullptr && ptr2->next->next != nullptr) {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next->next;
        }

        ListNode *newHead = ptr1->next;
        ptr1->next = nullptr;

        ptr1 = nullptr;
        ptr2 = newHead;
        ListNode *temp;

        while (ptr2 != nullptr) {
            temp = ptr2->next;
            ptr2->next = ptr1;
            ptr1 = ptr2;
            ptr2 = temp;
        }
        newHead = ptr1;

        ptr1 = head;
        ptr2 = newHead;
        while (ptr2 != nullptr) {
            if (ptr1->val != ptr2->val) {
                return false;
            }
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        return true;
    }
};
```

---

## Notes

- This problem is very similar to `LC#143`. To solve the problem using the constraints provided by the Follow Up, i.e. `O(n)` time and `O(1)` space.
- Find the halfway point of the linked list, split the linked list into two linked lists. Reverse the second linked list.
- The second linked list will always be equal to or smaller than the first part of the linked list, if it is smaller then it could be an odd palindrom, otherwise it could be an even palindrome.
- Traverse both at the same time while checking if the values match.
