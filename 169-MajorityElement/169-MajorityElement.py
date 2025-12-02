# Last updated: 12/2/2025, 2:11:56 AM
class Solution(object):
    def majorityElement(self, nums):
        return self.divide(nums, 0, len(nums) - 1)

    def divide(self, nums, left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        
        leftMajor = self.divide(nums, left, mid)
        rightMajor = self.divide(nums, mid + 1, right)
        
        if leftMajor == rightMajor:
            return leftMajor
        
        leftCount = self.count(nums, left, right, leftMajor)
        rightCount = self.count(nums, left, right, rightMajor)
        
        return leftMajor if leftCount > rightCount else rightMajor

    def count(self, nums, left, right, target):
        c = 0
        for i in range(left, right + 1):
            if nums[i] == target:
                c += 1
        return c


        