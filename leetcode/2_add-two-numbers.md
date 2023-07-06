[[2] - Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

---

- Medium
- [Submission](https://leetcode.com/problems/add-two-numbers/submissions/977807652/)
- linked-list, math, recursion

---

## Problem Statement

<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
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
private:
    int carry = 0;
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL && l2 == NULL && carry == 0) {
            return NULL;
        }

        int temp = carry;
        if (l1) temp += l1->val;
        if (l2) temp += l2->val;

        ListNode* node = new ListNode(temp % 10);
        carry = temp / 10;

        node->next = addTwoNumbers(l1 ? l1->next : NULL, l2 ? l2->next : NULL);
        return node;
    }
};
```

---

## Notes

- Already did this problem before, but last time did it in iterative method, tried to do it in recursive and got it first try, was pretty fun.
- Just required to check if l1, l2 is not null and that carry doesn't exist.
- Time and space complexity would be `O(n)`. Iterative method would use `O(1)` space.
