#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    filas, columnas = len(arr), len(arr)
    sum_diag_prim, sum_diag_sec = 0, 0
    for fila in range(filas):
        for columna in range(columnas):
            if fila == columna:
                    sum_diag_prim += arr[fila][columna]
            if (fila + columna) == (filas-1):
                    sum_diag_sec += arr[fila][columna]
    return abs(sum_diag_prim - sum_diag_sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
