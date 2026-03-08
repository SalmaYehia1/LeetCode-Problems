# Last updated: 3/8/2026, 3:16:33 PM
class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return float('-inf')

        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2

        left_max = self.maxSubArray(nums[:mid])
        right_max = self.maxSubArray(nums[mid:])
        cross_max = self.maxCrossingSum(nums, mid)

        return max(left_max, right_max, cross_max)

    def maxCrossingSum(self, nums, mid):
        left_sum = float('-inf')
        curr = 0
        for i in range(mid - 1, -1, -1):
            curr += nums[i]
            left_sum = max(left_sum, curr)

        right_sum = float('-inf')
        curr = 0
        for i in range(mid, len(nums)):
            curr += nums[i]
            right_sum = max(right_sum, curr)

        return left_sum + right_sum
