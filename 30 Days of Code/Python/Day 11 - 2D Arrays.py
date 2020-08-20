#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    i = 0
    maximum = 0
    while i < (len(arr) - 2):
        j = 0
        while j < (len(arr) - 2):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if total > maximum or (i == 0 and j == 0):
                maximum = total
            j = j + 1
        i = i + 1

    print(maximum)