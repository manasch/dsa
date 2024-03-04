import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque

class Solution:
    def __init__(self):
        with open("D:\\coding\\aoc\\aoc2023\\day19\\input.txt", encoding="utf-8") as f:
            self.input = f.read().split('\n\n')
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.first = self.input[0].splitlines()
        self.second = self.input[1].splitlines()

        '''
        a > b
        type(a).__gt__(a, b)
        int.__gt__(a, b)
        '''

        self.ops = {
            '>': int.__gt__,
            '<': int.__lt__
        }

        self.workflows = {}
        for workflow in self.first:
            name, rem = workflow[:-1].split('{')
            rules = rem.split(',')
            self.workflows[name] = ([], rules.pop())
            for rule in rules:
                comp, target = rule.split(':')
                key = comp[0]
                operator = comp[1]
                val = int(comp[2:])
                self.workflows[name][0].append([key, operator, val, target])
        
        self.ratings = []
        for rating in self.second:
            values = {}
            for itr in rating[1:-1].split(','):
                var, val = itr.split('=')
                values[var] = int(val)
            self.ratings.append(values)

    def solveOne(self):
        q = deque()

        total = 0
        for rating in self.ratings:
            q.append(self.workflows['in'])
            while q:
                rules, final = q.popleft()
                for rule in rules:
                    key, comp, val, target = rule
                    if self.ops[comp](rating[key], val):
                        if target == 'A':
                            total += sum(rating.values())
                            break
                        elif target == 'R':
                            break
                        else:
                            q.append(self.workflows[target])
                            break
                else:
                    if final == 'A':
                        total += sum(rating.values())
                    elif final == 'R':
                        break
                    else:
                        q.append(self.workflows[final])
        
        self.partOne = total

    def solveTwo(self):
        
        def count(ranges, name='in'):
            if name == 'R':
                return 0
            if name == 'A':
                prod = 1
                for lo, hi in ranges.values():
                    prod *= hi - lo + 1
                return prod
            
            rules, final = self.workflows[name]
            total = 0

            for rule in rules:
                key, comp, n, target = rule
                lo, hi = ranges[key]
                if comp == '<':
                    true_half = (lo, n - 1)
                    false_half = (n, hi)
                else:
                    true_half = (n + 1, hi)
                    false_half = (lo, n)
                if true_half[0] <= true_half[1]:
                    copy = dict(ranges)
                    copy[key] = true_half
                    total += count(copy, target)
                if false_half[0] <= false_half[1]:
                    ranges = dict(ranges)
                    ranges[key] = false_half
                else:
                    break
            else:
                total += count(ranges, final)
            return total
        
        self.partTwo = count({key: (1, 4000)  for key in 'xmas'})

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