# Last updated: 4/11/2026, 1:27:07 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        
4        arr = list(range(1,len(nums)+1))
5        diff=set(arr)-set(nums)
6        return list(diff)
7       
8
9        