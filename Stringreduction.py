# Solution 1

# Given a string of any combination of three letters ‘a’, ‘b’, and ‘c’, 
#find length of the smallest string that can be obtained by applying the following operation repeatedly:
#Take any two adjacent, distinct characters and replace them with the third.

def stringReduction(str):
	print (str)


	def length_(a ,b ,c ):
		if dp[a][b][c]!=-1 and dp[a][b][c]!=float('inf'):
			return dp[a][b][c]
    	# // If there is only one type of character
		if (a==0 and b==0):
			dp[a][b][c]=c
			return dp[a][b][c]
		if (a==0 and c==0):
			dp[a][b][c]=b
			return dp[a][b][c]
		if (b==0 and c==0):
			dp[a][b][c]=a
			return dp[a][b][c]

		if (a==0):
			dp[a][b][c]=length_(a+1,b-1,c-1)
			return dp[a][b][c]
		if(b==0):
			dp[a][b][c]=length_(a-1,b+1,c-1)
			return dp[a][b][c]
		if(c==0):
			dp[a][b][c]=length_(a-1,b-1,c+1)
			return dp[a][b][c]

		dp[a][b][c]=min(min(length_(a-1,b-1,c+1),length_(a-1,b+1,c-1)),length_(a+1,b-1,c-1))
		return dp[a][b][c]  


	max_len=100
	dp=[[[float('inf') for _ in range(max_len)] for _ in range(max_len)] for _ in range(max_len)]
	count=[0]*3
	
	for i in range(len(str)):
		count[ord(str[i])-ord('a')]+=1
	
	for i in range(count[0]+1):
		for j in range(count[1]+1):
			for k in range(count[2]+1):
				dp[i][j][k]=-1


	print length_(count[0],count[1],count[2])



# solution 2

def stringReduction_2(str):
	mem={}
	
	def Can(st, ed, ch):
		# Given a string can you check if we can reduce a substring to a single character ch?
		if (st,ed,ch) in mem:
			return mem[(st,ed,ch)]
		if st==ed:
			mem[(st,ed,ch)]=(ord(str[st-1])-ord('a')==ch)
			return mem[(st,ed,ch)]
		if ch==0:
			u=1
			v=2
		elif ch==1:
			u=0
			v=2
		else:
			u=0
			v=1

		for k in range(st,ed):
			# print (k,'kkkkkk',u,v)
			if ((Can(k+1,ed,v) and (Can(st,k,u)))  or (Can(st,k,v) and (Can(k+1,ed,u)))):
				# print "yesss"
				mem[(st,ed,ch)] = True
				return mem[(st,ed,ch)]
		mem[(st,ed,ch)] = False
		return mem[(st,ed,ch)]

	max_len=100

	# Let dp[ch][i] be the smallest length of the resultant string which can be achieved by 
	# applying the reduction operation over the prefix ending at position i
	#   in an optimal order such that the characters left on the final string are equal to ch

	# The key observation here is that we must convert a suffix of that prefix to a single character which is equal to  ch

	# So for all j<=i we need to check if we can reduce the suffix starting from index j 
	# ( and ending at index i) to a single character equal to ch . If we can , then dp[ch][i]=min(dp[ch][j-1][i]) for all such .
	dp = [[float('inf') for i in range(max_len)] for _ in range(3)]

	for ch in range(3):
		dp[ch][0]=0

	# if Can(1,4,1):
	# 	print "yesssssss"

	for ch in range(3):
		for i in range(1,len(str)+1):
			for j in range(1,i+1):
				# print ('sunil',j,i,ch)
				if Can(j,i,ch):
					# print ('mehdi',j,i,ch)
					dp[ch][i]=min(dp[ch][i],dp[ch][j-1]+1)
	# print dp

	print min(min(dp[0][len(str)],dp[1][len(str)]),dp[2][len(str)])