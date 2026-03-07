# Last updated: 3/7/2026, 10:34:09 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        n=sorted(set(nums))
4        nums[:]=list(n)
5        
6        return len(n) 