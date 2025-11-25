# Last updated: 11/25/2025, 5:01:50 PM

        
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        m = [1] * n
        
        for j in range(1, n):
            for i in range(j):
                if nums[j] > nums[i]:
                    m[j] = max(m[j], m[i] + 1)
        
        return max(m)
