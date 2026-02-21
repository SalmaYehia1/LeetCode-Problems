# Last updated: 2/21/2026, 1:54:23 PM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        k=set(nums)
        for i in k:
            if nums.count(i)>1:
                continue
            else:
                return i