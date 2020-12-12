#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    value = bin(n)[2:]
    
    value = value.split('0')

    maximum = 1
    for item in value:
        if len(item) > maximum:
            maximum = len(item)

    print(maximum)