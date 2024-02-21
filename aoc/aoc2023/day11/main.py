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
        self.rows, self.cols = [], []
        for r, row in enumerate(self.input):
            if '#' not in row:
                self.rows.append(r)
        
        for c in range(len(self.input[0])):
            for r in range(len(self.input)):
                if self.input[r][c] == '#':
                    break
            else:
                self.cols.append(c)

    def solveOne(self):
        galaxies = []
        row_idx, col_idx = 0, 0

        for r, row in enumerate(self.input):
            if row_idx < len(self.rows) and  r == self.rows[row_idx]:
                row_idx += 1
            col_idx = 0
            for c, ch in enumerate(row):
                if col_idx < len(self.cols) and c == self.cols[col_idx]:
                    col_idx += 1
                if ch == '#':
                    galaxies.append((r + row_idx, c + col_idx))
        
        res = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        self.partOne = res

    def solveTwo(self):
        galaxies = []
        row_idx, col_idx = 0, 0

        for r, row in enumerate(self.input):
            if row_idx < len(self.rows) and  r == self.rows[row_idx]:
                row_idx += 1
            col_idx = 0
            for c, ch in enumerate(row):
                if col_idx < len(self.cols) and c == self.cols[col_idx]:
                    col_idx += 1
                if ch == '#':
                    galaxies.append((r + (row_idx * 999999), c + (col_idx * 999999)))
        
        res = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
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