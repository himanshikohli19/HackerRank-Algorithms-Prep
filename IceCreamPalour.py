'''
Ice Cream Parlor

Two friends like to pool their money and go to the ice cream parlor.
 They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Sample Input

STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]

Sample Output
1 4
1 2

Explanation

Sunny and Johnny make the following two trips to the parlor:

The first time, they pool together m=4 dollars. Of the five flavors available that day, 
flavors 1 and 4 have a total cost of .
The second time, they pool together m=4 dollars. Of the four flavors available that day, 
flavors 2 and 2 have a total cost of .

'''
#SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    ar2=arr.copy()
    for i in range(len(arr)):
        left=m-arr[i]
        ar2.remove(arr[i])
        if left in ar2:
            return [i+1,((ar2.index(left))+i+2)]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
