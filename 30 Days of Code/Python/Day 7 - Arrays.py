#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    reordered = []
    for element in range(0, len(arr)):
        reordered.append(arr[len(arr) - (1 * (element + 1))])

    result = ''
    for num in reordered:
        result = result + str(num) + ' '

    print(result)