# There are n bulbs in a straight line, numbered from 0 to n-1 . Each bulb i has a button associated with it, 
# and there is a cost, ci , for pressing this button. When some button i is pressed, all the bulbs at a distance k from bulb  
# will be toggled(off->on, on->off).
# Given n,k , and the costs for each button, find and print the minimum cost of turning off all n bulbs if they're all on initially.


############# First solution ##############
# o(nk) solution
def turnOfflight(n,k,c):

    """
    n is number of lights
    k is distance
    c is cost array
    """
    ans=float('inf')
    # begining must be in range[0,k] inclusive
    for beg in xrange(0,k+1):
        cost=0
        nxt=beg
        while(nxt<=n):
            cost+=c[nxt]
            nxt+=2*k+1
        nxt-=2*k+1
        if nxt+k>=n:
            ans=min(ans,cost)
    return ans

############# second solution ##############
# o(n) solution

def turnOfflight_2(n,k,c):

    dp = [float('inf') for i in xrange(n+ 1)]
    dp[0] = 0

    for i in xrange(1, n+1):
        dp[min(i+k, n)] = min(dp[min(i+k, n)], dp[max(i-k-1, 0)] + c[i-1])
    return dp[n]