[[703] - Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream)

---

- Easy
- [Submission](https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/997745513/)
- tree, design, binary-search-tree, heap-priority-queue, binary-tree, data-stream

---

## Problem Statement

<p>Design a class to find the <code>k<sup>th</sup></code> largest element in a stream. Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Implement <code>KthLargest</code> class:</p>

<ul>
	<li><code>KthLargest(int k, int[] nums)</code> Initializes the object with the integer <code>k</code> and the stream of integers <code>nums</code>.</li>
	<li><code>int add(int val)</code> Appends the integer <code>val</code> to the stream and returns the element representing the <code>k<sup>th</sup></code> largest element in the stream.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;KthLargest&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
<strong>Output</strong>
[null, 4, 5, 5, 8, 8]

<strong>Explanation</strong>
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>.</li>
	<li>It is guaranteed that there will be at least <code>k</code> elements in the array when you search for the <code>k<sup>th</sup></code> element.</li>
</ul>


---

## Solution

```cpp
class KthLargest {
    priority_queue<int, vector<int>, greater<int>> q;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (auto val: nums) {
            q.push(val);
        }
        while (q.size() > k) {
            q.pop();
        }
    }
    
    int add(int val) {
        q.push(val);
        if (q.size() > k)
            q.pop();
        return q.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```

---

## Notes

- Create a heap with the existing elements of size `k`.
- Make this a min heap as this will keep the k'th largest element on the top, making it easy to return the topmost element of the heap.
- This works as no elements are being deleted from the heap.
