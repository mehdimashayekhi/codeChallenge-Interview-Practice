############################question############################
# take a word composed of lowercase English letters and try to get the maximum 
# possible score by building exactly 2 palindromic subsequences. 
# The score obtained is the product of the length of these 2 subsequences
# example meedhihd --->len(ee)*len(dhihd)-->10

def play_with_words(s):
	n=len(s)
	d=[]
	for i in xrange(n+1):
	    d+=[[]]
	    for j in xrange(n+1):
	        d[i]+=[-1]
	        if i==j:
	            d[i][i]=0

	for i in xrange(n):
	    d[i][i+1]=1


	for i in xrange(2,n+1):
	    for j in xrange(n+1-i):
	        if s[j]==s[j+i-1]:
	            d[j][j+i]=2+d[j+1][j+i-1]
	        else:
	            d[j][j+i]=max(d[j][j+i-1],d[j+1][j+i])
	m=0

	# print d
	for i in xrange(n):
		for j in xrange(i,n):
			m=max(m,d[0][i]*d[j][n])
	return m