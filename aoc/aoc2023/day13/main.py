import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().split("\n\n")
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.patterns = [row.split() for row in self.input]
    
    def findMirror1(self, pattern):
        for r in range(1, len(pattern)):
            above = pattern[:r][::-1]
            below = pattern[r:]

            above = above[:len(below)]
            below = below[:len(above)]

            if above == below:
                return r
        return 0
    
    def findMirror2(self, pattern):
        for r in range(1, len(pattern)):
            above = pattern[:r][::-1]
            below = pattern[r:]

            if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
                return r
        return 0

    def solveOne(self):
        res = 0
        for pattern in self.patterns:
            hor = self.findMirror1(pattern)
            res += 100 * hor

            ver = self.findMirror1(list(map("".join, zip(*pattern))))
            res += ver
        
        self.partOne = res

    def solveTwo(self):
        res = 0
        for pattern in self.patterns:
            hor = self.findMirror2(pattern)
            res += 100 * hor

            ver = self.findMirror2(list(map("".join, zip(*pattern))))
            res += ver
        
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