[[92] - Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii)

---

- Medium
- [Submission](https://leetcode.com/problems/reverse-linked-list-ii/submissions/1042764101/)
- linked-list

---

## Problem Statement

<p>Given the <code>head</code> of a singly linked list and two integers <code>left</code> and <code>right</code> where <code>left &lt;= right</code>, reverse the nodes of the list from position <code>left</code> to position <code>right</code>, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], left = 2, right = 4
<strong>Output:</strong> [1,4,3,2,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [5], left = 1, right = 1
<strong>Output:</strong> [5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>-500 &lt;= Node.val &lt;= 500</code></li>
	<li><code>1 &lt;= left &lt;= right &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in one pass?

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
private:
    ListNode* reverseList(ListNode* start, ListNode* limit) {
        ListNode *curr = start, *prev = limit, *temp;

        while (curr != limit) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *start = head, *end, *prev = nullptr;
        int count = 1;

        while (count < left) {
            ++count;
            prev = start;
            start = start->next;
        }

        end = start;
        while (count < right) {
            ++count;
            end = end->next;
        }

        if (prev == nullptr) {
            head = reverseList(start, end->next);
        }
        else {
            prev->next = reverseList(start, end->next);
        }
        
        return head;
    }
};
```

---

## Notes

- Create a separate function that reverses the portion of the linked list provided, handle the nodes it has to point to after the node has been reversed separately.
