# Last updated: 4/13/2026, 2:15:30 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=[]
        c=0
        for i in nums:
            c+=i
            k.append(c)
        return k

        