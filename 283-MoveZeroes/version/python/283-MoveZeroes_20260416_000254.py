# Last updated: 4/16/2026, 12:02:54 AM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        c=[]
4        k=0
5        for i in nums:
6            if i!=0:
7                c+=[i]
8            else:
9                k+=1
10        c+=[0]*k
11        nums[:] = c
12            