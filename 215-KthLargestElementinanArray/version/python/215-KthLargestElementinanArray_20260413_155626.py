# Last updated: 4/13/2026, 3:56:26 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        nums=sorted(nums,reverse=True)
4        return nums[k-1]
5        