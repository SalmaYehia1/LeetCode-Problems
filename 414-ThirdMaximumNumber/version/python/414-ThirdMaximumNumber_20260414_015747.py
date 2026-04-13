# Last updated: 4/14/2026, 1:57:47 AM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        nums = list(set(nums))          
4        nums.sort(reverse=True)         
5        
6        if len(nums) < 3:
7            return nums[0]              
8        
9        return nums[2]