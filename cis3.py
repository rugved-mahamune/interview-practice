#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the minimumBribes function below.
def minimumBribes(q):
    swap = 0
    reject = False
    for i in range(len(q)):
        t = q[i]-(i+1)
        if(t==1):
            swap+=t
            te = q[i+1]
            q[i+1] = q[i]
            q[i] = te
        elif(t==2):
            swap+=t
            te = q[i+1]
            q[i+1] = q[i]
            q[i] = te
            te = q[i+2]
            q[i+2] = q[i]
            q[i] = te
        elif(t>2):
            print("Too chaotic")
            reject = True
            break
    if (not reject):
        print(swap)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
