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
        self.grid = tuple(tuple(y for y in x) for x in self.input)
        self.start = (0, 0)
        for i, row in enumerate(self.grid):
            if 'S' in row:
                self.start = (i, row.index('S'))
                break

    def solveOne(self):
        q = deque()
        q.append(self.start)
        seen = None
        steps = 64

        for _ in range(steps):
            seen = set()
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    if min(nx, ny) < 0\
                    or nx >= len(self.grid)\
                    or ny >= len(self.grid[0])\
                    or (nx, ny) in seen\
                    or self.grid[nx][ny] == '#':
                        continue
                    seen.add((nx, ny))
                    q.append((nx, ny))
        self.partOne = len(seen)

    def solveTwo(self):
        q = deque()
        q.append(self.start)
        seen = None
        steps = 64

        for _ in range(steps):
            seen = set()
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    if (nx, ny) in seen or self.grid[nx % len(self.grid)][ny % len(self.grid[0])] == '#':
                        continue
                    seen.add((nx, ny))
                    q.append((nx, ny))
        self.partTwo = len(seen)

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