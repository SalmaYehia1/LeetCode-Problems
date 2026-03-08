# Last updated: 3/8/2026, 3:16:26 PM
class Solution(object):
    def singleNumber(self, nums):
        s=set(nums)
        for i in s:
            if nums.count(i)==1:
                return i

        
        