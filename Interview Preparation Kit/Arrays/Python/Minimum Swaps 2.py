#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    
    for num in range(0, len(arr)):

        while arr[num] != (num + 1):
            index = arr[num] - 1
            arr[num], arr[index] = arr[index], arr[num]
            swaps = swaps + 1

    return swaps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
