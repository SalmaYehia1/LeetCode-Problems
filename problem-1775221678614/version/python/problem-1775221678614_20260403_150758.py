# Last updated: 4/3/2026, 3:07:58 PM
1class Solution:
2    def minimumOperations(self, nums: List[int]) -> int:
3        c=0
4        for i in nums:
5            if i%3==1 or i%3==2:
6                c+=1
7        return c
8
9        