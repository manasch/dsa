[[8057] - Rod cutting problem](https://www.codingninjas.com/studio/problems/rod-cutting-problem_800284)

---

- MEDIUM
- Dynamic Programming
- Paytm (One97 Communications Limited), Atlassian, Gartner, Google, Dream11, Ola, Uber, Infosys, IBM, Amazon, Razorpay, Samsung, HCODE Technologies, RedDoorz, Jio Platforms Limited, Cuemath, Country Delight, Nagaaro

---

## Problem Statement

<h4 id="given-a-rod-of-length-n-units-the-rod-can-be-cut-into-different-sizes-and-each-size-has-a-cost-associated-with-it-determine-the-maximum-cost-obtained-by-cutting-the-rod-and-selling-its-pieces">Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost associated with it. Determine the maximum cost obtained by cutting the rod and selling its pieces.</h4>

<h5 id="note">Note:</h5>

<pre><code>1. The sizes will range from 1 to ‘N’ and will be integers.

2. The sum of the pieces cut should be equal to ‘N’.

3. Consider 1-based indexing.
</code></pre>

<details><summary> Detailed explanation (Input/output format, Notes, Images) </summary>
<h5 id="input-format">Input format:</h5>

<pre><code>The first line of input contains an integer ‘T’ denoting the number of test cases.

The next 2 * T lines represent the ‘T’ test cases.

The first line of each test case contains an integer ‘N’ denoting the length of the rod.

The second line of each test case contains a vector ’A’, of size ‘N’ representing the cost of different lengths, where each index of the array is the sub-length and the element at that index is the cost for that sub-length.
</code></pre>

<h4 id="note">Note:</h4>

<pre><code>Since 1-based indexing is considered, the 0th index of the vector will represent sub-length 1 of the rod. Hence the (N - 1)th index would represent the cost for the length ‘N’. 
</code></pre>

<h5 id="output-format">Output Format</h5>

<pre><code>For each test case, print a single line that contains a single integer which is the maximum cost obtained by selling the pieces.

The output of each test case will be printed in a separate line.
</code></pre>

<h4 id="note">Note:</h4>

<pre><code>You do not need to print anything; it has already been taken care of. Just implement the given function.
</code></pre>
</details>

<h5 id="constraints">Constraints:</h5>

<pre><code>1 &lt;= T &lt;= 50
1 &lt;= N &lt;= 100
1 &lt;= A[i] &lt;= 100

Where ‘T’ is the total number of test cases, ‘N’ denotes the length of the rod, and A[i] is the cost of sub-length.

Time limit: 1 sec.
</code></pre>


<h5 id="sample-input-1">Sample Input 1:</h5>

<pre><code>2
5
2 5 7 8 10
8
3 5 8 9 10 17 17 20
</code></pre>

<h5 id="sample-output-1">Sample Output 1:</h5>

<pre><code>12
24
</code></pre>

<h5 id="explanation-of-sample-input-1">Explanation of sample input 1:</h5>

<pre><code>Test case 1:

All possible partitions are:
1,1,1,1,1           max_cost=(2+2+2+2+2)=10
1,1,1,2             max_cost=(2+2+2+5)=11
1,1,3               max_cost=(2+2+7)=11
1,4                 max_cost=(2+8)=10
5                   max_cost=(10)=10
2,3                 max_cost=(5+7)=12
1,2,2               max _cost=(1+5+5)=12    

Clearly, if we cut the rod into lengths 1,2,2, or 2,3, we get the maximum cost which is 12.


Test case 2:

Possible partitions are:
1,1,1,1,1,1,1,1         max_cost=(3+3+3+3+3+3+3+3)=24
1,1,1,1,1,1,2           max_cost=(3+3+3+3+3+3+5)=23
1,1,1,1,2,2             max_cost=(3+3+3+3+5+5)=22
and so on….

If we cut the rod into 8 pieces of length 1, for each piece 3 adds up to the cost. Hence for 8 pieces, we get 8*3 = 24.
</code></pre>

<h5 id="sample-input-2">Sample Input 2:</h5>

<pre><code>1
6
3 5 6 7 10 12
</code></pre>

<h5 id="sample-output-2">Sample Output 2:</h5>

<pre><code>18
</code></pre>


---

## Solution

```cpp
int dfs(vector<int>& p, int n, int len, int idx, vector<int>& dp) {
	if (len == 0) {
		return 0;
	}
	if (len < 0) {
		return -1e8;
	}
	if (dp[len] != -1) {
		return dp[len];
	}
	int temp = -1e8;
	for (int split = idx; split <= n; ++split) {
		temp = max(temp, p[split - 1] + dfs(p, n, len - split, split, dp));
	}
	return dp[len] = temp;
}

int cutRod(vector<int> &price, int n)
{
	vector<int> dp(n + 1, -1);
	return dfs(price, n, n, 1, dp);
}

```

---

## Notes

- This is similar to coin change problem, storing the price for a particular length in the dp
