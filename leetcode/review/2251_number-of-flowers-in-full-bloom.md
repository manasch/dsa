[[2251] - Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom)

---

- Hard
- [Submission](https://leetcode.com/problems/number-of-flowers-in-full-bloom/submissions/1072884687/)
- array, hash-table, binary-search, sorting, prefix-sum, ordered-set

---

## Problem Statement

<p>You are given a <strong>0-indexed</strong> 2D integer array <code>flowers</code>, where <code>flowers[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> means the <code>i<sup>th</sup></code> flower will be in <strong>full bloom</strong> from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> (<strong>inclusive</strong>). You are also given a <strong>0-indexed</strong> integer array <code>people</code> of size <code>n</code>, where <code>people[i]</code> is the time that the <code>i<sup>th</sup></code> person will arrive to see the flowers.</p>

<p>Return <em>an integer array </em><code>answer</code><em> of size </em><code>n</code><em>, where </em><code>answer[i]</code><em> is the <strong>number</strong> of flowers that are in full bloom when the </em><code>i<sup>th</sup></code><em> person arrives.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/ex1new.jpg" style="width: 550px; height: 216px;" />
<pre>
<strong>Input:</strong> flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
<strong>Output:</strong> [1,2,2,2]
<strong>Explanation: </strong>The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/ex2new.jpg" style="width: 450px; height: 195px;" />
<pre>
<strong>Input:</strong> flowers = [[1,10],[3,3]], poeple = [3,3,2]
<strong>Output:</strong> [2,2,1]
<strong>Explanation:</strong> The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= flowers.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>flowers[i].length == 2</code></li>
	<li><code>1 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= people[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        sort(flowers.begin(), flowers.end());
        int n = people.size();
        int f = flowers.size();
        vector<pair<int, int>> sortedPeople;
        for (int i = 0; i < n; ++i) {
            sortedPeople.push_back({people[i], i});
        }
        sort(sortedPeople.begin(), sortedPeople.end());

        priority_queue<int, vector<int>, greater<>> end;
        vector<int> res(n, 0);

        int fptr = 0;
        for (auto& [p, i]: sortedPeople) {
            while (fptr < f && flowers[fptr][0] <= p) {
                end.push(flowers[fptr][1]);
                ++fptr;
            }
            while (!end.empty() && end.top() < p) {
                end.pop();
            }
            res[i] = end.size();
        }
        return res;
    }
};
```

---

## Notes

- At first glance, it felt like an interval problem, and so with such we sort the intervals.
- Just need to keep track of the end for each bloom period, and have the flowers blooming sorted.
- For each person, if he can watch a flower bloom, add that flower's end to the heap.
- Should also make sure to remove from the heap which have gone past the blooming period for the sorted people vector.

