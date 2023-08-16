[[239] - Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)

---

- Hard
- [Submission](https://leetcode.com/problems/sliding-window-maximum/submissions/1022887978/)
- [Submission](https://leetcode.com/problems/sliding-window-maximum/submissions/1022902081/)
- array, queue, sliding-window, heap-priority-queue, monotonic-queue

---

## Problem Statement

<p>You are given an array of integers&nbsp;<code>nums</code>, there is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the max sliding window</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong> 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


---

## Solution

```cpp
class Solution {
private:
    void print(map<int, int>& hash) {
        for (auto [k, v]: hash) {
            cout << k << ": " << v << endl; 
        }
        cout << endl;
    }
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        map<int, int, greater<int>> hash;
        vector<int> res;

        for (int i = 0; i < k; ++i) {
            ++hash[nums[i]];
        }
        int l = 0, r = k;
        while (r < n) {
            res.push_back(hash.begin()->first);
            ++hash[nums[r]];
            --hash[nums[l]];
            if (hash[nums[l]] == 0) {
                hash.erase(nums[l]);
            }
            ++l;
            ++r;
        }
        res.push_back(hash.begin()->first);
        return res;
    }
};
```

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> dq;
        vector<int> res;
        int l = 0, r = 0;

        while (r < n) {
            while (!dq.empty() && nums[dq.back()] < nums[r]) {
                dq.pop_back();
            }
            dq.push_back(r);
            if (l > dq.front()) {
                dq.pop_front();
            }

            if (r + 1 >= k) {
                res.push_back(nums[dq.front()]);
                ++l;
            }
            ++r;
        }
        return res;
    }
};
```

---

## Notes

- Initially my implementation was to use a heap (map) and keep track of the largest value that way and also maintaining the size of the map to be of `k` size.
- This had bad memory implications and also slower time as it was `log(k)` to insert and delete from the map. But otherwise it was simple to implement

- The hard part is to get it in `O(n)` time and this can be done with the help of a `deque`.
- It would be a monotonically decreasing `deque`. Insert elements to it on the back such that it is the smallest and pop out everything else.
- At the time of inference, the max element would be at the front.
