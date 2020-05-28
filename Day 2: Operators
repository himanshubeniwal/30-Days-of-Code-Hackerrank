#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = 1
    tax = 1
    meal = meal_cost
    tip = (meal) * (tip_percent/100)
    tax = (meal) * (tax_percent/100)
    overall = meal + tip + tax
    overall = round(overall)
    print(overall)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
