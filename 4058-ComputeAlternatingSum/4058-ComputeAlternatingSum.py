# Last updated: 4/6/2026, 10:26:18 PM
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        k=0
        n=len(nums)
        for i in range(n):
            if i%2==0:
                k+=nums[i]
            else:
                k-=nums[i]
        return k