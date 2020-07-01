#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'threePalindromicSubstrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING word as parameter.
#

def threePalindromicSubstrings(word = ""):
    # Write your code here
    final = []
    exist = [0] * len(word)
    got = {}
    for i in range(len(word)):
        if(palingdrome(word,0,i)):
            final.append(word[0:i+1])
            got[word[0:i+1]] = (0,i)
        for j in range(i+1,len(word)):
            if(palingdrome(word,i+1,j)):
                final.append(word[i+1:j+1])
                got[word[i+1:j+1]] = (i+1,j)
    
    for i in final:
        if(exist[got[i][0]] > 0 or exist[got[i][1]] > 0):
            final.remove(i)
        else:
            exist[got[i][0]] = 1
            exist[got[i][1]] = 1 
    final = sorted(final, key=len)
    return final[-3:]
def palingdrome(word,ini,end):
    while(ini <= end):
        if(word[ini] == word[end]):
            ini+=1
            end-=1
        else: 
            return False
    return True
if __name__ == '__main__':
    '''fptr = open(os.environ['OUTPUT_PATH'], 'w')

    word = input()

    result = threePalindromicSubstrings(word)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()'''

    a = "tenet"
    indices = {0: 0, 1: 1, 2: 2}
    for i in range(0,len(a)-2):
        if(palingdrome(a,0,i)):
            indices[0] = i
            for j in range(i+1,len(a)-1):
                if(palingdrome(a,i+1,j) and palingdrome(a,j,i)):
                    indices[1] = i+1
                    indices[2] = j+1
    print(indices)