#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    arr.sort()
    sum_min = sumArray(arr[:4])
    sum_max = sumArray(arr[1:])
    return sum_min, sum_max


def sumArray(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    result = miniMaxSum(arr)
    print(result[0], result[1])
