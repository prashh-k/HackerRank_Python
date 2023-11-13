#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    p = 0
    q = 0
    ans = []
    for i in range(0, len(a)):
        if a[i] > b[i]:
            p = p + 1
        elif a[i] < b[i]:
            q = q + 1
        else:
            continue
    ans.append(p)
    ans.append(q)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
