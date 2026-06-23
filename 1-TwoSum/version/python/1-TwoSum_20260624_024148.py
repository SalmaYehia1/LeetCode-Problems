# Last updated: 6/24/2026, 2:41:48 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n=len(nums)
4        s= n* (n+1)//2
5        return s- sum(nums)
6        