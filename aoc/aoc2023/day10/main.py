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
        self.m = len(self.input)
        self.n = len(self.input[0])
        for r, row in enumerate(self.input):
            for c, ch in enumerate(row):
                if ch == 'S':
                    self.x = r
                    self.y = c
                    break
            else:
                continue
            break

    def solveOne(self):
        q = deque()
        q.append((self.x, self.y))
        seen = set()
        
        while q:
            r, c = q.popleft()
            seen.add((r, c))
            ch = self.input[r][c]

            if (r > 0) and ch in "S|JL" and self.input[r - 1][c] in "7|F" and (r - 1, c) not in seen:
                q.append((r - 1, c))
            if (r < self.m - 1) and ch in "S|7F" and self.input[r + 1][c] in "LJ|" and (r + 1, c) not in seen:
                q.append((r + 1, c))
            if (c > 0) and ch in "-7SJ" and self.input[r][c - 1] in "-FL" and (r, c - 1) not in seen:
                q.append((r, c - 1))
            if (c < self.n - 1) and ch in "SF-L" and self.input[r][c + 1] in "-J7" and (r, c + 1) not in seen:
                q.append((r, c + 1))
        
        self.partOne = len(seen) // 2

    def solveTwo(self):
        pass

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