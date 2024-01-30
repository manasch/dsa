import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque

# Store the starting index of each number, by only checking adjacent cells if it is a symbol
class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().splitlines()
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.rows = len(self.input)
        self.cols = len(self.input[0])

    def solveOne(self):
        startCords = set()
        for r, row in enumerate(self.input):
            for c, ch in enumerate(row):
                if ch.isdigit() or ch == ".":
                    continue
                
                for nr in [r - 1, r, r + 1]:
                    for nc in [c - 1, c, c + 1]:
                        if min(nr, nc) < 0 or nr >= self.rows or nc >= self.cols or not self.input[nr][nc].isdigit():
                            continue
                        while nc > 0 and self.input[nr][nc - 1].isdigit():
                            nc -= 1
                        startCords.add((nr, nc))
        
        res = 0
        for x, y in startCords:
            num = 0
            while y < self.cols and self.input[x][y].isdigit():
                num = num * 10 + int(self.input[x][y])
                y += 1
            res += num
        self.partOne = res

    def solveTwo(self):
        res = 0
        for r, row in enumerate(self.input):
            for c, ch in enumerate(row):
                if ch != "*":
                    continue
                
                cords = set()
                for nr in [r - 1, r, r + 1]:
                    for nc in [c - 1, c, c + 1]:
                        if min(nr, nc) < 0 or nr >= self.rows or nc >= self.cols or not self.input[nr][nc].isdigit():
                            continue
                        while nc > 0 and self.input[nr][nc - 1].isdigit():
                            nc -= 1
                        cords.add((nr, nc))
                
                if len(cords) == 2:
                    nums = []
                    for x, y in cords:
                        num = 0
                        while y < self.cols and self.input[x][y].isdigit():
                            num = num * 10 + int(self.input[x][y])
                            y += 1
                        nums.append(num)
                    res += nums[0] * nums[1]
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