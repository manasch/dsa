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
        grid = tuple(self.input)
        
        grid = tuple(map("".join, zip(*grid)))        
        grid = tuple("#".join(["".join(sorted(x, reverse=True)) for x in row.split('#')]) for row in grid)
        grid = tuple(map("".join, zip(*grid)))

        res = 0
        for r, row in enumerate(grid):
            res += (len(grid) - r) * row.count('O')
        self.partOne = res

    def solveTwo(self):
        grid = tuple(self.input)

        def cycle():
            nonlocal grid
            for _ in range(4):
                grid = tuple(map("".join, zip(*grid)))        
                grid = tuple("#".join(["".join(sorted(x, reverse=True)) for x in row.split('#')]) for row in grid)
                grid = tuple(row[::-1] for row in grid)
        
        gridSet = {grid}
        gridArray = [grid]
        itr = 0

        while True:
            itr += 1
            cycle()
            if grid in gridSet:
                break
            gridSet.add(grid)
            gridArray.append(grid)
        
        start = gridArray.index(grid)
        idx = (1000000000 - start) % (itr - start) + start
        finalGrid = gridArray[idx]

        res = 0
        for r, row in enumerate(finalGrid):
            res += (len(finalGrid) - r) * row.count('O')
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