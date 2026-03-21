# Last updated: 3/21/2026, 7:40:25 PM
1class Solution:
2    def alternatingSum(self, nums: List[int]) -> int:
3        k=0
4        n=len(nums)
5        for i in range(n):
6            if i%2==0:
7                k+=nums[i]
8            else:
9                k-=nums[i]
10        return k