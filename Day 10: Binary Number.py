#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    randomnmbr = bin(n).replace('0b', '0')
    maxii = max(map(len, randomnmbr.split('0')))
    print(maxii)
