# Last updated: 3/31/2026, 1:05:30 AM
1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        nums.append(k)
4        nums.sort()
5        return nums.index(k)
6        