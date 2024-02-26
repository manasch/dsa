import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().splitlines()
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.grid = [list(map(int, x)) for x in self.input]

    def solveOne(self):
        m = len(self.input)
        n = len(self.input[0])
        pq = [(0, 0, 0, 0, 0, 0)]
        seen = set()

        res = 0
        while pq:
            loss, x, y, dx, dy, steps = heapq.heappop(pq)

            if (x, y) == (m - 1, n - 1):
                res = loss
                break

            if (x, y, dx, dy, steps) in seen:
                continue
            seen.add((x, y, dx, dy, steps))

            if steps < 3 and (dx, dy) != (0, 0):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    heapq.heappush(pq, (loss + self.grid[nx][ny], nx, ny, dx, dy, steps + 1))
            
            for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                    nx = x + ndx
                    ny = y + ndy
                    if 0 <= nx < m and 0 <= ny < n:
                        heapq.heappush(pq, (loss + self.grid[nx][ny], nx, ny, ndx, ndy, 1))
        
        self.partOne = res

    def solveTwo(self):
        m = len(self.input)
        n = len(self.input[0])
        pq = [(0, 0, 0, 0, 0, 0)]
        seen = set()

        res = 0
        while pq:
            loss, x, y, dx, dy, steps = heapq.heappop(pq)

            if (x, y) == (m - 1, n - 1) and n >= 4:
                res = loss
                break

            if (x, y, dx, dy, steps) in seen:
                continue
            seen.add((x, y, dx, dy, steps))

            if steps < 10 and (dx, dy) != (0, 0):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    heapq.heappush(pq, (loss + self.grid[nx][ny], nx, ny, dx, dy, steps + 1))
            
            if steps >= 4 or (dx, dy) == (0, 0):
                for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                        nx = x + ndx
                        ny = y + ndy
                        if 0 <= nx < m and 0 <= ny < n:
                            heapq.heappush(pq, (loss + self.grid[nx][ny], nx, ny, ndx, ndy, 1))
        
        self.partTwo = res

    def solve(self):
        self.parse()
        self.solveOne()
        self.solveTwo()

    def answer(self):
        print("Part One:", self.partOne)
        print("Part Two:", self.partTwo)

def main():
    solution = Solution()
    solution.solve()
    solution.answer()

if __name__ == "__main__":
    main()