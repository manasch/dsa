[[1095] - Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array)

---

- Hard
- [Submission](https://leetcode.com/problems/find-in-mountain-array/submissions/1073171409/)
- array, binary-search, interactive

---

## Problem Statement

<p><em>(This problem is an <strong>interactive problem</strong>.)</em></p>

<p>You may recall that an array <code>arr</code> is a <strong>mountain array</strong> if and only if:</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>Given a mountain array <code>mountainArr</code>, return the <strong>minimum</strong> <code>index</code> such that <code>mountainArr.get(index) == target</code>. If such an <code>index</code> does not exist, return <code>-1</code>.</p>

<p><strong>You cannot access the mountain array directly.</strong> You may only access the array using a <code>MountainArray</code> interface:</p>

<ul>
	<li><code>MountainArray.get(k)</code> returns the element of the array at index <code>k</code> (0-indexed).</li>
	<li><code>MountainArray.length()</code> returns the length of the array.</li>
</ul>

<p>Submissions making more than <code>100</code> calls to <code>MountainArray.get</code> will be judged <em>Wrong Answer</em>. Also, any solutions that attempt to circumvent the judge will result in disqualification.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> array = [1,2,3,4,5,3,1], target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> array = [0,1,2,4,2,1], target = 3
<strong>Output:</strong> -1
<strong>Explanation:</strong> 3 does not exist in <code>the array,</code> so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= mountain_arr.length() &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= mountain_arr.get(index) &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        unordered_map<int, int> dp;

        int l = 1, r = n - 2;
        int m, peak;
        while (true) {
            m = l + ((r - l) >> 1);
            if (dp.find(m) == dp.end()) {
                dp[m] = mountainArr.get(m);
            }
            if (dp.find(m - 1) == dp.end()) {
                dp[m - 1] = mountainArr.get(m - 1);
            }
            if (dp.find(m + 1) == dp.end()) {
                dp[m + 1] = mountainArr.get(m + 1);
            }

            if (dp[m] > dp[m - 1] && dp[m] > dp[m + 1]) {
                peak = m;
                break;
            }
            else if (dp[m - 1] < dp[m] && dp[m] < dp[m + 1]) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }
        
        l = 0;
        r = peak;
        while (l <= r) {
            m = l + ((r - l) >> 1);
            if (dp.find(m) == dp.end()) {
                dp[m] = mountainArr.get(m);
            }
            if (dp[m] == target) {
                return m;
            }
            else if (dp[m] > target) {
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }

        l = peak;
        r = n - 1;
        while (l <= r) {
            m = l + ((r - l) >> 1);
            if (dp.find(m) == dp.end()) {
                dp[m] = mountainArr.get(m);
            }
            if (dp[m] == target) {
                return m;
            }
            else if (dp[m] > target) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }

        return -1;
    }
};
```

---

## Notes

- This is just 3 binary searches.
    - One to get the peak
    - One to check the left portion of the mountain
    - One to check the right portion of the mountain if target doesn't exist on the left.

- The initial search for peak can be made from `[1, n - 2]`
