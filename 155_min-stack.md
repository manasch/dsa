# [[155] - Min Stack](https://leetcode.com/problems/min-stack)

---

- Medium
- [Submission](https://leetcode.com/problems/min-stack/submissions/882378523/)

### cpp
```cpp
class MinStack {
private:
    vector<int> st;
    vector<int> minSt;
public:
    MinStack() {

    }
    
    void push(int val) {
        st.push_back(val);
        if (minSt.empty()) minSt.push_back(val);
        else minSt.push_back(val > minSt.back() ? minSt.back() : val);
    }
    
    void pop() {
        st.pop_back();
        minSt.pop_back();
    }
    
    int top() {
        return st.back();
    }
    
    int getMin() {
        return minSt.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

---

## Notes

- push, pop and top are easy to implement, the trick to perform getMin in O(1) is to use another stack which keeps track of the smallest element at the time of insertion of a new element, this way, the top of that stack will always contain the minimum element in the main stack at all times.
