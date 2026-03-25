# Last updated: 3/25/2026, 4:29:34 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    ans=ans+1
        return ans
        