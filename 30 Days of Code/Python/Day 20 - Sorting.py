#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

runs = 0
for num in range(n):
    swaps = 0

    for execution in range(n - 1):
        if a[execution] > a[execution + 1]:

            index1 = a.index(a[execution])
            index2 = a.index(a[execution + 1])
            a[index1], a[index2] = a[index2], a[index1]

            swaps = swaps + 1
            runs = runs + 1

    if swaps == 0:
        break

print('Array is sorted in {} swaps.'.format(runs), 'First Element: {}'.format(a[0]), 'Last Element: {}'.format(a[len(a) - 1]), sep='\n')