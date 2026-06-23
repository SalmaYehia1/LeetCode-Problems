# Last updated: 6/24/2026, 12:46:31 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(nums)!=len(set(nums))
4        