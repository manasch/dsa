[[23] - Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

---

- Hard
- [Submission](https://leetcode.com/problems/merge-k-sorted-lists/submissions/999366498/)
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

---

## Notes

- Used a min-heap to store all the numbers and then popped them all out to create the new linked list.
- This can be solved using a similar method in which merge sort is done, will try that next.
