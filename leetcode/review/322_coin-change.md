[[322] - Coin Change](https://leetcode.com/problems/coin-change)

---

- Medium
- [Submission](https://leetcode.com/problems/coin-change/submissions/1005578996/)
- array, dynamic-programming, breadth-first-search

---

## Problem Statement

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        unordered_map<int, int> dp;
        int res = dfs(coins, dp, amount);
        if (res != INT_MAX) {
            return res;
        }
        return -1;
    }
private:
    int dfs(vector<int>& coins, unordered_map<int, int>& dp, int amount) {
        if (amount == 0) {
            return 0;
        }
        if (amount < 0) {
            return INT_MAX;
        }

        if (dp.find(amount) != dp.end()) {
            return dp[amount];
        }
        int minCoins = INT_MAX;
        for (auto c: coins) {
            int res = dfs(coins, dp, amount - c);
            if (res != INT_MAX) {
                minCoins = min(minCoins, res + 1);
            }
        }
        dp[amount] = minCoins;
        return dp[amount];
    }
};
```

---

## Notes

- Done with assist, but getting the hang of dp, perform a dfs, and store the value for later use.
- True DP would be bottom-up where the problem is just solved from the base case.
