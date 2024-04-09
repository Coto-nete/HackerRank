#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if ('AM' in s) and (s[:2]!='12'):
        return s[:-2]
    elif ('AM' in s) and (s[:2]=='12'):
        return '00'+s[2:-2]
    elif ('PM' in s) and s[:2]!='12':
        h = s[:2]
        h = int(h)+12
        return str(h)+s[2:-2]
    elif ('PM' in s) and s[:2]=='12':
        h = '12'
        return str(h)+s[2:-2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
