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

            self.char_map = {
                'T': 'A',
                # 'J': 'B',
                'J': '.',
                'Q': 'C',
                'K': 'D',
                'A': 'E',
            }

    def parse(self):
        self.hands = []
        for line in self.input:
            hand, val = line.split()
            self.hands.append((hand, int(val)))
    
    def score(self, hand):
        """
        5           : Five of a kind
        4 1         : Four of a kind
        3 2         : Full house
        3 1 1       : Three of a kind
        2 2 1       : Two pair
        2 1 1 1     : One pair
        1 1 1 1 1   : High card
        """

        counts = [hand.count(x) for x in hand]
        if 5 in counts:
            return 6
        elif 4 in counts:
            return 5
        elif 3 in counts:
            if 2 in counts:
                return 4
            return 3
        elif 2 in counts:
            if counts.count(1) == 1:
                return 2
            return 1
        return 0

    def solveOne(self):
        def strength(hand):
            return (self.score(hand), "".join([self.char_map.get(x, x) for x in hand]))
        
        hands = sorted(self.hands, key = lambda hand: strength(hand[0]))
        res = 0
        for idx, (hand, val) in enumerate(hands, 1):
            res += idx * val
        self.partOne = res

    def solveTwo(self):
        def all_hands(hand):
            if hand == "":
                return [""]
            return [
                x + y
                for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
                for y in all_hands(hand[1:])
            ]
        
        def strength(hand):
            return (max(map(self.score, all_hands(hand))), "".join([self.char_map.get(x, x) for x in hand]))
        
        hands = sorted(self.hands, key = lambda hand: strength(hand[0]))
        res = 0
        for idx, (hand, val) in enumerate(hands, 1):
            res += idx * val
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