[[433] - Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation)

---

- Medium
- [Submission](https://leetcode.com/submissions/detail/835352974/)
- hash-table, string, breadth-first-search

---

## Problem Statement

<p>A gene string can be represented by an 8-character long string, with choices from <code>&#39;A&#39;</code>, <code>&#39;C&#39;</code>, <code>&#39;G&#39;</code>, and <code>&#39;T&#39;</code>.</p>

<p>Suppose we need to investigate a mutation from a gene string <code>startGene</code> to a gene string <code>endGene</code> where one mutation is defined as one single character changed in the gene string.</p>

<ul>
	<li>For example, <code>&quot;AACCGGTT&quot; --&gt; &quot;AACCGGTA&quot;</code> is one mutation.</li>
</ul>

<p>There is also a gene bank <code>bank</code> that records all the valid gene mutations. A gene must be in <code>bank</code> to make it a valid gene string.</p>

<p>Given the two gene strings <code>startGene</code> and <code>endGene</code> and the gene bank <code>bank</code>, return <em>the minimum number of mutations needed to mutate from </em><code>startGene</code><em> to </em><code>endGene</code>. If there is no such a mutation, return <code>-1</code>.</p>

<p>Note that the starting point is assumed to be valid, so it might not be included in the bank.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> startGene = &quot;AACCGGTT&quot;, endGene = &quot;AACCGGTA&quot;, bank = [&quot;AACCGGTA&quot;]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> startGene = &quot;AACCGGTT&quot;, endGene = &quot;AAACGGTA&quot;, bank = [&quot;AACCGGTA&quot;,&quot;AACCGCTA&quot;,&quot;AAACGGTA&quot;]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>startGene.length == endGene.length == bank[i].length == 8</code></li>
	<li><code>startGene</code>, <code>endGene</code>, and <code>bank[i]</code> consist of only the characters <code>[&#39;A&#39;, &#39;C&#39;, &#39;G&#39;, &#39;T&#39;]</code>.</li>
</ul>


---

## Solution

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
