# [[883] - Car Fleet](https://leetcode.com/problems/car-fleet)

---

- Medium
- [Submission](https://leetcode.com/problems/car-fleet/submissions/887263792/)

### cpp
```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        int res = 0;
        map<int, int> pq;
        stack<float> st;
        float t;

        for (int i = 0; i < n; ++i) {
            pq.insert(pair<int, int>(position[i], speed[i]));
        }

        for (auto it = pq.rbegin(); it != pq.rend(); ++it) {
            t = (float) (target - it->first) / (float) it->second;
            if (st.empty()) {
                st.push(t);
            }
            else {
                if (t > st.top()) {
                    ++res;
                    st.push(t);
                }
            }
        }

        return ++res;
    }
};
```

---

## Notes

- Uses two concepts, sorting it by distance and finding out time for each car.
- Traverse backwards, if an earlier car has a greater speed, then it would be slowed down by the car ahead of it, hence keep a stack of the speed of cars while traversing backwards inserting only when the speed is slower. `O(n)` space and `O(nlogn)` time.
