# Last updated: 2/27/2026, 2:46:47 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        x=set(nums)
4        if len(x)!=len(nums):
5            return True
6        else:
7            return False
8       
9        