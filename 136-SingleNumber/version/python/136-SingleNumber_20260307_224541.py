# Last updated: 3/7/2026, 10:45:41 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        while val in nums:
4            nums.remove(val)
5        return len(nums)
6        