[[25] - Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group)

---

- Hard
- [Submission](https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/1016838911/)
- linked-list, recursion

---

## Problem Statement

<p>Given the <code>head</code> of a linked list, reverse the nodes of the list <code>k</code> at a time, and return <em>the modified list</em>.</p>

<p><code>k</code> is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of <code>k</code> then left-out nodes, in the end, should remain as it is.</p>

<p>You may not alter the values in the list&#39;s nodes, only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [2,1,4,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 3
<strong>Output:</strong> [3,2,1,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you solve the problem in <code>O(1)</code> extra memory space?</p>


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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *curr = head, *kptr = head, *newHead = NULL;
        ListNode *prevHead = NULL;
        vector<ListNode *> nodes;
        int n;

        while (true) {
            n = k;
            while (n && kptr != NULL) {
                --n;
                kptr = kptr->next;
            }
            if (n != 0) {
                break;
            }
            nodes = reverseList(curr, kptr);
            if (newHead == NULL) {
                newHead = nodes[0];
                prevHead = nodes[1];
            }
            else {
                prevHead->next = nodes[0];
                prevHead = nodes[1];
            }
            curr = kptr;
        }
        return newHead;
    }
private:
    vector<ListNode *> reverseList(ListNode *head, ListNode *nextHead) {
        ListNode *prev = NULL;
        ListNode *curr = head;
        ListNode *ogHead = head;
        ListNode *temp;

        while (curr != NULL && curr != nextHead) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        ogHead->next = nextHead;
        head = prev;
        return {head, ogHead};
    }
};
```

---

## Notes

- So apparently this was supposed to be done recursively. But ig iteratively it isn't that hard.
- Create a reverse function to reverse k (by sending the kth node as a guard check).
- The key part lies in what's to be returned, can return the original head and the new head, original head will be used to create new pointers in the main function. In the reverse function, I made it point to the kth pointer so that the linked list remains intact.
