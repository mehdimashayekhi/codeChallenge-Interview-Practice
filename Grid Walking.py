#!/bin/python
# Grid Walking Hacker rank https://www.hackerrank.com/challenges/grid-walking/problem?h_r=internal-search
from __future__ import print_function

import os
import sys

#
# Complete the gridWalking function below.
#
def gridWalking(m, x, D):
    #
    # Write your code here.
    #
    MOD=10**9+7
    n=len(D)
    # First we precompute C(n,k), i.e. the combinatory number of n choose k
    C=[[0 for _ in range(301)] for _ in range(301)]
    for i in range(1,301):
        for j in range(i+1):
            if j==0 or i==j:
                C[i][j]=1
            else:
                C[i][j]=(C[i-1][j-1]+C[i-1][j])%MOD
    
    # We notice every dimension is independent from each other. 
    # So we can solve each dimension separately, then merge them together.
    # We compute the number of ways when we are in dimension i, position j and move k steps.    
    #We represent it as dim1[i][j][k]= dim1[i][j-1][k-1] + dim1[i][j+1][k-1].
    # Compute dim1
    dim1=[[[0 for _ in range(301)] for _ in range(101)] for _ in range(11)]
    
    for i in range(1,n+1):
        for j in range(1,D[i-1]+1):
            dim1[i][j][0]=1  
    
    for i in range(1,n+1):
        for k in range(1,m+1):
            for j in range(1, D[i-1]+1):
                if j==1:
                    dim1[i][j][k] = (dim1[i][j+1][k-1])%MOD
                elif j==D[i-1]:
                    dim1[i][j][k] = (dim1[i][j-1][k-1])%MOD
                else:
                    dim1[i][j][k]= (dim1[i][j-1][k-1] + dim1[i][j+1][k-1])%MOD
    
    
    # now we compute the number of ways if we only use the first k dimensions (dim 1 to k, inclusive) and make i moves.
    # w[k][i] = sum_{j=0 to i, inclusive}(C[i][j] * w[k-1][j] * dim1[k][x[k]][i-j])
    # w[1][i] = dim1[1][x[1]][i]
    # That means we can use first k-1 dimensions and make j moves, and make i-j moves in the k'th dimension. 
    # There're i moves and we can pick any j for the moves in first k-1 dimensions. That's C[i][j].
    
    w=[[0 for _ in range(11)] for _ in range(301)]
    
    for i in range(1,m+1):
        w[1][i]=dim1[1][x[0]][i]
    
    for k in range(1,n+1):
        w[k][0]=1
    
    for k in range(2,n+1):
        for i in range(1,m+1):
            sum_=0
            for j in range(i+1):
                sum_+=(C[i][j]*(w[k-1][j]%MOD)*dim1[k][x[k-1]][i-j])%MOD
        w[k][i]=sum_%MOD
    return w[n][m]
