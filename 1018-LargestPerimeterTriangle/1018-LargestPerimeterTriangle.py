# Last updated: 3/8/2026, 3:16:09 PM
class Solution(object):
    def largestPerimeter(self, nums):
        
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        
        return 0