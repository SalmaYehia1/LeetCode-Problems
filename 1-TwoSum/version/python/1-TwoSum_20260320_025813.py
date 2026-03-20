# Last updated: 3/20/2026, 2:58:13 AM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        if target in nums:
4            return nums.index(target)
5        else:
6            nums.append(target)
7            nums.sort()
8            return nums.index(target)
9
10            
11            