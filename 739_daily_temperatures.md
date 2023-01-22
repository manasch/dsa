# [[739] - Daily Temperatures](https://leetcode.com/problems/daily-temperatures)

---

- Medium
- [Submission](https://leetcode.com/problems/daily-temperatures/submissions/883047943/)

### cpp
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        int current;
        vector<int> answer(n, 0);
        stack<pair<int, int>> st;

        for (int i = 0; i < n; ++i) {
            current = temperatures[i];
            while (!st.empty() && current > st.top().second) {
                answer[st.top().first] = i - st.top().first;
                st.pop();
            }
            st.push(make_pair(i, current));
        }

        return answer;
    }
};
```

---

## Notes

- A simple usage of stack, the trick here is to maintain a stack with its index position and temperature. This stack will always be monotonically decreasing.
- This is because as we iterate through to the temperatures array, we check if the current temperature is greater than the top of the stack, if it is find the difference between the indexes and update the answer array and pop it from the stack. This results in a monotonically decreasing stack. Repeat this until the current temperature is not greater than the top of the stack.
