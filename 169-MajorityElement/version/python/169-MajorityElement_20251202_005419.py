# Last updated: 12/2/2025, 12:54:19 AM
1class Solution(object):
2    def majorityElement(self, nums):
3        return self.divide(nums, 0, len(nums) - 1)
4
5    def divide(self, nums, left, right):
6        if left == right:
7            return nums[left]
8        
9        mid = (left + right) // 2
10        
11        
12        leftMajor = self.divide(nums, left, mid)
13        rightMajor = self.divide(nums, mid + 1, right)
14        
15        if leftMajor == rightMajor:
16            return leftMajor
17        
18        leftCount = self.count(nums, left, right, leftMajor)
19        rightCount = self.count(nums, left, right, rightMajor)
20        
21        return leftMajor if leftCount > rightCount else rightMajor
22
23    def count(self, nums, left, right, target):
24        c = 0
25        for i in range(left, right + 1):
26            if nums[i] == target:
27                c += 1
28        return c
29
30
31        