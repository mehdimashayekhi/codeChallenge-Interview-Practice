# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.



class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # First Solution
        #TLE passess 20 test cases
#         def helper(curStr,curIndex,nums,S,re):
#             if curIndex==len(nums):
#                 if eval(curStr)==S:
#                     res.append(curStr)
#                 return
#             for op in '+-':
#                 curStr+=op                
#                 helper(curStr+str(nums[curIndex]),curIndex+1,nums,S,re)
#                 curStr=curStr[:-1]
        
#         res=[]
#         helper("",0,nums,S,re)
#         return(len(res))

# Second Solution
# TLE pssess 34 tets cases
#         def helper(curVal,curIndex,nums,S,res):
#             if curIndex==len(nums):
#                 if (curVal)==S:
#                     res[0]+=1
#                 return
              
#             helper(curVal+(nums[curIndex]),curIndex+1,nums,S,res)
#             helper(curVal-(nums[curIndex]),curIndex+1,nums,S,res)
        
#         res=[0]
#         helper(0,0,nums,S,res)
#         return((res[0]))



# Third solution pasess all test cases
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d)
            dic = tdic
        return dic.get(S, 0)