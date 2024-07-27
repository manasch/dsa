[[2976] - Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i)

---

- Medium
- [Submission](https://leetcode.com/problems/minimum-cost-to-convert-string-i/submissions/1335150140/)
- array, string, graph, shortest-path
- Contest: none

---

## Problem Statement

<p>You are given two <strong>0-indexed</strong> strings <code>source</code> and <code>target</code>, both of length <code>n</code> and consisting of <strong>lowercase</strong> English letters. You are also given two <strong>0-indexed</strong> character arrays <code>original</code> and <code>changed</code>, and an integer array <code>cost</code>, where <code>cost[i]</code> represents the cost of changing the character <code>original[i]</code> to the character <code>changed[i]</code>.</p>

<p>You start with the string <code>source</code>. In one operation, you can pick a character <code>x</code> from the string and change it to the character <code>y</code> at a cost of <code>z</code> <strong>if</strong> there exists <strong>any</strong> index <code>j</code> such that <code>cost[j] == z</code>, <code>original[j] == x</code>, and <code>changed[j] == y</code>.</p>

<p>Return <em>the <strong>minimum</strong> cost to convert the string </em><code>source</code><em> to the string </em><code>target</code><em> using <strong>any</strong> number of operations. If it is impossible to convert</em> <code>source</code> <em>to</em> <code>target</code>, <em>return</em> <code>-1</code>.</p>

<p><strong>Note</strong> that there may exist indices <code>i</code>, <code>j</code> such that <code>original[j] == original[i]</code> and <code>changed[j] == changed[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcd&quot;, target = &quot;acbe&quot;, original = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;d&quot;], changed = [&quot;b&quot;,&quot;c&quot;,&quot;b&quot;,&quot;e&quot;,&quot;b&quot;,&quot;e&quot;], cost = [2,5,5,1,2,20]
<strong>Output:</strong> 28
<strong>Explanation:</strong> To convert the string &quot;abcd&quot; to string &quot;acbe&quot;:
- Change value at index 1 from &#39;b&#39; to &#39;c&#39; at a cost of 5.
- Change value at index 2 from &#39;c&#39; to &#39;e&#39; at a cost of 1.
- Change value at index 2 from &#39;e&#39; to &#39;b&#39; at a cost of 2.
- Change value at index 3 from &#39;d&#39; to &#39;e&#39; at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;aaaa&quot;, target = &quot;bbbb&quot;, original = [&quot;a&quot;,&quot;c&quot;], changed = [&quot;c&quot;,&quot;b&quot;], cost = [1,2]
<strong>Output:</strong> 12
<strong>Explanation:</strong> To change the character &#39;a&#39; to &#39;b&#39; change the character &#39;a&#39; to &#39;c&#39; at a cost of 1, followed by changing the character &#39;c&#39; to &#39;b&#39; at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of &#39;a&#39; to &#39;b&#39;, a total cost of 3 * 4 = 12 is incurred.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcd&quot;, target = &quot;abce&quot;, original = [&quot;a&quot;], changed = [&quot;e&quot;], cost = [10000]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to convert source to target because the value at index 3 cannot be changed from &#39;d&#39; to &#39;e&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= source.length == target.length &lt;= 10<sup>5</sup></code></li>
	<li><code>source</code>, <code>target</code> consist of lowercase English letters.</li>
	<li><code>1 &lt;= cost.length == original.length == changed.length &lt;= 2000</code></li>
	<li><code>original[i]</code>, <code>changed[i]</code> are lowercase English letters.</li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>original[i] != changed[i]</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<int>> matrix(26, vector<int>(26, INT_MAX));
        unordered_map<char, vector<pair<char, int>>> adj;

        for (int i = 0; i < original.size(); ++i) {
            adj[original[i]].push_back({changed[i], cost[i]});
        }

        auto djikstra = [&] (char ch) {
            priority_queue<pair<int, char>, vector<pair<int, char>>, greater<>> pq;
            unordered_set<char> vis;
            int src = ch - 'a';
            int dst;

            pq.push({0, ch});
            while (!pq.empty()) {
                auto [w1, n1] = pq.top();
                pq.pop();

                if (vis.find(n1) != vis.end()) {
                    continue;
                }
                vis.insert(n1);
                dst = n1 - 'a';
                matrix[src][dst] = min(w1, matrix[src][dst]);

                for (auto [n2, w2]: adj[n1]) {
                    if (vis.find(n2) == vis.end()) {
                        pq.push({w1 + w2, n2});
                    }
                }
            }
        };

        for (char ch = 'a'; ch <= 'z'; ++ch) {
            if (adj.find(ch) == adj.end()) {
                continue;
            }
            djikstra(ch);
        }

        // for (int i = 0; i < 26; ++i) {
        //     for (int j = 0; j < 26; ++j) {
        //         cout << (matrix[i][j] == INT_MAX ? -1 : matrix[i][j]) << " ";
        //     }
        //     cout << endl;
        // }

        long long res = 0;
        for (int i = 0; i < source.size(); ++i) {
            int src = source[i] - 'a';
            int dst = target[i] - 'a';
            if (source[i] == target[i]) {
                continue;
            }
            if (adj.find(source[i]) == adj.end() || matrix[src][dst] == INT_MAX) {
                return -1;
            }
            res += matrix[src][dst];
        }
        return res;
    }
};
```

---

## Notes

- This is just finding the shortest path for each character to every other character.
- This problem was essentially designed for `Floyd-Warshall` algorithm.
- Can also perform `Dijkstra` on each character, which is what I did.
