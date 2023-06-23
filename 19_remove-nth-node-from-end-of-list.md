# [[19] - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

- Medium
- [Submission](https://leetcode.com/submissions/detail/810363670/)

### cpp
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
        ListNode* ptr = head;
        ListNode* delay = head;
        ListNode* prev = NULL;
        
        int i = 0;
        while (ptr != NULL) {
            if (i >= n) {
                prev = delay;
                delay = delay->next;
            }
            ptr = ptr->next;
            ++i;
        }

        // Make ptr point to the node that has to be deleted
        if (prev == NULL) {
            head = delay->next;
        } else {
            prev->next = delay->next;
        }
        return head;
    }
};
```

---

## Notes

- This can be easily solved in one traversal, finding the total length of the linked list, and then traversing L - N to remove the node.
- This can also be achieved in one pass, as required by the follow up question. It can be done so by utilizing two pointers. The first pointer will start normally, while the second pointer will start after the first pointer has moved N steps, that way when the first pointer reaches the last node, the second pointer would be N away from the end, pointing to the node to be deleted, which can be done in multiple ways.
