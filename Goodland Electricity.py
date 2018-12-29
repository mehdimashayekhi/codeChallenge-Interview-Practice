#!/bin/python
#
 # https://www.hackerrank.com/challenges/pylons/problem
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

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    prev=-1
    next_=-1
    count=0
    while(next_<len(arr)-1):
        on=min(next_+k,len(arr)-1)
        while(on>prev):
            if arr[on]==1:
                break
            on-=1
        if on==prev:
            return -1
        next_=on+k-1
        prev=on
        count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


