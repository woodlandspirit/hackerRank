#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives, negatives, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            positives +=1
        elif i < 0:
            negatives += 1
        else:
            zero += 1
    print(positives / len(arr))
    print(negatives / len(arr))
    print(zero / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)