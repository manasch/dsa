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
        self.dxns = {
            'r': [0, 1],
            'l': [0, -1],
            'u': [-1, 0],
            'd': [1, 0]
        }
        self.m = len(self.input)
        self.n = len(self.input[0])

    def calc(self, i, j, d):
        seen = set()
        energized = set()
        q = deque()
        q.append([i, j, d])

        while q:
            x, y, d = q.popleft()
            
            if min(x, y) < 0 or x >= self.m or y >= self.n:
                continue

            if (x, y, d) in seen:
                continue
            seen.add((x, y, d))
            energized.add((x, y))

            ch = self.input[x][y]
            if ch == '|' and d in 'rl':
                dx, dy = self.dxns['u']
                q.append([x + dx, y + dy, 'u'])
                dx, dy = self.dxns['d']
                q.append([x + dx, y + dy, 'd'])
            elif ch == '-' and d in 'ud':
                dx, dy = self.dxns['r']
                q.append([x + dx, y + dy, 'r'])
                dx, dy = self.dxns['l']
                q.append([x + dx, y + dy, 'l'])
            elif ch == '\\':
                if d == 'l':
                    dx, dy = self.dxns['u']
                    q.append([x + dx, y + dy, 'u'])
                elif d == 'r':
                    dx, dy = self.dxns['d']
                    q.append([x + dx, y + dy, 'd'])
                elif d == 'u':
                    dx, dy = self.dxns['l']
                    q.append([x + dx, y + dy, 'l'])
                else:
                    dx, dy = self.dxns['r']
                    q.append([x + dx, y + dy, 'r'])
            elif ch == '/':
                if d == 'l':
                    dx, dy = self.dxns['d']
                    q.append([x + dx, y + dy, 'd'])
                elif d == 'r':
                    dx, dy = self.dxns['u']
                    q.append([x + dx, y + dy, 'u'])
                elif d == 'u':
                    dx, dy = self.dxns['r']
                    q.append([x + dx, y + dy, 'r'])
                else:
                    dx, dy = self.dxns['l']
                    q.append([x + dx, y + dy, 'l'])
            else:
                dx, dy = self.dxns[d]
                q.append([x + dx, y + dy, d])
        
        # for i in range(m):
        #     row = []
        #     for j in range(n):
        #         if (i, j) in energized:
        #             row.append('#')
        #         else:
        #             row.append('.')
        #     print("".join(row))
        return len(energized)
                
    def solveOne(self):
        self.partOne = self.calc(0, 0, 'r')

    def solveTwo(self):
        max_energized = 0
        for r in range(self.m):
            max_energized = max(max_energized, self.calc(r, 0, 'r'))
            max_energized = max(max_energized, self.calc(r, self.n - 1, 'l'))
        for c in range(self.n):
            max_energized = max(max_energized, self.calc(0, c, 'd'))
            max_energized = max(max_energized, self.calc(self.m - 1, c, 'u'))
        self.partTwo = max_energized

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