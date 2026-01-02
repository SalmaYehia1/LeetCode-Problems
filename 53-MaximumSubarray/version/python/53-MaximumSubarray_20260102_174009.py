# Last updated: 1/2/2026, 5:40:09 PM
1class Solution(object):
2    def maxSubArray(self, nums):
3        if not nums:
4            return float('-inf')
5
6        if len(nums) == 1:
7            return nums[0]
8
9        mid = len(nums) // 2
10
11        left_max = self.maxSubArray(nums[:mid])
12        right_max = self.maxSubArray(nums[mid:])
13        cross_max = self.maxCrossingSum(nums, mid)
14
15        return max(left_max, right_max, cross_max)
16
17    def maxCrossingSum(self, nums, mid):
18        left_sum = float('-inf')
19        curr = 0
20        for i in range(mid - 1, -1, -1):
21            curr += nums[i]
22            left_sum = max(left_sum, curr)
23
24        right_sum = float('-inf')
25        curr = 0
26        for i in range(mid, len(nums)):
27            curr += nums[i]
28            right_sum = max(right_sum, curr)
29
30        return left_sum + right_sum
31