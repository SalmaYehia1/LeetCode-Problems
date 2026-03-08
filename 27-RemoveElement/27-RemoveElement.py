# Last updated: 3/8/2026, 3:16:34 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        