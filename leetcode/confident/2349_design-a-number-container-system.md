[[2349] - Design a Number Container System](https://leetcode.com/problems/design-a-number-container-system)

---

- Medium
- [Submission](https://leetcode.com/problems/design-a-number-container-system/submissions/1535725760/)
- hash-table, design, heap-priority-queue, ordered-set
- Contest: none

---

## Problem Statement

<p>Design a number container system that can do the following:</p>

<ul>
	<li><strong>Insert </strong>or <strong>Replace</strong> a number at the given index in the system.</li>
	<li><strong>Return </strong>the smallest index for the given number in the system.</li>
</ul>

<p>Implement the <code>NumberContainers</code> class:</p>

<ul>
	<li><code>NumberContainers()</code> Initializes the number container system.</li>
	<li><code>void change(int index, int number)</code> Fills the container at <code>index</code> with the <code>number</code>. If there is already a number at that <code>index</code>, replace it.</li>
	<li><code>int find(int number)</code> Returns the smallest index for the given <code>number</code>, or <code>-1</code> if there is no index that is filled by <code>number</code> in the system.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;NumberContainers&quot;, &quot;find&quot;, &quot;change&quot;, &quot;change&quot;, &quot;change&quot;, &quot;change&quot;, &quot;find&quot;, &quot;change&quot;, &quot;find&quot;]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
<strong>Output</strong>
[null, -1, null, null, null, null, 1, null, 2]

<strong>Explanation</strong>
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= index, number &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>10<sup>5</sup></code> calls will be made <strong>in total</strong> to <code>change</code> and <code>find</code>.</li>
</ul>


---

## Solution

```cpp
class NumberContainers {
private:
    unordered_map<int, int> numAtIdx;
    unordered_map<int, priority_queue<int, vector<int>, greater<>>> smallestIdx;
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        numAtIdx[index] = number;
        smallestIdx[number].push(index);
    }
    
    int find(int number) {
        if (smallestIdx.find(number) == smallestIdx.end()) {
            return -1;
        }
        auto &pq = smallestIdx[number];
        while (!pq.empty()) {
            while (!pq.empty() && number != numAtIdx[pq.top()]) {
                pq.pop();
            }
            if (pq.empty()) {
                break;
            }
            return pq.top();
        }
        return -1;
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
```

---

## Notes

- one map keeps track of what is at the index.
- the other map keeps track of the indices that number was at and updates it lazily.
- when asked to find, check what is currently at the index, if it doesn't match, pop it and check the next value in the pq.
- if it doesn't match at all, return -1, else return the index it is at.
- the only catch, is to use the reference of the priority queue.

- turns out this is the best solution according to the editorial.
