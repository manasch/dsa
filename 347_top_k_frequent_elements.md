# [[347] - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

- Medium
- [Submission](https://leetcode.com/problems/top-k-frequent-elements/submissions/871377021/)

### cpp
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> hashmap;
        for (auto x: nums) {
            hashmap[x]++;
        }

        vector<vector<int>> reverseIndex(n + 1);
        for (auto [k, i]: hashmap) {
            reverseIndex[i].push_back(k);
        }

        vector<int> ans;
        for (int i = n; i >= 0; --i) {
            if (ans.size() >= k) break;
            if (reverseIndex[i].size() != 0) {
                ans.insert(ans.end(), reverseIndex[i].begin(), reverseIndex[i].end());
            }
        }

        return ans;
    }
};
```

---

## Notes

- There are multiple ways to solve this problem, the obvious way to solve it would be to create a priority queue of the count of the elements and take the top k, but this would be `O(nlogn)`, this can be improved by taking a heap and only heapify it k times as we only need the top `k` frequent elements, hene making it `O(klogn)`.
- There's an even faster way by using bucket sort, or somewhat of a reverse index, where the index is the count and the value is a vector of elements with that count, the list length is fixed to the length of the given nums list and therefore just iterating through the back of this list and getting the `k` elements will give the answer, `O(n)` space and time.
