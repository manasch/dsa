[[735] - Asteroid Collision](https://leetcode.com/problems/asteroid-collision)

---

- Medium
- [Submission](https://leetcode.com/problems/asteroid-collision/submissions/999255830/)
- array, stack, simulation

---

## Problem Statement

<p>We are given an array <code>asteroids</code> of integers representing asteroids in a row.</p>

<p>For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.</p>

<p>Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [5,10,-5]
<strong>Output:</strong> [5,10]
<strong>Explanation:</strong> The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [8,-8]
<strong>Output:</strong> []
<strong>Explanation:</strong> The 8 and -8 collide exploding each other.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [10,2,-5]
<strong>Output:</strong> [10]
<strong>Explanation:</strong> The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= asteroids.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= asteroids[i] &lt;= 1000</code></li>
	<li><code>asteroids[i] != 0</code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> result;
        int lastAsteroid, collision;
        bool flag = true;
        for (int asteroid: asteroids) {
            if (asteroid > 0) {
                result.push_back(asteroid);
            }
            else {
                flag = true;
                while (!result.empty() && result.back() > 0) {
                    lastAsteroid = result.back();
                    result.pop_back();
                    collision = lastAsteroid + asteroid;

                    if (collision == 0) {
                        flag = false;
                        break;
                    }
                    else if (collision < 0) {
                        continue;
                    }
                    else {
                        flag = false;
                        result.push_back(lastAsteroid);
                        break;
                    }
                }

                if (flag) {
                    result.push_back(asteroid);
                }
            }
        }
        return result;
    }
};
```

---

## Notes

- Uses the help of a stack. If the asteroid is moving right (+), then just push it into the vector.
- If the asteroid is moving left (-), compare it with the rightmost asteroid in the vector, if it is heavier, then keep popping until it isn't or it finds one of equal weight.
