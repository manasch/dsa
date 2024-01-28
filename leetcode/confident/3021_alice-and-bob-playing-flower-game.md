[[3021] - Alice and Bob Playing Flower Game](https://leetcode.com/problems/alice-and-bob-playing-flower-game)

---

- Medium
- [Submission](https://leetcode.com/problems/alice-and-bob-playing-flower-game/submissions/1158843970/)
- 
- Contest: [weekly-contest-382](https://leetcode.com/contest/weekly-contest-382)

---

## Problem Statement

<p>Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are <code>x</code> flowers in the clockwise direction between Alice and Bob, and <code>y</code> flowers in the anti-clockwise direction between them.</p>

<p>The game proceeds as follows:</p>

<ol>
	<li>Alice takes the first turn.</li>
	<li>In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that side.</li>
	<li>At the end of the turn, if there are no flowers left at all, the <strong>current</strong> player captures their opponent and wins the game.</li>
</ol>

<p>Given two integers, <code>n</code> and <code>m</code>, the task is to compute the number of possible pairs <code>(x, y)</code> that satisfy the conditions:</p>

<ul>
	<li>Alice must win the game according to the described rules.</li>
	<li>The number of flowers <code>x</code> in the clockwise direction must be in the range <code>[1,n]</code>.</li>
	<li>The number of flowers <code>y</code> in the anti-clockwise direction must be in the range <code>[1,m]</code>.</li>
</ul>

<p>Return <em>the number of possible pairs</em> <code>(x, y)</code> <em>that satisfy the conditions mentioned in the statement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, m = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, m = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> No pairs satisfy the conditions described in the statement.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    long long flowerGame(int n, int m) {
        long long o1, o2;
        long long e1, e2;
        
        o1 = ceil((double) n / 2);
        e1 = n - o1;
        
        o2 = ceil((double) m / 2);
        e2 = m - o2;
        
        long long s1 = o1 * e2;
        long long s2 = o2 * e1;
        long long res = s1 + s2;
        
        return res;
    }
};
```

---

## Notes

- This is actually pretty easy, you can just find the total number of possible summations and divide by 2, as half would be even sum and half would be odd sum.

- I tried going combinatorics method and find even from both and odd from both and multiple the cross parity. (odd1 * even2 + odd2 * even1)
