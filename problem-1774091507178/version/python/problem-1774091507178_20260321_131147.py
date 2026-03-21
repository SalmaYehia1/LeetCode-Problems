# Last updated: 3/21/2026, 1:11:47 PM
1class Solution:
2    def buildArray(self, nums: List[int]) -> List[int]:
3        ans=[]
4        for i in range(len(nums)):
5            ans.append(nums[nums[i]])
6        return ans
7
8        