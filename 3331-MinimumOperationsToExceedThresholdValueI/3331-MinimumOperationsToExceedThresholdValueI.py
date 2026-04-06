# Last updated: 4/6/2026, 10:26:31 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.append(k)
        nums.sort()
        return nums.index(k)
        