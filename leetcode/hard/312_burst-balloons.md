[[312] - Burst Balloons](https://leetcode.com/problems/burst-balloons)

---

- Hard
- [Submission](https://leetcode.com/problems/burst-balloons/submissions/1050196436/)
- array, dynamic-programming

---

## Problem Statement

<p>You are given <code>n</code> balloons, indexed from <code>0</code> to <code>n - 1</code>. Each balloon is painted with a number on it represented by an array <code>nums</code>. You are asked to burst all the balloons.</p>

<p>If you burst the <code>i<sup>th</sup></code> balloon, you will get <code>nums[i - 1] * nums[i] * nums[i + 1]</code> coins. If <code>i - 1</code> or <code>i + 1</code> goes out of bounds of the array, then treat it as if there is a balloon with a <code>1</code> painted on it.</p>

<p>Return <em>the maximum coins you can collect by bursting the balloons wisely</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,5,8]
<strong>Output:</strong> 167
<strong>Explanation:</strong>
nums = [3,1,5,8] --&gt; [3,5,8] --&gt; [3,8] --&gt; [8] --&gt; []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);

        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));

        auto dfs = [&] (auto self, int l, int r) {
            if (l > r) {
                return 0;
            }
            if (dp[l][r] != -1) {
                return dp[l][r];
            }

            dp[l][r] = 0;
            int coins;
            for (int i = l; i <= r; ++i) {
                coins = nums[l - 1] * nums[i] * nums[r + 1];
                coins += self(self, l, i - 1) + self(self, i + 1, r);
                dp[l][r] = max(dp[l][r], coins);
            }
            return dp[l][r];
        };

        return dfs(dfs, 1, n - 2);
    }
};
```

---

## Notes

- Tried a lambda dfs for the first time.
- Well, this problem is beyond me as of now, Instead of going forwards which results in a O(2^n) space complexity, we go backwards, that is, decide what is popped last.
- Have a window defined after modifying the original array by adding 1's to either ends.
- Iterate through each element in that window and assume that element is what is popped last, hence, it would be multiplied with values to the left of the window and right of the window.
- After which, the dfs calls happen to the left window and the right window. The resultant of a window can be cached in a 2d array.
- Definitely have to revisit this problem again.
