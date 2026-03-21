# Last updated: 3/21/2026, 7:38:33 PM
1class Solution:
2    def alternatingSum(self, nums: List[int]) -> int:
3        k=0
4        n=len(nums)
5        if n==1:
6            return nums[0]
7        elif n%2==0:
8            for i in range(0,n-1,2):
9                k+=nums[i]
10                k-=nums[i+1]
11        else:
12            nums.append(0)
13            for i in range(0,n,2):
14                k+=nums[i]
15                k-=nums[i+1]
16        return k
17        