########################Question#################
#Modify The Sequence; You are given a sequence of integers a1,a2,a3.....an (a1>0). 
# You are free to replace any integer with any other positive integer. 
# How many integers must be replaced to make the resulting sequence strictly increasing?

# example 1 2 2 3 4 ---> answer=3; 7 8 9 10 1 2 3 4 5 6--> ans=6

# #############Solution########################################
#Note that for each element of modified sequence we have bi >= i (1<=i<=n) and we need to find the longest increasing 
# subsequence of the original sequence ai and ai >= i. We keep such ai unchanged and other values can be changed into the 
# value as their index. If we make another ci = ai – i， the answer is the equal to n – the longest of the non-decreasing subsequence 
# with no negative number. 
# For the longest non-decreasing subsequence we can use the classic O(nlogn) algorithm or O(n2); both answers below

# Let us make a new sequence using the transformation: y[i] = x[i] - i.
# Secondly, the problem has now changed into the following problem: after modifying the elements of sequence y all the elements must 
# be non-negative (that is y[i]' >= 0) and the sequence must be non-decreasing. (That is y[i]' >= y[i - 1]' which means x[i]' - x[i - 1]' >= 1).

# For the new problem, it is the same as finding the longest non-decreasing subsequence in sequence y. 
# So we just use y[i] = x[i] - i and eliminate the negative values and find a longest non-decreasing subsequence in it. 
# If the length of the longest non-decreasing m. 
# The answer is n - m. (we can keep the m elements unchanged and others must be changed.)

###############################################################

def modifySequence(arr):
    #
    # Write your code here.
    #
    def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP sOLUTION O(n2)
#         if not nums:
#             return 0
#         dp=[1 for _ in range(len(nums))]
        
#         for i in range(1,len(nums)):
#             for j in range(0,i):
#                 if nums[i]>=nums[j]:
#                     dp[i]=max(dp[i],dp[j]+1)
#         return max(dp)
		# binary search version O(nlogn)

		#tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
        tails = [0] * len(nums)
        size = 0
        #(1) if x is larger than all tails, append it, increase the size by 1
		#(2) if tails[i-1] < x <= tails[i], update tails[i]
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] <= x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

       
    new_arr=[arr[i]-i for i in range(len(arr))]
    new_arr=[a for a in new_arr if a>0]
    length = lengthOfLIS(new_arr)
    return len(arr)-length