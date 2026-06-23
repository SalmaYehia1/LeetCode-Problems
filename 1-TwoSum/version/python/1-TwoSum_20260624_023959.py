# Last updated: 6/24/2026, 2:39:59 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen={}
4
5        for i , n in enumerate(nums):
6            k=target - n 
7            if k in seen:
8                return [seen[target-n],i]
9            seen[n]=i
10        