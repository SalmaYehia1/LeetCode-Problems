# Last updated: 4/6/2026, 10:26:25 PM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # nums.sort()
        res=[]
        for i in nums:
            if nums.count(i) ==2 and i not in res:
                res.append(i)
        return res
            
        
        