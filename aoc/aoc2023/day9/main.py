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
        self.nums = [list(map(int, x.split())) for x in self.input]

    def solveOne(self):
        def extrapolate(nums):
            if all(x == 0 for x in nums):
                return 0
            diffs = [y - x for x, y in list(zip(nums, nums[1:]))]
            return nums[-1] + extrapolate(diffs)
        
        res = 0
        for line in self.nums:
            res += extrapolate(line)
        self.partOne = res

    def solveTwo(self):
        def extrapolate(nums):
            if all(x == 0 for x in nums):
                return 0
            diffs = [y - x for x, y in list(zip(nums, nums[1:]))]
            return nums[0] - extrapolate(diffs)
        
        res = 0
        for line in self.nums:
            res += extrapolate(line)
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