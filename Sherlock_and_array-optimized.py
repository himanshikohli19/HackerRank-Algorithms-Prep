'''
SHERLOCK AND ARRAY - Unoptimized Solution
https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

Watson gives Sherlock an array of integers. His challenge is to find an element of the array
 such that the sum of all elements to the left is equal to the sum of all elements to the right.

Sample Input 0
2
3
1 2 3
4
1 2 3 3

Sample Output 0
NO
YES
'''
#SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    tsum=sum(arr)
    arrlen=len(arr)
    left=0
    for num in arr:
        current=num
        tsum-=current
        if left==tsum:
            return "YES"
        left+=current
    return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
