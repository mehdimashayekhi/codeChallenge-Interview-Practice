#!/bin/python

import math
import os
import random
import re
import sys
#
 # https://www.hackerrank.com/contests/countercode/challenges/poisonous-plants
 #
 # @author Mehdi Mashayekhi
 #/
# Complete the poisonousPlants function below.
def poisonousPlants(plants):
    min_ = plants[0]
    maxDays = 0
    n = len(plants)

    for i in range(1,n):
        min_=min(min_,plants[i])
        if plants[i]>plants[i-1]:
            last = plants[i]
            days=1
            k=i+1
            while(k<n and plants[k]>min_):
                if plants[k]<=last:
                    last=plants[k]
                    days+=1
                k+=1
            maxDays=max(maxDays,days)

    return maxDays

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = map(int, raw_input().rstrip().split())

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
