#https://www.hackerrank.com/challenges/mandragora/problem

def mandragora(H):
    # H = [3,2,5]
    #sort the array it's better to eat the least value of health
    H.sort()
    
    n=len(H)
    
    p=H[n-1]*n # if we eat all except last one

    # then start by eating all except last 2, and kepp continue until s is greater than zero
    s = n-2
    sum_=H[-1]

    while(s>=0):
        sum_+=H[s]
        p=max(p,(s+1)*sum_)
        s-=1

    return p