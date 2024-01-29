import aocd
import heapq
import math

from collections import defaultdict, deque

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.readlines()
            self.partOne = None
            self.partTwo = None

    def parse(self):
        pass

    def solveOne(self):
        res = 0
        for line in self.input:
            line = line.strip()
            n = len(line)

            start = 0
            end = n - 1

            try:
                while not line[start].isnumeric() and start < n:
                    start += 1
                while not line[end].isnumeric() and end >= 0:
                    end += -1
                res += int(line[start] + line[end])
            except IndexError as e:
                print(e)
        self.partOne = res

    def solveTwo(self):
        res = 0
        nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for line in self.input:
            line = line.strip()
            n = len(line)
            numList = []
            
            idx = 0
            while idx < n:
                if line[idx].isnumeric():
                    numList.append(line[idx])
                else:
                    for num in nums:
                        if line[idx:].startswith(num):
                            numList.append(str(nums.index(num)))
                            break
                idx += 1
            res += int(numList[0] + numList[-1])
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