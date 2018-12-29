#!/bin/python
#
 # https://www.hackerrank.com/challenges/non-divisible-subset/problem
 #
 # @author Mehdi Mashayekhi
 #/
# Complete the poisonousPlants function below.
#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
# For any number K, the sum of 2 values (A & B) is evenly divisible by K if 
#the sum of the remainders of A/K + B/K is K.

# For the special case where remainder is 0, given the set of all values which are individually divisible by K, they can't be paired with any others. So, at most 1 value which is evenly divisible by K can be added to the result set.

# For even values of K, the equal remainder is simular to the 0 case. For K = 6, pairs are 1+5, 2+4, 3+3. For values with remainder 3, at most one value can be added to the result set.
    d=collections.defaultdict(list)
    for n in S:
        remainder = n%k
        d[remainder].append(n)
    res = 0
    found=False
    for key,value in d.items():
        if key==0 and not found:
            res+=1
            found=True
            del d[key]
        elif k-key==key:
            res+=1
            del d[key]
        else:
            first = len(d[key])
            del d[key]
            if k-key in d:
                second=len(d[k-key])
                del d[k-key]
            else:
                second=float('-inf')
            res+=max(first,second)
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = map(int, raw_input().rstrip().split())

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()

