[[706] - Design HashMap](https://leetcode.com/problems/design-hashmap)

---

- Easy
- [Submission](https://leetcode.com/problems/design-hashmap/submissions/1066992117/)
- array, hash-table, linked-list, design, hash-function

---

## Problem Statement

<p>Design a HashMap without using any built-in hash table libraries.</p>

<p>Implement the <code>MyHashMap</code> class:</p>

<ul>
	<li><code>MyHashMap()</code> initializes the object with an empty map.</li>
	<li><code>void put(int key, int value)</code> inserts a <code>(key, value)</code> pair into the HashMap. If the <code>key</code> already exists in the map, update the corresponding <code>value</code>.</li>
	<li><code>int get(int key)</code> returns the <code>value</code> to which the specified <code>key</code> is mapped, or <code>-1</code> if this map contains no mapping for the <code>key</code>.</li>
	<li><code>void remove(key)</code> removes the <code>key</code> and its corresponding <code>value</code> if the map contains the mapping for the <code>key</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyHashMap&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;remove&quot;, &quot;get&quot;]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, 1, -1, null, 1, null, -1]

<strong>Explanation</strong>
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= key, value &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>put</code>, <code>get</code>, and <code>remove</code>.</li>
</ul>


---

## Solution

```cpp
class Node {
public:
    Node(int key, int val, Node *next) : key(key), val(val), next(next) {}
    Node(int key, int val) : key(key), val(val), next(nullptr) {}

    int key, val;
    Node *next;
};

class MyHashMap {
private:
    int s = 10000;
    vector<Node *> table;
public:
    MyHashMap() : table(s, nullptr) {}

    int hash(int key) {
        return key % s;
    }
    
    void put(int key, int value) {
        int h = hash(key);
        Node *ptr = table[h];
        Node *prev = nullptr;

        while (ptr != nullptr && ptr->key != key) {
            prev = ptr;
            ptr = ptr->next;
        }

        if (ptr == nullptr) {
            ptr = new Node(key, value);
            if (prev) {
                prev->next = ptr;
            }
            else {
                table[h] = ptr;
            }
        }
        else {
            ptr->val = value;
        }
    }
    
    int get(int key) {
        int h = hash(key);
        Node *ptr = table[h];

        while (ptr != nullptr && ptr->key != key) {
            ptr = ptr->next;
        }

        if (ptr == nullptr) {
            return -1;
        }
        return ptr->val;
    }
    
    void remove(int key) {
        int h = hash(key);
        Node *ptr = table[h];
        Node *prev = nullptr;

        while (ptr != nullptr && ptr->key != key) {
            prev = ptr;
            ptr = ptr->next;
        }

        if (ptr) {
            if (prev) {
                prev->next = ptr->next;
            }
            else {
                table[h] = ptr->next;
            }
            delete ptr;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
```

---

## Notes

- Designed it using separate chaining hash collision method. 
