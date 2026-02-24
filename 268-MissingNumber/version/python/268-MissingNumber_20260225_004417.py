# Last updated: 2/25/2026, 12:44:17 AM
1class Solution(object):
2    def missingNumber(self, nums):
3        n=len(nums)
4        nums.sort()
5        for i in range(n+1):
6            if i  not in nums:
7                return i
8
9
10        
11        