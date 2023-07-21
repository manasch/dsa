[[23] - Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

---

- Hard
- [Submission](https://leetcode.com/problems/merge-k-sorted-lists/submissions/999366498/)
- [Submission](https://leetcode.com/problems/merge-k-sorted-lists/submissions/999380782/)
- linked-list, divide-and-conquer, heap-priority-queue, merge-sort

---

## Problem Statement

<p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked-lists into one sorted linked-list and return it.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> will not exceed <code>10<sup>4</sup></code>.</li>
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (auto lst: lists) {
            ListNode* ptr = lst;
            while (ptr != nullptr) {
                pq.push(ptr->val);
                ptr = ptr->next;
            }
        }

        ListNode *head = NULL;
        ListNode *prev = NULL;
        int n;
        while (!pq.empty()) {
            n = pq.top();
            pq.pop();
            ListNode *node = new ListNode(n);
            if (head == nullptr) {
                head = node;
            }
            else {
                prev->next = node;
            }
            prev = node;
        }
        return head;
    }
};
```

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
    ListNode* mergeList(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr && l2 == nullptr) {
            return NULL;
        }

        if (l1 == nullptr) return l2;
        if (l2 == nullptr) return l1;

        ListNode* head = NULL;
        
        if (l1->val <= l2->val) {
            head = l1;
            l1 = l1->next;
        }
        else {
            head = l2;
            l2 = l2->next;
        }

        ListNode *curr = head;
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val <= l2->val) {
                curr->next = l1;
                l1 = l1->next;
            }
            else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;
        }

        if (l1 == nullptr) {
            curr->next = l2;
        }
        else {
            curr->next = l1;
        }
        return head;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return NULL;
        }
        vector<ListNode*> newLists;
        while (lists.size() > 1) {
            for (int i = 0; i < lists.size(); i += 2) {
                ListNode* l1 = lists[i];
                ListNode* l2 = i + 1 < lists.size() ? lists[i + 1] : nullptr;
                newLists.push_back(mergeList(l1, l2));
            }
            lists.clear();
            lists.insert(lists.end(), newLists.begin(), newLists.end());
            newLists.clear();
        }

        return lists[0];
    }
};
```

---

## Notes

- Used a min-heap to store all the numbers and then popped them all out to create the new linked list.
- This can be solved using a similar method in which merge sort is done.
- Create another function which merges two lists at once, and iterate through the vector of lists 2 at a time to merge them and reduce the number of lists to be merged at each iteration by 2.
- When the lists vector has only 1 list remaining return that as the answer.
