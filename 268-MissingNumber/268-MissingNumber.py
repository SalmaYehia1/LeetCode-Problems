# Last updated: 3/8/2026, 3:16:18 PM
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        nums.sort()
        for i in range(n+1):
            if i  not in nums:
                return i


        
        