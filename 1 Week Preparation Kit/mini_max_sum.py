#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum, max_sum = 0, 0
    arr.sort()
    for i, value in enumerate(arr):
        if i < (len(arr)-1):
            min_sum += value
    for j, value in enumerate(arr):
        if j >= 1:
            max_sum += value
    print(min_sum, end="")
    print(" ", end="")
    print(max_sum)
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)