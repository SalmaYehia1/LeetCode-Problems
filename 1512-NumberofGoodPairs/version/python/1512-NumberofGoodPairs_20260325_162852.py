# Last updated: 3/25/2026, 4:28:52 PM
1class Solution:
2    def numIdenticalPairs(self, nums: List[int]) -> int:
3        c=0
4        n=len(nums)
5        for i in range(n):
6            for j in range(i,n):
7                if i < j:
8                    if nums[i]==nums[j]:
9                        c+=1
10        return c
11
12
13
14
15        