# [[2] Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

--

- Medium
- [Submission](https://leetcode.com/submissions/detail/799719218/)

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *p1, *p2;
        ListNode* prev = NULL;
        ListNode* root;
        
        p1 = l1;
        p2 = l2;
        int carry = 0;
        int temp;
        
        while (p1 != NULL || p2 != NULL || carry) {
            ListNode* node = new ListNode;
            node->next = NULL;
            temp = 0;
            
            temp += carry;
            carry = 0;
            
            if (p1) temp += p1->val;
            if (p2) temp += p2->val;
                        
            if (temp >= 10) carry = temp / 10;
            
            node->val = temp % 10;
            
            if (!prev) root = node;
            else prev->next = node;
            
            if (p1) p1 = p1->next;
            if (p2) p2 = p2->next;
            prev = node;
        }
        return root;
    }
};
```

---

## Notes

- It is already given that the numbers are stored in reverse. This can be used to just add the digits sequentially.
- Storing both the numbers in a seperate variable would cause an integer overflow, hence it is required to add the digits and sum up the carry sequentially.
- The case where the 2 numbers are of different lengths can be handled easily, by checking which of the numbers ends first, the tricky edge case would be for these kinds of cases `99 + 1, 999 + 1` where 1 is always a carry and the resultant number is of greater length than both.
- This can be handled by performing a check on the existence of a carry.
