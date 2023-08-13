[[846] - Hand of Straights](https://leetcode.com/problems/hand-of-straights)

---

- Medium
- [Submission](https://leetcode.com/problems/hand-of-straights/submissions/1019929126/)
- array, hash-table, greedy, sorting

---

## Problem Statement

<p>Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size <code>groupSize</code>, and consists of <code>groupSize</code> consecutive cards.</p>

<p>Given an integer array <code>hand</code> where <code>hand[i]</code> is the value written on the <code>i<sup>th</sup></code> card and an integer <code>groupSize</code>, return <code>true</code> if she can rearrange the cards, or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice&#39;s hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,4,5], groupSize = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice&#39;s hand can not be rearranged into groups of 4.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hand.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hand[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= groupSize &lt;= hand.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1296: <a href="https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a></p>


---

## Solution

```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        if (n % groupSize != 0) {
            return false;
        }
        map<int, int> freq;
        for (auto h: hand) {
            ++freq[h];
        }

        while (!freq.empty()) {
            int start = freq.begin()->first;
            for (int i = 0; i < groupSize; ++i) {
                if (freq.find(start + i) == freq.end()) {
                    return false;
                }
                else {
                    --freq[start + i];
                }
                if (freq[start + i] == 0) {
                    freq.erase(start + i);
                }
            }
        }
        return true;
    }
};
```

---

## Notes

- If the size of the hand is not divisible by the group size, return false then and there.
- Have a frequence of the count of each type of card, starting from the minimum, if a group of size 3 can't be formed, return false there itself, update min value each time it is removed completely.
