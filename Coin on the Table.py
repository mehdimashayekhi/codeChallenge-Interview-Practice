# Coin on the Table
# https://www.hackerrank.com/challenges/coin-on-the-table/problem
def coinOnTheTable(m, k, board):
    #
    # Write your code here.
    #
    n=len(board)
    
    dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(1001)]
    x=0
    y=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='*':
                x=i
                y=j
                break
    
    
    for i in range(n):
        for j in range(m):
            dp[0][i][j]=float('inf')
    dp[0][0][0]=0
    for s in range(1,k+1):
        for i in range(n):
            for j in range(m):
                dp[s][i][j] = dp[s-1][i][j]
                if i>0: dp[s][i][j]=min(dp[s][i][j], dp[s-1][i-1][j]+int(board[i-1][j]!='D'))
                if i<n-1: dp[s][i][j]=min(dp[s][i][j], dp[s-1][i+1][j]+int(board[i+1][j]!='U'))
                if j<m-1: dp[s][i][j]=min(dp[s][i][j], dp[s-1][i][j+1]+int(board[i][j+1]!='L'))
                if j>0: dp[s][i][j]=min(dp[s][i][j], dp[s-1][i][j-1]+int(board[i][j-1]!='R'))
    if dp[k][x][y]!=float('inf'):
        return dp[k][x][y]
    else:
        return -1