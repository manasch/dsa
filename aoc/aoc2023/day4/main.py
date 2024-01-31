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
        pass

    def solveOne(self):
        res = 0
        for line in self.input:
            nums = line.split(": ")[1].split(" | ")
            winning = set(nums[0].split())
            have = set(nums[1].split())
            
            common = winning.intersection(have)
            if common:
                res += pow(2, len(common) - 1)
        self.partOne = res

    def solveTwo(self):
        res = 0
        # games = defaultdict(lambda: 1)
        games = {}
        for game in range(1, len(self.input) + 1):
            games[game] = 1
        
        for idx, line in enumerate(self.input, 1):
            nums = line.split(": ")[1].split(" | ")
            winning = set(nums[0].split())
            have = set(nums[1].split())

            common = winning.intersection(have)
            if common:
                for card in range(idx + 1, idx + len(common) + 1):
                    games[card] += games[idx]
        self.partTwo = sum(games.values())        

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