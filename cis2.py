#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swap = 0
    shifted = {}
    shifted = dict(zip(q,[0] * len(q)))
    for i in range(len(q)-1):
        for j in range(len(q)-i-1):
            if q[j] > q[j+1]:
                t = q[j]
                q[j] = q[j+1]
                q[j+1] = t
                swap+=1
                shifted[q[j+1]] +=1
           # print(shifted)

    qs = list(shifted.values())
    qs.sort()
    if(qs[-1] > 2):
        print("Too chaotic")
    else:
        print(swap)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)



    2

    5

    2 1 5 3 4

    5

    2 5 1 3 4