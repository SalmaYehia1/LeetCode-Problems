# Last updated: 3/31/2026, 1:26:20 AM
1class Solution:
2    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
3        
4        c=0
5        for i in range(len(nums)):
6            s=bin(i)[2:]
7            if s.count('1')==k:
8                c+=nums[i]
9        return c
10
11                