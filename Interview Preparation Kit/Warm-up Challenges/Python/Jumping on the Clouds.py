#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = 0
    jumps = 0

    while position < len(c) - 1:
        if position + 2 <= len(c) - 1 and c[position + 2] == 0:
            position = position + 2
            jumps = jumps + 1
        else:
            position = position + 1
            jumps = jumps + 1
    return jumps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
