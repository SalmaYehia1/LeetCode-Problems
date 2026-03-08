# Last updated: 3/8/2026, 3:16:35 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=sorted(set(nums))
        nums[:]=list(n)
        
        return len(n) 