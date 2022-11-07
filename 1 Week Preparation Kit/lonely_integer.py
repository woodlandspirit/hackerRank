#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    dicc = dict.fromkeys(a)
    for value in dicc:
        occurrences = a.count(value)
        dicc.update({value: occurrences})
    lonely_int_index = list(dicc.values()).index(1)
    return list(dicc.keys())[lonely_int_index]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
