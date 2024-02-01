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
        for time, dist in zip(self.times, self.dists):
            beg, end = 1, time // 2
            
            while beg <= end:
                hold = beg + ((end - beg) >> 1)
                if hold * (time - hold) > dist:
                    end = hold - 1
                else:
                    beg = hold + 1

            window = 2 * ((time // 2) - beg + 1)
            window += 0 if time % 2 == 1 else -1
            res *= window
        self.partOne = res

    def solveTwo(self):
        res = 1
        time = int("".join(list(map(str, self.times))))
        dist = int("".join(list(map(str, self.dists))))

        beg, end = 1, time // 2

        while beg <= end:
            hold = beg + ((end - beg) >> 1)
            if hold * (time - hold) > dist:
                end = hold - 1
            else:
                beg = hold + 1

        res = (time // 2 - beg + 1) * 2
        res += 0 if time % 2 else -1
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