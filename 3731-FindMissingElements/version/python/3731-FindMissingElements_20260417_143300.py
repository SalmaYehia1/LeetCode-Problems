# Last updated: 4/17/2026, 2:33:00 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        m=min(nums)
4        k=max(nums)
5        s=k-m
6        if s==len(nums)-1:
7            return []
8        else:
9            arr=[i for i in range(m,k+1)]
10            diff=list(set(arr)-set(nums))
11            diff.sort()
12        return diff
13           