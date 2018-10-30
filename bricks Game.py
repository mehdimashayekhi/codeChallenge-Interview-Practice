#https://www.hackerrank.com/challenges/play-game/problem
def bricksGame(arr):
    #
    # Write your code here.
    #
    n=len(arr)
    
    dp=[0 for _ in range(n)]
    
    curSum=0

    for i in range(n-1,-1,-1):
        curSum+=arr[i]
        if i>=n-3:
            dp[i]=curSum
        else:
            dp[i] = curSum-dp[i+1]
            dp[i] = max(dp[i], curSum-dp[i+2])
            dp[i] = max(dp[i], curSum-dp[i+3])
    return dp[0]