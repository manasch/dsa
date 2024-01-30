import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.readlines()
            self.partOne = None
            self.partTwo = None
        
        self.balls = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        self.pattern = re.compile("(\d+) (\w+)")

    def parse(self):
        pass

    def solveOne(self):
        res = 0
        for idx, line in enumerate(self.input, 1):
            line = line.strip()
            game, sets = line.split(": ")
            balls_picked = sets.split("; ")
            flag = True
            for pick in balls_picked:
                for match in self.pattern.finditer(pick):
                    if int(match.group(1)) > self.balls.get(match.group(2)):
                        res += idx
                        flag = False
                        break
                if not flag:
                    break
        
        n = len(self.input)
        self.partOne = int(n * (n + 1) / 2) - res

    def solveTwo(self):
        res = 0
        minCountReq = defaultdict(lambda: defaultdict(int))
        for idx, line in enumerate(self.input, 1):
            line = line.strip()
            game, sets = line.split(": ")
            balls_picked = sets.split("; ")
            temp = 1
            for pick in balls_picked:
                for match in self.pattern.finditer(pick):
                    color = match.group(2)
                    count = int(match.group(1))
                    minCountReq[idx][color] = max(minCountReq[idx][color], count)

            for col, cnt in minCountReq[idx].items():
                temp *= int(cnt)
            res += temp
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