import aocd
import heapq
import json
import math
import re

from collections import defaultdict, OrderedDict, deque

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().split("\n\n")
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.seeds, *self.blocks = self.input
        self.seeds = list(map(int, self.seeds.split(": ")[1].split()))        
    
    def solveOne(self):
        seeds = self.seeds.copy()

        for block in self.blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))
            new = []
            for seed in seeds:
                for dst, src, rng in ranges:
                    if seed in range(src, src + rng):
                        new.append(seed - src + dst)
                        break
                else:
                    new.append(seed)
            seeds = new
        self.partOne = min(seeds)

    def solveTwo(self):
        seeds = []
        for i in range(0, len(self.seeds), 2):
            seeds.append([self.seeds[i], self.seeds[i] + self.seeds[i + 1]])
        
        for block in self.blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))

            new = []
            while len(seeds) > 0:
                start, end = seeds.pop()
                for dst, src, rng in ranges:
                    os = max(start, src)
                    oe = min(end, src + rng)
                    if os < oe:
                        new.append((os - src + dst, oe - src + dst))
                        if os > start:
                            seeds.append((start, os))
                        if end > oe:
                            seeds.append((oe, end))
                        break
                else:
                    new.append((start, end))
            seeds = new

        self.partTwo = min(seeds)[0]

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