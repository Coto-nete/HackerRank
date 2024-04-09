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
    mi = arr.copy()
    mi.remove(max(arr))
    ma = arr.copy()
    ma.remove(min(arr))
    a=0
    b=0
    for c in range(len(mi)):
        a += mi[c]
        b += ma[c]
    print(f'{a} {b}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
