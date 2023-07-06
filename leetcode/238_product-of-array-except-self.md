[[238] - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)

---

- Medium
- [Submission](https://leetcode.com/problems/product-of-array-except-self/submissions/871408918/)
- array, prefix-sum

---

## Problem Statement

<p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)&nbsp;</code>extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>


---

## Solution

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // int n = nums.size();
        // vector<int> prefixmul, postfixmul;
        // prefixmul.push_back(nums[0]);
        // postfixmul.push_back(nums[n - 1]);

        // for (int i = 1; i < n; ++i) {
        //     prefixmul.push_back(prefixmul[i - 1] * nums[i]);
        //     postfixmul.push_back(postfixmul[i - 1] * nums[n - i - 1]);
        // }
        // reverse(postfixmul.begin(), postfixmul.end());

        // vector<int> ans;
        // for (int i = 0; i < n; ++i) {
        //     if (i == 0) ans.push_back(postfixmul[i + 1]);
        //     else if (i == n - 1) ans.push_back(prefixmul[i - 1]);
        //     else ans.push_back(prefixmul[i - 1] * postfixmul[i + 1]);
        // }

        // return ans;

        int n = nums.size();
        vector<int> ans(n);
        int prepost = 1;
        for (int i = 0; i < n; ++i) {
            ans[i] = prepost;
            prepost *= nums[i];
        }

        prepost = 1;
        for (int i = n - 1; i >= 0; --i) {
            ans[i] *= prepost;
            prepost *= nums[i];
        }

        return ans;
    }
};
```

---

## Notes

- Obvious solution would be `O(n^2)`.
- Another solution would be to have 2 other arrays of size `O(n)`, one prefix products and other postfix products.
- The result array would be the products of prefix[i - 1] * postfix[i + 1] while handling edge cases.
- Finally the ideal solution would be to have a value that stores the prefix/postfix till the current index, on first pass store it in `i + 1` location, second pass going in reverse, multiply with value at `i + 1` in reverse.
    ```
    [1, 2, 3, 4]

    First pass
    [1, 1, 2, 6]

    Second pass
    [24, 12, 8, 6]
    ```
