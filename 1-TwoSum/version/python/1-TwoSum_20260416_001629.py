# Last updated: 4/16/2026, 12:16:29 AM
1from collections import Counter
2class Solution:
3    def sumOfUnique(self, nums: List[int]) -> int:
4        z=Counter(nums)
5        c=0
6        for x in z:
7            if z[x]==1:
8                c+=x
9        return c
10        