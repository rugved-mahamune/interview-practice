#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getRich' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER initialEnergy
#  2. INTEGER_ARRAY energy
#  3. INTEGER_ARRAY coins
#

def getRich(initialEnergy, energy, coins):
    # Write your code here
    kv = dict(zip(coins, energy))
    sum1 = 0
    for i in range(len(energy)):
        if(initialEnergy == 0):
            initialEnergy += energy[i]
        else:
            sum1 += coins[i]
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    initialEnergy = int(input().strip())

    energy_count = int(input().strip())

    energy = []

    for _ in range(energy_count):
        energy_item = int(input().strip())
        energy.append(energy_item)

    coins_count = int(input().strip())

    coins = []

    for _ in range(coins_count):
        coins_item = int(input().strip())
        coins.append(coins_item)

    result = getRich(initialEnergy, energy, coins)

    fptr.write(str(result) + '\n')

    fptr.close()
