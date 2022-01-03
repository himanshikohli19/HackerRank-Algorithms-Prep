'''
MISSING NUMBERS
https://www.hackerrank.com/challenges/missing-numbers/problem

Given two arrays of integers, find which elements in the second array are missing from the first array.

Notes

If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
Return the missing numbers sorted ascending.
Only include a missing number once, even if it is missing multiple times.
The difference between the maximum and minimum numbers in the original list is less than or equal to 100.
'''

#SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    missing = set()
    for n in brr:
        if n in arr:
            arr.remove(n)
        else:
            missing.add(n)
    return sorted(missing)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))

