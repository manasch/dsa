# [[433] - Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

---

- Medium
- [Submission](https://leetcode.com/submissions/detail/835352974/)

### cpp
```cpp
class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        unordered_set<string> seen;
        queue<string> q;
        
        q.push(start);
        seen.insert(start);
        
        int mutations = 0;
        while (!q.empty()) {
            int qsize = q.size();
            
            for (int j = 0; j < qsize; ++j) {
                string node = q.front();
                q.pop();
                
                if (node == end) return mutations;
                
                for (char x: "AGCT") {
                    for (int i = 0; i < node.size(); ++i) {
                        string adj = node;
                        adj[i] = x;
                        
                        if (!seen.count(adj) && find(bank.begin(), bank.end(), adj) != bank.end()) {
                            q.push(adj);
                            seen.insert(adj);
                        }
                    }
                }
            }
            ++mutations;
        }
        
        return -1;
    }
};
```

---

## Notes

- To be honest, I didn't understand what the question wanted, so I took help from the solution.
- After reading the solution, I understood that we are treating this problem as a graph where each node is a gene and an edge represents one mutation.
- A mutation can be a single letter change in the gene. We are required to find the minimum number of mutations required to reach the end gene from the start. This is basically a BFS search within the graph. Provided that DFS can give the solution too, it is better to use BFS to find shortest path problems.
- Essentially, in every iteration we find the mutation by changing every character, and put it in the queue if the mutation exists in the bank. For that mutation, we again perform set of mutations and keep adding it to the queue after checking in the bank.
- If the end gene cannot be reached from the start gene, we will exit out of the loop and return -1.
