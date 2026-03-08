# Last updated: 3/8/2026, 3:16:21 PM
class Solution(object):
    def containsDuplicate(self, nums):
        x=set(nums)
        if len(x)!=len(nums):
            return True
        else:
            return False
       
        