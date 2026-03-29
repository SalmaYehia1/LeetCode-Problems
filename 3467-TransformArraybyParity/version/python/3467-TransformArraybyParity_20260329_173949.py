# Last updated: 3/29/2026, 5:39:49 PM
1class Solution:
2    def transformArray(self, nums: List[int]) -> List[int]:
3        for i in range(len(nums)):
4            if nums[i]%2==0:
5                nums[i]=0
6            else:
7                nums[i]=1
8        nums.sort()
9        return nums
10                
11        