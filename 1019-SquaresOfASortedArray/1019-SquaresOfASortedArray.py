# Last updated: 4/13/2026, 2:15:39 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [abs(x) for x in nums]
        arr.sort()
        nums=[]
        for i in arr:
            nums.append(i*i)
        return nums

        