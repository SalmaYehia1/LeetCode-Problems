# Last updated: 2/20/2026, 12:11:02 PM
1class Solution(object):
2    def largestPerimeter(self, nums):
3        
4        nums.sort()
5        for i in range(len(nums) - 1, 1, -1):
6            if nums[i-2] + nums[i-1] > nums[i]:
7                return nums[i-2] + nums[i-1] + nums[i]
8        
9        return 0