# Last updated: 2/21/2026, 1:51:46 PM
1class Solution(object):
2    def singleNumber(self, nums):
3        for i in range(len(nums)):
4            x=nums[i]
5            if nums.count(x)==1:
6                return x
7
8        
9        