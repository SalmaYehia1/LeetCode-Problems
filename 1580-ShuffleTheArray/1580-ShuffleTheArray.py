# Last updated: 4/6/2026, 10:27:43 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
        