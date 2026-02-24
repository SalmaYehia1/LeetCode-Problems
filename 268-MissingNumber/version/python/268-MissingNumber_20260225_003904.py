# Last updated: 2/25/2026, 12:39:04 AM
1class Solution(object):
2    def missingNumber(self, nums):
3        n=len(nums)
4        for i in range(n+1):
5            if i  not in nums:
6                return i
7
8
9        
10        