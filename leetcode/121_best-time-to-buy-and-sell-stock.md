[[121] - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

---

- Easy
- [Submission](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/974609974/)
- array, dynamic-programming

---

## Problem Statement

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1)
            return 0;
        
        int buy = 0;
        int sell = 1;
        int profit = 0;

        while (sell < prices.size()) {
            int sp = prices[sell] - prices[buy];
            if (sp <= 0) {
                buy = sell;
            }
            else {
                profit = max(sp, profit);
            }
            ++sell;
        }

        return profit;
    }
};
```

---

## Notes

- This involves utilizing two pointers, left one for the buying day and right one for the selling day.
- Uses a sliding window approach where the left side is always at the lowest price it has come across so far while the right side tries to find the peak
