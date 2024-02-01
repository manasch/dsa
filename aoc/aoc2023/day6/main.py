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
        self.times = list(map(int, self.input[0].split(":")[1].split()))
        self.dists = list(map(int, self.input[1].split(":")[1].split()))

    def solveOne(self):
        res = 1
        for idx, t in enumerate(self.times):
            l, r = 0, t
            dist = self.dists[idx]
            while True:
                if dist < l * (t - l):
                    break
                l += 1
            while True:
                if dist < r * (t - r):
                    break
                r -= 1
            res *= (r - l + 1)
        self.partOne = res

    def solveTwo(self):
        time = ""
        dist = ""
        for idx in range(len(self.times)):
            time += str(self.times[idx])
            dist += str(self.dists[idx])
        
        time = int(time)
        dist = int(dist)
        l, r = 0, time
        while True:
            if dist < l * (time - l):
                break
            l += 1
        while True:
            if dist < r * (time - r):
                break
            r -= 1
        res = (r - l + 1)
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