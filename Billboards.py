############################question############################
# there are n billboard locations, and no more than k consecutive billboards be up at any given time
#Given n, k, and the revenue value of each of the  billboards, find and print the maximum profit 
# example, n=6, k=2, revenue = [1,2,3,1,6,10], maximum revenue is 21
#We remove the first and fourth billboards, which gives us the configuration _ 2 3 _ 6 10 
#and a profit of 2+3+6+10=21. As no other configuration has a profit greater than 21, we print 21 as our answer. 


####solution###################################################3
#Let f[i] denote, for given the first i billboards, the minimum profit we have to sacrifice. Obviously,  
#f[i]=0 if i<=k . When i>k, we have to give up some billboards.
#Specifically, among the rightmost k+1 billboards, we have to give up at least one. 
#Therefore, we can enumerate the rightmost billboard, say at position j, 
#that we want to drop. After dropping the j-th billboard, we are now facing a subproblem, i.e.,
#we are given the first j-1  billboards, and we want to know the minimum profit we have to sacrifice.
#Of course f[j-1],  is the optimal solution to that subproblem. Thus,

# f[i] = 0 if i<=k
# else: f[i] = min(f[j-1]+revenue[j]) for j in range(i-k,i), and final answer is total_revenue -f[n]

def billboards(k, revenue):
    #
    # Write your code here.
    #
    
    n=len(revenue)
    f = [0 for _ in range(n+1)]
    a = [0 for _ in range(n+1)]
    a[1:]=revenue
    
    def g(i):
        return f[i-1]+a[i]
        
    queue = collections.deque()
    for i in range(1,k+1):
        while len(queue)>0 and g(i)<=g(queue[-1]):
            queue.pop()
        queue.append(i)
    for i in range(k+1,n+1):
    	#Before adding new element from the tail, we check out whether that element is less than or equal to tail of the queue. 
    	#If so, remove that element from the tail (since that element is old and can never be better than the one to be inserted, hence is useless). 
    	#Repeat this process until tail element is strictly less than the one to be added or  queue is empty. 
    	#This will guarantee that the data in queue is always an increasing sequence. Hence, at any time,
    	# queue.first is simply the answer w.r.t. the current f[i].
        while len(queue)>0 and g(i)<=g(queue[-1]):
            queue.pop()
        queue.append(i)
        f[i]=g(queue[0])
        #If the head element is already out of date w.r.t. the current f[i] , remove it from the head.
        if queue[0]==i-k:
            queue.popleft()
    
    total = sum(revenue)
    return total - f[n]