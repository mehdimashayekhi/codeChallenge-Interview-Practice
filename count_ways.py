################################Question Counting the Ways############################# 
# F(x) is the number of ways to get the value of x given array, 
# return F(l)+...+F(r); example given arr=[1,2,3], l=1, r=6 return 22
# F(1) = 1; F(2) = 2; F(3) = 3; F(4) = 4 ;F(5) = 5; F(6) = 7

def countWays(arr, l, r):
    #
    # Write your code here.
    #
    mod = 10**9+7
    n=len(arr)
    # dp[sum][i]  --> no of ways to have value sume with first i coins (inclusive)
    dp=[[0 for _ in range(n)] for _ in range(r+1)]
    
    for i in range(n):
        # we can have zero sum with any number of coins (i.e., empty set)
        dp[0][i]=1
    
    for sum in range(1, r+1):
        if sum%arr[0]==0: dp[sum][0]=1
    
    for sum in range(1,r+1):
        for j in range(1,n):
            if arr[j]>sum:
                dp[sum][j]=dp[sum][j-1]
            else:
                dp[sum][j]=dp[sum][j-1]+dp[sum-arr[j]][j]
    
            dp[sum][j]%=mod
    
    res=0
    
    for i in range(l,r+1):
        res+=dp[i][n-1]
        res%=mod
    return res