import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque
from functools import reduce

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().split("\n\n")
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.sequence = self.input[0]
        self.n = len(self.sequence)
        pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
        self.map = {}
        for m in pattern.findall(self.input[1]):
            self.map[m[0]] = (m[1], m[2])

    def solveOne(self):
        steps = 0
        current = "AAA"
        idx = 0
        while current != "ZZZ":
            current = self.map[current][0 if self.sequence[idx] == 'L' else 1]
            idx = (idx + 1) % self.n
            steps += 1
        self.partOne = steps

    def solveTwo(self):
        steps = []
        current = [x for x in self.map if x[-1] == 'A']
        
        for start in current:
            idx = 0
            s = 0
            while start[-1] != 'Z':
                start = self.map[start][0 if self.sequence[idx] == 'L' else 1]
                idx = (idx + 1) % self.n
                s += 1
            steps.append(s)
        
        def gcd(a, b):
            if b > a:
                return gcd(b, a)
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        def lcm(a, b):
            return int((a * b) / gcd(a, b))
        
        self.partTwo = reduce(lcm, steps)

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