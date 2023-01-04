# [[238] - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

- Medium
- [Submission](https://leetcode.com/problems/product-of-array-except-self/submissions/871408918/)

### cpp
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
