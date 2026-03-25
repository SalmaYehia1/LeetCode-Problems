# Last updated: 3/25/2026, 4:32:41 PM
1class Solution:
2    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
3        # nums.sort()
4        res=[]
5        for i in nums:
6            if nums.count(i) ==2 and i not in res:
7                res.append(i)
8        return res
9            
10        
11        