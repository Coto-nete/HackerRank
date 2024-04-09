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
    n=0
    z=0
    p=0
    for c in arr:
        if c<0:
            n+=1
        elif c>0:
            p+=1
        else:
            z+=1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
