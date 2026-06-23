# Last updated: 6/24/2026, 1:52:07 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        if target in nums:
4            return nums.index(target)
5        else:
6            return -1
7        