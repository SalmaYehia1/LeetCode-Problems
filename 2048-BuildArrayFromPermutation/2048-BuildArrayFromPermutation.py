# Last updated: 4/6/2026, 10:26:48 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

        