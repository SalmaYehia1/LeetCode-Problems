# Last updated: 4/6/2026, 10:26:36 PM
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        c=0
        for i in range(len(nums)):
            s=bin(i)[2:]
            if s.count('1')==k:
                c+=nums[i]
        return c

                