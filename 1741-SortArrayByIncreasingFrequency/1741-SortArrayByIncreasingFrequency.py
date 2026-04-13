# Last updated: 4/13/2026, 2:15:28 AM
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        x =sorted(x.items(), key=lambda item: (item[1], -item[0])) #if there is a tie
        res=[]
        
        for i , j in x:

            res+=[i]*j
        return res


        