[[2342] - Max Sum of a Pair With Equal Sum of Digits](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits)

---

- Medium
- [Submission](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/submissions/1540062001/)
- array, hash-table, sorting, heap-priority-queue
- Contest: none

---

## Problem Statement

<p>You are given a <strong>0-indexed</strong> array <code>nums</code> consisting of <strong>positive</strong> integers. You can choose two indices <code>i</code> and <code>j</code>, such that <code>i != j</code>, and the sum of digits of the number <code>nums[i]</code> is equal to that of <code>nums[j]</code>.</p>

<p>Return <em>the <strong>maximum</strong> value of </em><code>nums[i] + nums[j]</code><em> that you can obtain over all possible indices </em><code>i</code><em> and </em><code>j</code><em> that satisfy the conditions.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [18,43,36,13,7]
<strong>Output:</strong> 54
<strong>Explanation:</strong> The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,12,19,14]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no two numbers that satisfy the conditions, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int, priority_queue<int, vector<int>, greater<>>> mp;

        auto digitSum = [] (int num) -> int {
            int res = 0;
            while (num > 0) {
                res += (num % 10);
                num /= 10;
            }
            return res;
        };

        for (const int& num: nums) {
            int ds = digitSum(num);
            auto& pq = mp[ds];
            pq.push(num);

            if (pq.size() > 2) {
                pq.pop();
            }
        }

        int res = 0;
        for (auto& [k, v]: mp) {
            int s = 0;
            if (v.size() == 2) {
                s += v.top();
                v.pop();
                s += v.top();
                v.pop();
                res = max(res, s);
            }
        }
        return res == 0 ? -1 : res;
    }
};
```

---

## Notes

- pretty straightforward, keep track of the digit sums, use a priority_queue (min-heap) to store the greatest 2 values for each digit sum.

- sum up the 2 greatest values for each digit sum, get highest of all this.

- don't need a priority_queue at all, approach 3 is pretty cool where only the max value come across is stored, as when the next max value is come across, just update the current max for that digit sum and add it with the current element to end up with the max value for the digit sum.
