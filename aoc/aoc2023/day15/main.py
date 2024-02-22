import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque, OrderedDict

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().splitlines()
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.seq = self.input[0].split(',')
    
    def hash(self, seq):
        start = 0
        for ch in seq:
            start += ord(ch)
            start *= 17
            start %= 256
        return start
    
    def solveOne(self):
        self.partOne = sum(map(self.hash, self.seq))

    def solveTwo(self):
        boxes = [OrderedDict() for _ in range(256)]
        
        for seq in self.seq:
            if '=' in seq:
                label, power = seq.split('=')
                power = int(power)
                box = self.hash(label)

                boxes[box][label] = power

            else:
                label = seq[:seq.index('-')]
                box = self.hash(label)

                if label in boxes[box]:
                    boxes[box].pop(label)
        
        res = 0
        for idx, box in enumerate(boxes, 1):
            if box:
                for jdx, (label, power) in enumerate(box.items(), 1):
                    res += idx * jdx * power
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