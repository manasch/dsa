#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def assign(arr, pos):
    new_arr = []
    for item in arr:
        new_arr.append(item + pos)
    
    return new_arr

def find_num(s, t, arr):
    count = 0
    for i in arr:
        if s <= i <= t:
            count += 1
    
    return count

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_loc = assign(apples, a)
    oranges_loc = assign(oranges, b)

    print(find_num(s, t, apples_loc))
    print(find_num(s, t, oranges_loc))



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
