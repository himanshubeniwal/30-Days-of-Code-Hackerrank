#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
    if numSwaps == 0:
        break
print('Array is sorted in {} swaps.'.format(numSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
